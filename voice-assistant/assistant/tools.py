"""Tools for the voice assistant.

Implements time, timers, notes, and system tools that can be called by the LLM.
"""

from __future__ import annotations

import json
import os
import time
import uuid
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List

import logging

log = logging.getLogger(__name__)


class Tools:
    """Collection of tools available to the voice assistant."""

    def __init__(self, config):
        self.config = config
        self.notes_path = config.tools.notes_path
        self._timers: Dict[str, Dict[str, Any]] = {}  # timer_id -> {label, end_time}

        # Ensure notes file exists
        self.notes_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.notes_path.exists():
            self.notes_path.write_text("# Notes\n\n", encoding="utf-8")

    def get_time(self, _: str = "") -> str:
        """Get the current time.

        Args:
            _: Unused parameter (for tool interface consistency)

        Returns:
            Current time formatted as a string
        """
        now = datetime.now()
        return now.strftime("%I:%M %p on %A, %B %d, %Y")

    def set_timer(self, params: str) -> str:
        """Set a timer.

        Args:
            params: JSON string with "seconds" (int) and optional "label" (str)

        Returns:
            Confirmation message
        """
        try:
            data = json.loads(params) if params.strip() else {}
            seconds = int(data.get("seconds", 0))
            label = data.get("label", f"Timer {len(self._timers) + 1}")

            if seconds <= 0:
                return "Please specify a positive number of seconds for the timer."

            if seconds > 86400 * 7:  # 7 days max
                return "Timer cannot be set for more than 7 days."

            timer_id = str(uuid.uuid4())
            end_time = time.time() + seconds

            self._timers[timer_id] = {
                "id": timer_id,
                "label": label,
                "seconds": seconds,
                "end_time": end_time,
                "created": time.time()
            }

            # Clean up old timers
            self._cleanup_timers()

            mins, secs = divmod(seconds, 60)
            hours, mins = divmod(mins, 60)
            time_parts = []
            if hours:
                time_parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
            if mins:
                time_parts.append(f"{mins} minute{'s' if mins != 1 else ''}")
            if secs and not hours:  # Only show seconds if less than an hour
                time_parts.append(f"{secs} second{'s' if secs != 1 else ''}")

            time_str = ", ".join(time_parts) if time_parts else "0 seconds"
            return f"Timer set for {time_str}: {label}"

        except (json.JSONDecodeError, ValueError, KeyError) as e:
            log.error("Error setting timer: %s", e)
            return "Invalid timer parameters. Please provide JSON with 'seconds' field."

    def list_timers(self, _: str = "") -> str:
        """List active timers.

        Args:
            _: Unused parameter (for tool interface consistency)

        Returns:
            Formatted list of active timers
        """
        self._cleanup_timers()

        if not self._timers:
            return "No active timers."

        now = time.time()
        timer_list = []
        for timer in self._timers.values():
            remaining = max(0, timer["end_time"] - now)
            if remaining > 0:
                mins, secs = divmod(int(remaining), 60)
                hours, mins = divmod(mins, 60)
                time_parts = []
                if hours:
                    time_parts.append(f"{hours}h")
                if mins:
                    time_parts.append(f"{mins}m")
                if secs or not hours:  # Show seconds if less than an hour
                    time_parts.append(f"{secs}s")
                time_str = " ".join(time_parts)
                timer_list.append(f"- {timer['label']}: {time_str} remaining")

        if not timer_list:
            return "No active timers."

        return "Active timers:\n" + "\n".join(timer_list)

    def cancel_timer(self, params: str = "") -> str:
        """Cancel a timer.

        Args:
            params: JSON string with "timer_id" or "label" to cancel

        Returns:
            Confirmation message
        """
        try:
            data = json.loads(params) if params.strip() else {}
            timer_id = data.get("timer_id")
            label = data.get("label")

            cancelled = False

            if timer_id:
                if timer_id in self._timers:
                    del self._timers[timer_id]
                    cancelled = True
            elif label:
                # Find timer by label (case insensitive)
                to_delete = []
                for tid, timer in self._timers.items():
                    if timer["label"].lower() == label.lower():
                        to_delete.append(tid)
                for tid in to_delete:
                    del self._timers[tid]
                    cancelled = True
            else:
                return "Please specify either 'timer_id' or 'label' to cancel."

            if cancelled:
                self._cleanup_timers()
                return "Timer cancelled."
            else:
                return "Timer not found."

        except json.JSONDecodeError as e:
            log.error("Error cancelling timer: %s", e)
            return "Invalid parameters. Please provide JSON with 'timer_id' or 'label' field."

    def take_note(self, params: str) -> str:
        """Take a note.

        Args:
            params: JSON string with "text" (str) to save as a note

        Returns:
            Confirmation message
        """
        try:
            data = json.loads(params) if params.strip() else {}
            text = data.get("text", "").strip()

            if not text:
                return "Please provide text for the note."

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note_entry = f"- [{timestamp}] {text}\n"

            with open(self.notes_path, "a", encoding="utf-8") as f:
                f.write(note_entry)

            log.info("Note saved: %s", text[:50] + ("..." if len(text) > 50 else ""))
            return f"Note saved: {text}"

        except json.JSONDecodeError as e:
            log.error("Error taking note: %s", e)
            return "Invalid parameters. Please provide JSON with 'text' field."

    def list_notes(self, params: str = "") -> str:
        """List recent notes.

        Args:
            params: JSON string with optional "limit" (int, default 10)

        Returns:
            Formatted list of recent notes
        """
        try:
            data = json.loads(params) if params.strip() else {}
            limit = int(data.get("limit", 10))
        except (json.JSONDecodeError, ValueError):
            limit = 10

        if not self.notes_path.exists():
            return "No notes found."

        content = self.notes_path.read_text(encoding="utf-8")
        lines = [line.strip() for line in content.split('\n') if line.strip()]

        # Filter to just note lines (those starting with - [)
        note_lines = [line for line in lines if line.startswith('- [')]

        if not note_lines:
            return "No notes found."

        # Get the most recent notes
        recent_notes = note_lines[-limit:] if len(note_lines) > limit else note_lines
        recent_notes.reverse()  # Most recent first

        if len(recent_notes) > limit:
            return f"Showing {limit} most recent notes:\n" + "\n".join(recent_notes)
        else:
            return "All notes:\n" + "\n".join(recent_notes)

    def system_info(self, _: str = "") -> str:
        """Get system information.

        Args:
            _: Unused parameter (for tool interface consistency)

        Returns:
            System information string
        """
        import platform
        import sys

        info = []
        info.append(f"Platform: {platform.system()} {platform.release()} ({platform.machine()})")
        info.append(f"Python: {sys.version.split()[0]}")
        info.append(f"Assistant: {self.config.assistant.name}")

        # Add uptime if we had it
        info.append(f"Status: Ready")

        return " | ".join(info)

    def _cleanup_timers(self):
        """Remove expired timers."""
        now = time.time()
        expired = [tid for tid, timer in self._timers.items() if timer["end_time"] < now]
        for tid in expired:
            del self._timers[tid]
            log.debug("Removed expired timer: %s", tid)


# Tool registry for easy access
TOOL_REGISTRY = {
    "time": Tools.get_time,
    "timers": lambda self, params: (  # Handle both set and list based on params
        self.set_timer(params) if params and '"seconds"' in params
        else self.list_timers(params)
    ),
    "notes": lambda self, params: (  # Handle both take and list based on params
        self.take_note(params) if params and '"text"' in params
        else self.list_notes(params)
    ),
    "system": Tools.system_info,
}