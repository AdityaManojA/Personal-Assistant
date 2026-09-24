"""Microphone capture and speaker playback.

Everything downstream wants 16 kHz mono int16, so the input stream is opened at
that rate and hands out fixed-size frames. The callback never blocks: if the
consumer falls behind we drop frames rather than stall PortAudio, because a
dropped frame is invisible and a stalled callback is a glitch.
"""

from __future__ import annotations

import queue
import threading
from typing import Iterator

import numpy as np
import sounddevice as sd

INT16_MAX = 32767.0


class Microphone:
    """Blocking frame reader over a sounddevice input stream."""

    def __init__(
        self,
        sample_rate: int = 16000,
        frame_samples: int = 1280,
        device: object = None,
        max_queued: int = 64,
    ) -> None:
        self.sample_rate = sample_rate
        self.frame_samples = frame_samples
        self.device = device
        self._queue: queue.Queue[np.ndarray] = queue.Queue(maxsize=max_queued)
        self._stream: sd.InputStream | None = None
        self.overflows = 0

    def _callback(self, indata, frames, time_info, status) -> None:  # noqa: ARG002
        if status and status.input_overflow:
            self.overflows += 1
        try:
            self._queue.put_nowait(indata[:, 0].copy())
        except queue.Full:
            pass

    def start(self) -> None:
        self._stream = sd.InputStream(
            samplerate=self.sample_rate,
            blocksize=self.frame_samples,
            channels=1,
            dtype="int16",
            device=self.device,
            callback=self._callback,
        )
        self._stream.start()

    def read(self, timeout: float | None = None) -> np.ndarray:
        return self._queue.get(timeout=timeout)

    def drain(self) -> None:
        """Throw away anything already buffered — used after barge-in."""
        while True:
            try:
                self._queue.get_nowait()
            except queue.Empty:
                return

    def stop(self) -> None:
        if self._stream is not None:
            self._stream.stop()
            self._stream.close()
            self._stream = None

    def __enter__(self) -> "Microphone":
        self.start()
        return self

    def __exit__(self, *exc) -> None:
        self.stop()


class Speaker:
    """Streaming PCM playback with an abort that takes effect immediately.

    ``abort`` is what makes barge-in feel right: when the user talks over the
    assistant we need the buffered audio gone now, not after it drains.
    """

    def __init__(self, device: object = None, volume: float = 1.0) -> None:
        self.device = device
        self.volume = volume
        self._stream: sd.OutputStream | None = None
        self._sample_rate: int | None = None
        self._lock = threading.Lock()
        self._aborted = threading.Event()

    def _ensure_open(self, sample_rate: int) -> None:
        if self._stream is not None and self._sample_rate == sample_rate:
            return
        self._close_locked()
        self._stream = sd.OutputStream(
            samplerate=sample_rate,
            channels=1,
            dtype="int16",
            device=self.device,
        )
        self._stream.start()
        self._sample_rate = sample_rate

    def play(self, pcm: np.ndarray, sample_rate: int) -> None:
        """Play an int16 buffer, blocking until done or aborted."""
        if pcm.size == 0:
            return
        with self._lock:
            if self._aborted.is_set():
                return
            self._ensure_open(sample_rate)
            stream = self._stream
        assert stream is not None

        if self.volume != 1.0:
            pcm = np.clip(pcm.astype(np.float32) * self.volume, -32768, 32767).astype(
                np.int16
            )

        # Write in chunks so an abort is noticed within a few milliseconds
        # instead of after the whole buffer.
        chunk = max(1, sample_rate // 50)  # 20 ms
        for start in range(0, pcm.size, chunk):
            if self._aborted.is_set():
                return
            stream.write(np.ascontiguousarray(pcm[start : start + chunk]))

    def abort(self) -> None:
        """Stop playback now and discard whatever is still queued."""
        self._aborted.set()
        with self._lock:
            if self._stream is not None:
                try:
                    self._stream.abort()
                except Exception:
                    pass
                self._stream = None
                self._sample_rate = None

    def resume(self) -> None:
        self._aborted.clear()

    def _close_locked(self) -> None:
        if self._stream is not None:
            try:
                self._stream.stop()
                self._stream.close()
            except Exception:
                pass
            self._stream = None
            self._sample_rate = None

    def close(self) -> None:
        with self._lock:
            self._close_locked()

    def __enter__(self) -> "Speaker":
        return self

    def __exit__(self, *exc) -> None:
        self.close()


def to_float32(pcm: np.ndarray) -> np.ndarray:
    """int16 -> float32 in [-1, 1], which is what the models expect."""
    return (pcm.astype(np.float32) / INT16_MAX).clip(-1.0, 1.0)


def to_int16(samples: np.ndarray) -> np.ndarray:
    """float32 in [-1, 1] -> int16."""
    return np.clip(samples * INT16_MAX, -32768, 32767).astype(np.int16)


def chunker(pcm: np.ndarray, size: int) -> Iterator[np.ndarray]:
    """Yield fixed-size slices, dropping any trailing partial chunk."""
    for start in range(0, len(pcm) - size + 1, size):
        yield pcm[start : start + size]


def tone(frequency: float, ms: int, sample_rate: int, amplitude: float = 0.25) -> np.ndarray:
    """Generate a short sine tone. Used for the activation chime so we ship no
    binary audio assets."""
    n = int(sample_rate * ms / 1000)
    t = np.arange(n, dtype=np.float32) / sample_rate
    wave = np.sin(2 * np.pi * frequency * t) * amplitude
    # 5 ms fade in/out to avoid a click at the edges.
    fade = max(1, int(sample_rate * 0.005))
    if n > 2 * fade:
        wave[:fade] *= np.linspace(0, 1, fade, dtype=np.float32)
        wave[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)
    return to_int16(wave)


def list_devices() -> str:
    """Human-readable device listing for `run.py --devices`."""
    lines = [f"PortAudio {sd.get_portaudio_version()[1]}", ""]
    for index, dev in enumerate(sd.query_devices()):
        default_in = " <-- default input" if index == sd.default.device[0] else ""
        default_out = " <-- default output" if index == sd.default.device[1] else ""
        lines.append(
            f"[{index:2d}] {dev['name']}  "
            f"in={dev['max_input_channels']} out={dev['max_output_channels']} "
            f"@{int(dev['default_samplerate'])}Hz{default_in}{default_out}"
        )
    return "\n".join(lines)
