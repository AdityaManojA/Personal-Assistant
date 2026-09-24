"""Text helpers for spoken output."""

from __future__ import annotations

import re

_SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
# Strips markdown the model emits despite instructions. Speaking "asterisk
# asterisk" out loud is the single most jarring failure mode of a voice agent.
_MARKDOWN = [
    (re.compile(r"```.*?```", re.DOTALL), " "),
    (re.compile(r"`([^`]*)`"), r"\1"),
    (re.compile(r"\*\*([^*]+)\*\*"), r"\1"),
    (re.compile(r"\*([^*]+)\*"), r"\1"),
    (re.compile(r"^\s*[-*+]\s+", re.MULTILINE), ""),
    (re.compile(r"^\s*#{1,6}\s+", re.MULTILINE), ""),
    (re.compile(r"\[([^\]]+)\]\([^)]+\)"), r"\1"),
]


def clean_for_speech(text: str) -> str:
    for pattern, replacement in _MARKDOWN:
        text = pattern.sub(replacement, text)
    return re.sub(r"\s+", " ", text).strip()


class SentenceBuffer:
    """Accumulates streamed tokens and emits whole sentences.

    Speaking on sentence boundaries is what makes a streaming voice assistant
    feel responsive — you start talking after ~20 tokens instead of waiting for
    the full reply. ``min_chars`` prevents emitting fragments like "Sure." on
    their own, which produces choppy, stuttering output.
    """

    def __init__(self, min_chars: int = 24) -> None:
        self.min_chars = min_chars
        self._buffer = ""

    def push(self, token: str) -> list[str]:
        self._buffer += token
        parts = _SENTENCE_END.split(self._buffer)
        if len(parts) == 1:
            return []
        # Everything except the trailing fragment is a complete sentence.
        complete, self._buffer = parts[:-1], parts[-1]
        ready: list[str] = []
        pending = ""
        for sentence in complete:
            pending = f"{pending} {sentence}".strip()
            if len(pending) >= self.min_chars:
                ready.append(pending)
                pending = ""
        if pending:
            self._buffer = f"{pending} {self._buffer}".strip()
        return [clean_for_speech(s) for s in ready if s.strip()]

    def flush(self) -> list[str]:
        remainder, self._buffer = self._buffer.strip(), ""
        cleaned = clean_for_speech(remainder)
        return [cleaned] if cleaned else []
