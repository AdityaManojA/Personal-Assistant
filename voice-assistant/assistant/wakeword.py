"""Wake word detection via openWakeWord.

Runs a small ONNX model over every incoming frame. This is the only component
that is always running, so it stays deliberately cheap — a few hundred
microseconds per 80 ms frame on a single CPU core.
"""

from __future__ import annotations

import logging
import time
from pathlib import Path

import numpy as np

log = logging.getLogger(__name__)

BUNDLED_MODELS = ("alexa", "hey_jarvis", "hey_mycroft", "hey_rhasspy", "timer", "weather")


class WakeWordDetector:
    """Scores fixed-size frames and reports when the phrase fires.

    ``process`` returns True at most once per cooldown window, so the caller can
    treat it as a simple boolean trigger and not worry about the model firing
    three frames in a row.
    """

    def __init__(
        self,
        model_name: str = "hey_jarvis",
        threshold: float = 0.5,
        cooldown_s: float = 1.2,
        model_path: str | Path | None = None,
    ) -> None:
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        self._model = None
        self._key = model_name
        self._model_path = Path(model_path) if model_path else None

    def load(self) -> None:
        from openwakeword.model import Model
        from openwakeword.utils import download_models

        if self._model_path is not None:
            if not self._model_path.exists():
                raise FileNotFoundError(f"Wake word model not found: {self._model_path}")
            models = [str(self._model_path)]
            self._key = self._model_path.stem
        else:
            # No-op when the model is already cached in ~/.cache/openwakeword.
            if self.model_name in BUNDLED_MODELS:
                download_models(model_names=[self.model_name])
            models = [self.model_name]

        # ONNX rather than tflite: onnxruntime is already a dependency and this
        # avoids pulling in a second inference stack.
        self._model = Model(wakeword_models=models, inference_framework="onnx")
        log.info("Wake word ready: %s (threshold %.2f)", self._key, self.threshold)

    def score(self, frame: np.ndarray) -> float:
        if self._model is None:
            raise RuntimeError("WakeWordDetector.load() must be called first")
        scores = self._model.predict(frame)
        return float(scores.get(self._key, 0.0))

    def process(self, frame: np.ndarray) -> bool:
        """Feed one frame; True if the wake word just fired."""
        score = self.score(frame)
        now = time.monotonic()
        if score >= self.threshold and (now - self._last_fired) >= self.cooldown_s:
            self._last_fired = now
            log.debug("Wake word fired: score=%.3f", score)
            return True
        return False

    def reset(self) -> None:
        """Clear the model's internal audio buffer (call after a barge-in)."""
        if self._model is not None:
            try:
                self._model.reset()
            except Exception:
                pass
