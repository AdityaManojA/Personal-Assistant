"""Voice activity detection and utterance endpointing.

This is the component that decides *when the user stopped talking*, and getting
it right matters more for perceived quality than anything else in the pipeline.
Too eager and you clip people mid-sentence; too patient and every reply feels
sluggish.

Silero VAD v5 runs on onnxruntime, so the install stays free of torch. The
model is stateful and expects exactly 512 samples at 16 kHz, so frames arriving
at 1280 samples are re-sliced internally.
"""

from __future__ import annotations

import logging
from collections import deque
from pathlib import Path

import numpy as np

from .audio import to_float32

log = logging.getLogger(__name__)

CHUNK_16K = 512
CONTEXT_16K = 64
STATE_SHAPE = (2, 1, 128)

# Frames to keep before speech is confirmed, so the first syllable is not clipped.
def _pre_roll_frames(ms: int, frame_samples: int, sample_rate: int) -> int:
    return max(1, int(ms / 1000 * sample_rate / frame_samples))


class SileroVadOnnx:
    """Thin wrapper around silero_vad.onnx (v5 interface)."""

    def __init__(self, model_path: str | Path, sample_rate: int = 16000) -> None:
        import onnxruntime as ort

        path = Path(model_path)
        if not path.exists():
            raise FileNotFoundError(
                f"Silero VAD model not found at {path}. "
                "Run: python scripts/download_models.py"
            )
        opts = ort.SessionOptions()
        # Single-threaded: this runs on 32 ms of audio at a time and the
        # thread-pool overhead costs more than the inference.
        opts.inter_op_num_threads = 1
        opts.intra_op_num_threads = 1
        opts.log_severity_level = 3
        self.session = ort.InferenceSession(
            str(path), sess_options=opts, providers=["CPUExecutionProvider"]
        )
        self.sample_rate = sample_rate
        self._sr = np.array(sample_rate, dtype=np.int64)
        self.reset()

    def reset(self) -> None:
        self._state = np.zeros(STATE_SHAPE, dtype=np.float32)
        self._context = np.zeros((1, CONTEXT_16K), dtype=np.float32)

    def __call__(self, chunk: np.ndarray) -> float:
        """chunk: 512 float32 samples in [-1, 1]. Returns speech probability."""
        window = np.concatenate([self._context, chunk.reshape(1, -1)], axis=1)
        out, self._state = self.session.run(
            None,
            {"input": window.astype(np.float32), "state": self._state, "sr": self._sr},
        )
        self._context = chunk.reshape(1, -1)[:, -CONTEXT_16K:]
        return float(out[0][0])


class Endpointer:
    """Turns a stream of frames into discrete utterances.

    Usage::

        ep = Endpointer(cfg.vad, sample_rate, frame_samples)
        ep.begin()                       # after the wake word fires
        for frame in frames:
            event = ep.feed(frame)
            if event == "utterance_end":
                audio = ep.audio()       # int16, ready for the transcriber
                ep.begin()               # arm for the next one
    """

    def __init__(
        self,
        config,
        sample_rate: int = 16000,
        frame_samples: int = 1280,
        model_path: str | Path | None = None,
    ) -> None:
        self.config = config
        self.sample_rate = sample_rate
        self.frame_samples = frame_samples
        self._pre_roll = _pre_roll_frames(
            config.pre_roll_ms, frame_samples, sample_rate
        )
        self._model = self._load_model(config, model_path)
        self.begin()

    @staticmethod
    def _load_model(config, model_path):
        if getattr(config, "use_onnx", True):
            path = model_path or _default_model_path()
            try:
                return SileroVadOnnx(path, 16000)
            except FileNotFoundError:
                log.warning(
                    "Silero ONNX model missing; falling back to the torch backend. "
                    "Run scripts/download_models.py to stay torch-free."
                )
        from silero_vad import load_silero_vad  # heavy import, only on fallback

        return load_silero_vad()

    # -- state machine -------------------------------------------------------

    def begin(self) -> None:
        """Arm the endpointer. Must be called before feeding frames."""
        try:
            self._model.reset()
        except Exception:
            pass
        self._frames: list[np.ndarray] = []
        self._residual = np.zeros(0, dtype=np.float32)
        self._pending = np.zeros(0, dtype=np.float32)
        self._speaking = False
        self._speech_ms = 0.0
        self._silence_ms = 0.0
        self._waited_ms = 0.0
        self._speech_start_frame: int | None = None
        self._recent: deque[np.ndarray] = deque(maxlen=self._pre_roll)

    def feed(self, frame: np.ndarray) -> str | None:
        """Feed one int16 frame.

        Returns ``"speech_start"``, ``"utterance_end"``, ``"timeout"`` (no
        speech after the wake word), or None.
        """
        frame_ms = len(frame) / self.sample_rate * 1000.0
        self._frames.append(frame)

        if not self._speaking:
            self._recent.append(frame)
            self._waited_ms += frame_ms
            if self._waited_ms > self.config.start_timeout_s * 1000:
                return "timeout"

        probabilities = self._probabilities(frame)
        event: str | None = None

        for prob in probabilities:
            if prob >= self.config.threshold:
                self._speech_ms += CHUNK_16K / self.sample_rate * 1000.0
                self._silence_ms = 0.0
                if not self._speaking and self._speech_ms >= self.config.min_speech_ms:
                    self._speaking = True
                    self._speech_start_frame = len(self._frames) - len(self._recent)
                    event = "speech_start"
            else:
                if self._speaking:
                    self._silence_ms += CHUNK_16K / self.sample_rate * 1000.0
                else:
                    # Decay so a couple of stray high frames cannot accumulate
                    # into a false speech start.
                    self._speech_ms = max(0.0, self._speech_ms - CHUNK_16K / self.sample_rate * 1000.0)

        if self._speaking and self._silence_ms >= self.config.silence_ms:
            return "utterance_end"

        total_ms = len(self._frames) * frame_ms
        if total_ms >= self.config.max_utterance_s * 1000:
            log.debug("Utterance hit the %.0fs cap", self.config.max_utterance_s)
            return "utterance_end"

        return event

    def _probabilities(self, frame: np.ndarray) -> list[float]:
        """Re-slice an arbitrary frame length into model-sized chunks."""
        self._pending = np.concatenate([self._pending, to_float32(frame)])
        out: list[float] = []
        if isinstance(self._model, SileroVadOnnx):
            size = CHUNK_16K
        else:
            size = 512 if self.sample_rate == 16000 else 256
        while len(self._pending) >= size:
            chunk, self._pending = self._pending[:size], self._pending[size:]
            out.append(float(self._model(chunk)))
        return out

    def audio(self) -> np.ndarray:
        """The captured utterance as int16, with pre-roll and without the
        trailing silence that triggered the endpoint."""
        if not self._frames:
            return np.zeros(0, dtype=np.int16)
        start = 0
        if self._speech_start_frame is not None:
            start = max(0, self._speech_start_frame - self._pre_roll)
        pcm = np.concatenate(self._frames[start:])
        # Trim the trailing silence too — Whisper hallucinates on long silence.
        keep_ms = 200
        trim = int(self._silence_ms - self.config.silence_ms + keep_ms)
        if trim > 0:
            cut = int(trim / 1000 * self.sample_rate)
            if cut < len(pcm):
                pcm = pcm[: len(pcm) - cut]
        return pcm

    @property
    def is_speaking(self) -> bool:
        return self._speaking


def _default_model_path() -> Path:
    from .config import MODELS_DIR

    return MODELS_DIR / "silero_vad.onnx"
