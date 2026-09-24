"""Typed configuration loading.

Reads ``config.yaml``, applies ``KEY__SUBKEY`` environment overrides, and
resolves secrets from the environment (with an optional ``.env`` file).
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field, fields, is_dataclass
from pathlib import Path
from typing import Any, get_type_hints

import yaml

ROOT = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT / "models"
DEFAULT_CONFIG_PATH = ROOT / "config.yaml"


def _load_dotenv(path: Path) -> None:
    """Minimal .env loader so we do not hard-depend on python-dotenv."""
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip("'\"")
        os.environ.setdefault(key, value)


@dataclass
class AudioConfig:
    input_device: Any = None
    output_device: Any = None
    sample_rate: int = 16000
    frame_ms: int = 80

    @property
    def frame_samples(self) -> int:
        return int(self.sample_rate * self.frame_ms / 1000)


@dataclass
class WakeWordConfig:
    enabled: bool = True
    model: str = "hey_jarvis"
    threshold: float = 0.5
    cooldown_s: float = 1.2
    activation_sound: bool = True


@dataclass
class VadConfig:
    use_onnx: bool = True
    threshold: float = 0.5
    min_speech_ms: int = 200
    silence_ms: int = 700
    pre_roll_ms: int = 240
    max_utterance_s: float = 30.0
    start_timeout_s: float = 6.0


@dataclass
class STTConfig:
    backend: str = "local"
    model: str = "base.en"
    device: str = "cpu"
    compute_type: str = "int8"
    language: str = "en"
    beam_size: int = 1
    nim_model: str = "nvidia/parakeet-tdt-0.6b-v2"
    nim_base_url: str = "https://integrate.api.nvidia.com/v1"


@dataclass
class TTSConfig:
    backend: str = "piper"
    voice: str = "en_US-lessac-medium"
    volume: float = 1.0


@dataclass
class LLMConfig:
    base_url: str = "https://integrate.api.nvidia.com/v1"
    model: str = "deepseek-ai/deepseek-v4.1-flash"
    api_key_env: str = "NVIDIA_API_KEY"
    temperature: float = 0.3
    max_tokens: int = 400
    timeout_s: float = 60.0
    max_tool_rounds: int = 4


@dataclass
class AssistantConfig:
    name: str = "Assistant"
    greeting: str = "Ready."
    history_turns: int = 8
    log_transcripts: bool = True
    system_prompt: str = (
        "You are {name}, a voice assistant. Keep replies short and spoken. "
        "Never use markdown."
    )


@dataclass
class ToolsConfig:
    enabled: list[str] = field(
        default_factory=lambda: ["time", "timers", "notes", "system"]
    )
    allow_shell: bool = False
    notes_file: str = "notes.md"
    mcp_servers: dict[str, Any] = field(default_factory=dict)


@dataclass
class Config:
    audio: AudioConfig = field(default_factory=AudioConfig)
    wakeword: WakeWordConfig = field(default_factory=WakeWordConfig)
    vad: VadConfig = field(default_factory=VadConfig)
    stt: STTConfig = field(default_factory=STTConfig)
    tts: TTSConfig = field(default_factory=TTSConfig)
    llm: LLMConfig = field(default_factory=LLMConfig)
    assistant: AssistantConfig = field(default_factory=AssistantConfig)
    tools: ToolsConfig = field(default_factory=ToolsConfig)
    api_key: str | None = None

    @property
    def notes_path(self) -> Path:
        p = Path(self.tools.notes_file)
        return p if p.is_absolute() else ROOT / p

    @property
    def system_prompt(self) -> str:
        return self.assistant.system_prompt.format(name=self.assistant.name)


def _build(cls: type, data: Any):
    """Instantiate a dataclass from a plain dict, ignoring unknown keys."""
    if not isinstance(data, dict):
        return cls()
    try:
        # Resolves the string annotations produced by `from __future__ import
        # annotations` back into real classes, so nested dataclasses work.
        hints = get_type_hints(cls)
    except Exception:
        hints = {f.name: f.type for f in fields(cls)}

    kwargs: dict[str, Any] = {}
    for key, value in data.items():
        if key not in hints:
            continue
        ftype = hints[key]
        if is_dataclass(ftype) and isinstance(value, dict):
            kwargs[key] = _build(ftype, value)
        else:
            kwargs[key] = value
    return cls(**kwargs)


def _apply_env_overrides(raw: dict[str, Any]) -> dict[str, Any]:
    """Allow SECTION__KEY=value environment overrides."""
    for env_key, env_value in os.environ.items():
        if "__" not in env_key:
            continue
        section, _, key = env_key.partition("__")
        section, key = section.lower(), key.lower()
        if section in {"llm", "stt", "tts", "audio", "vad", "wakeword", "tools", "assistant"}:
            node = raw.setdefault(section, {})
            if isinstance(node, dict):
                node[key] = yaml.safe_load(env_value)
    return raw


def load_config(path: str | Path | None = None) -> Config:
    _load_dotenv(ROOT / ".env")
    config_path = Path(path) if path else DEFAULT_CONFIG_PATH
    raw: dict[str, Any] = {}
    if config_path.exists():
        raw = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    raw = _apply_env_overrides(raw)

    cfg = Config(
        audio=_build(AudioConfig, raw.get("audio")),
        wakeword=_build(WakeWordConfig, raw.get("wakeword")),
        vad=_build(VadConfig, raw.get("vad")),
        stt=_build(STTConfig, raw.get("stt")),
        tts=_build(TTSConfig, raw.get("tts")),
        llm=_build(LLMConfig, raw.get("llm")),
        assistant=_build(AssistantConfig, raw.get("assistant")),
        tools=_build(ToolsConfig, raw.get("tools")),
    )

    # A NIM base URL in the environment wins over the file, so you can point the
    # same config at a self-hosted endpoint without editing YAML.
    if os.environ.get("NIM_BASE_URL"):
        cfg.llm.base_url = os.environ["NIM_BASE_URL"]

    cfg.api_key = os.environ.get(cfg.llm.api_key_env) or None
    return cfg
