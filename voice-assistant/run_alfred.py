#!/usr/bin/env python3
"""Test wake word detector initialization"""

import sys
import logging
from pathlib import Path

from assistant.config import load_config
from assistant.wakeword import WakeWordDetector

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

def main() -> int:
    # Load configuration
    config = load_config(Path("voice-assistant/config.yaml"))
    log.info("Configuration loaded")

    # Try to create WakeWordDetector
    try:
        log.info("Creating WakeWordDetector...")
        wakeword = WakeWordDetector(
            model_name=config.wakeword.model,
            threshold=config.wakeword.threshold,
            cooldown_s=config.wakeword.cooldown_s,
        )
        log.info("WakeWordDetector created successfully")
        
        # Try to load it
        log.info("Loading WakeWordDetector...")
        wakeword.load()
        log.info("WakeWordDetector loaded successfully")
        
    except Exception as e:
        log.error("Failed with WakeWordDetector: %s", e, exc_info=True)
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
