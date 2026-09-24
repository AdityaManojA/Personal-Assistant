"""Speech to text.

Default is faster-whisper running locally on CPU with int8 quantization: free,
private, and around 300 ms for a typical spoken request. The NIM backend is
there for when you want higher accuracy or are on a weak machine.
"""

from __future__ import annotations

import io
import logging
import time
import wave

import numpy as np

log = logging.getLogger(__name__)


def _wav_bytes(pcm: np.ndarray, sample_rate: int) -> bytes:
    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as handle:
        handle.setnchannels(1)
        handle.setsampwidth(2)
        handle.setframerate(sample_rate)
        handle.writeframes(pcm.tobytes())
    return buffer.getvalue()


class Transcriber:
    def __init__(self, config, api_key: str | None = None, sample_rate: int = 16000):
        self.config = config
        self.sample_rate = sample_rate
        self.backend = config.backend.lower()
        self._model = None
        self._client = None
        if self.backend == "nim":
            from openai import OpenAI

            key = api_key or _env_key("NIM_STT_API_KEY")
            if not key:
                raise RuntimeError(
                    "stt.backend is 'nim' but no API key was found. "
                    "Set NIM_STT_API_KEY (or NVIDIA_API_KEY) in your .env file."
                )
            self._client = OpenAI(base_url=config.nim_base_url, api_key=key)

    def load(self) -> None:
        if self.backend != "local":
            return
        from faster_whisper import WhisperModel

        started = time.perf_counter()
        self._model = WhisperModel(
            self.config.model,
            device=self.config.device,
            compute_type=self.config.compute_type,
            num_workers=1,
        )
        log.info(
            "Whisper %s loaded in %.1fs (%s/%s)",
            self.config.model,
            time.perf_counter() - started,
            self.config.device,
            self.config.compute_type,
        )
        self.warmup()

    def warmup(self) -> None:
        """Run a fraction of a second of silence through the model so the first
        real request does not pay the graph-initialization cost."""
        if self._model is None:
            return
        silence = np.zeros(self.sample_rate // 2, dtype=np.int16)
        self.transcribe(silence)

    def transcribe(self, pcm: np.ndarray) -> str:
        if pcm.size == 0:
            return ""
        started = time.perf_counter()
        if self.backend == "nim":
            text = self._transcribe_nim(pcm)
        else:
            text = self._transcribe_local(pcm)
        log.debug("STT %.0f ms: %r", (time.perf_counter() - started) * 1000, text)
        return text

    def _transcribe_local(self, pcm: np.ndarray) -> str:
        if self._model is None:
            raise RuntimeError("Transcriber.load() must be called first")
        audio = pcm.astype(np.float32) / 32768.0
        segments, _ = self._model.transcribe(
            audio,
            language=self.config.language,
            beam_size=self.config.beam_size,
            # We already endpointed with Silero, so a second VAD pass would
            # only add latency and clip the same edges twice.
            vad_filter=False,
            condition_on_previous_text=False,
        )
        return " ".join(segment.text.strip() for segment in segments).strip()

    def _transcribe_nim(self, pcm: np.ndarray) -> str:
        if self._client is None:
            raise RuntimeError("NIM transcriber is not configured (missing API key)")
        result = self._client.audio.transcriptions.create(
            model=self.config.nim_model,
            file=("audio.wav", _wav_bytes(pcm, self.sample_rate)),
        )
        return getattr(result, "text", "").strip()


def _env_key(name: str) -> str | None:
    import os

    return os.environ.get(name)
