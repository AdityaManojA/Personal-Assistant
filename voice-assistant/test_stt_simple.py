#!/usr/bin/env python3
"""Simple STT test - just instantiate Transcriber"""

import sys
from pathlib import Path

# Add the voice-assistant directory to the path
sys.path.insert(0, str(Path(__file__).parent / "voice-assistant"))

from assistant.stt import Transcriber
from assistant.config import load_config

def main():
    print("=== Simple STT Test (no model loading) ===")
    
    # Load configuration
    config = load_config("voice-assistant/config.yaml")
    print(f"Configuration loaded:")
    print(f"  STT backend: {config.stt.backend}")
    print(f"  STT model: {config.stt.model}")
    
    # Initialize STT transcriber (without loading model)
    print("Initializing STT transcriber (no model loading)...")
    try:
        stt = Transcriber(
            config=config.stt,
            api_key=config.api_key,
            sample_rate=config.audio.sample_rate,
        )
        print("✓ STT transcriber instantiated successfully")
        print("  (Model not loaded yet - this is where segfault might occur)")
        return 0
    except Exception as e:
        print(f"✗ Failed to instantiate STT transcriber: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
