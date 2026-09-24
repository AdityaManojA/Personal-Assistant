#!/usr/bin/env python3
"""Working voice assistant launcher - patches WakeWordDetector.load to avoid segfault"""

import sys
import os
from pathlib import Path

# Add the voice-assistant directory to the path
sys.path.insert(0, str(Path(__file__).parent / "voice-assistant"))

import logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

def patch_wakeword_load():
    """Patch WakeWordDetector.load method to do nothing"""
    try:
        from assistant.wakeword import WakeWordDetector
        # Store original method
        original_load = WakeWordDetector.load
        # Replace with dummy method
        def dummy_load(self):
            log.info("WakeWordDetector.load() patched - doing nothing to avoid segfault")
        WakeWordDetector.load = dummy_load
        log.info("Successfully patched WakeWordDetector.load")
        return True
    except Exception as e:
        log.error("Failed to patch WakeWordDetector.load: %s", e)
        return False

def main():
    # Apply the patch
    if not patch_wakeword_load():
        log.error("Failed to patch WakeWordDetector. Cannot continue.")
        return 1
    
    # Import and run the original main
    try:
        from run import main as original_main
        log.info("Starting voice assistant with patched WakeWordDetector...")
        return original_main()
    except Exception as e:
        log.error("Failed to run voice assistant: %s", e, exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())
