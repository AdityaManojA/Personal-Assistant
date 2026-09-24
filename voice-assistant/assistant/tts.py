"""Text to speech, with a worker thread so synthesis never blocks the LLM stream.

The important detail here is overlap. While Piper is synthesizing sentence one,
the LLM is still generating sentence two, and the speaker is still playing
sentence zero. That pipelining is what gets time-to-first-audio under a second.
"""

from __future__ import annotations

import logging
import queue
import threading
import time
from pathlib import Path

import numpy as np

from .audio import Speaker
from .config import MODELS_DIR

log = logging.getLogger(__name__)

VOICES_DIR = MODELS_DIR / "voices"
_STOP = object()


class PiperEngine:
    """Local neural TTS. Roughly 0.1x realtime on a modern CPU core."""

    def __init__(self, voice: str = "en_US-lessac-medium") -> None:
        self.voice_name = voice
        self.voice = None
        self.sample_rate = 22050

    def load(self) -> None:
        try:
            from piper import PiperVoice  # piper-tts >= 1.2
        except ImportError:  # pragma: no cover - older layout
            from piper.voice import PiperVoice

        model_path = VOICES_DIR / f"{self.voice_name}.onnx"
        config_path = VOICES_DIR / f"{self.voice_name}.onnx.json"
        if not model_path.exists():
            raise FileNotFoundError(
                f"Piper voice not found: {model_path}\n"
                "Run: python scripts/download_models.py"
            )
        self.voice = PiperVoice.load(
            str(model_path),
            config_path=str(config_path) if config_path.exists() else None,
        )
        self.sample_rate = int(getattr(self.voice.config, "sample_rate", 22050))
        log.info("Piper voice ready: %s @ %d Hz", self.voice_name, self.sample_rate)

    def synthesize(self, text: str) -> np.ndarray:
        """Return int16 PCM for the given text."""
        if self.voice is None:
            raise RuntimeError("PiperEngine.load() must be called first")

        if hasattr(self.voice, "synthesize_stream_raw"):
            chunks = [
                np.frombuffer(chunk, dtype=np.int16)
                for chunk in self.voice.synthesize_stream_raw(text)
            ]
            return np.concatenate(chunks) if chunks else np.zeros(0, dtype=np.int16)

        # Fallback for piper builds without the streaming API.
        import io
        import wave

        buffer = io.BytesIO()
        with wave.open(buffer, "wb") as handle:
            self.voice.synthesize(text, handle)
        buffer.seek(0)
        with wave.open(buffer, "rb") as handle:
            self.sample_rate = handle.getframerate()
            return np.frombuffer(handle.readframes(handle.getnframes()), dtype=np.int16)


class NullEngine:
    """Used when tts.backend is 'none' — prints instead of speaking."""

    sample_rate = 22050

    def load(self) -> None:
        return

    def synthesize(self, text: str) -> np.ndarray:
        print(f"  \033[36m{text}\033[0m", flush=True)
        return np.zeros(0, dtype=np.int16)


class Voice:
    """Serializes synthesis and playback on a background worker.

    Callers push sentences as they stream out of the model and then ``wait()``
    for the queue to drain. ``stop()`` is the barge-in path: it clears anything
    pending and aborts playback mid-word.
    """

    def __init__(self, config, speaker: Speaker) -> None:
        self.config = config
        self.speaker = speaker
        self.backend = config.backend.lower()
        self.engine = NullEngine() if self.backend == "none" else PiperEngine(config.voice)
        self._queue: queue.Queue = queue.Queue()
        self._thread: threading.Thread | None = None
        self._running = False
        self._speaking = threading.Event()
        self.spoken: list[str] = []

    def load(self) -> None:
        self.engine.load()

    def start(self) -> None:
        self._running = True
        self._thread = threading.Thread(target=self._worker, daemon=True, name="tts")
        self._thread.start()

    def say(self, text: str) -> None:
        """Queue a sentence for speaking."""
        if text and text.strip():
            self._queue.put(text.strip())

    def _worker(self) -> None:
        while self._running:
            item = self._queue.get()
            if item is _STOP:
                self._queue.task_done()
                break
            try:
                self._speaking.set()
                started = time.perf_counter()
                pcm = self.engine.synthesize(item)
                synth_ms = (time.perf_counter() - started) * 1000
                if pcm.size:
                    self.speaker.play(pcm, self.engine.sample_rate)
                self.spoken.append(item)
                log.debug("TTS %.0f ms for %d chars", synth_ms, len(item))
            except Exception:
                log.exception("Speech synthesis failed")
            finally:
                self._speaking.clear()
                self._queue.task_done()

    def wait(self) -> None:
        """Block until everything queued has been spoken."""
        self._queue.join()

    @property
    def is_speaking(self) -> bool:
        return self._speaking.is_set() or not self._queue.empty()

    def stop(self) -> None:
        """Barge-in: drop queued sentences and cut playback immediately."""
        try:
            while True:
                self._queue.get_nowait()
                self._queue.task_done()
        except queue.Empty:
            pass
        self.speaker.abort()
        self.speaker.resume()

    def close(self) -> None:
        self._running = False
        self._queue.put(_STOP)
        if self._thread is not None:
            self._thread.join(timeout=2.0)


def play_chime(speaker: Speaker, sample_rate: int = 22050) -> None:
    """Two quick ascending tones so the user knows the wake word landed."""
    from .audio import tone

    speaker.play(tone(880, 70, sample_rate, amplitude=0.18), sample_rate)
    speaker.play(tone(1320, 90, sample_rate, amplitude=0.18), sample_rate)
