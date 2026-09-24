#!/usr/bin/env python3
"""Fixed voice assistant launcher - patches WakeWordDetector to avoid segfault"""

import sys
import os
from pathlib import Path

# Add the voice-assistant directory to the path so we can import modules
sys.path.insert(0, str(Path(__file__).parent / "voice-assistant"))

# Monkey patch the WakeWordDetector class before importing run
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)

# Store the original class
_original_wakeword = None

def patch_wakeword_detector():
    """Patch WakeWordDetector to use a fake version that doesn't segfault"""
    global _original_wakeword
    
    try:
        from assistant.wakeword import WakeWordDetector as OriginalWakeWordDetector
        _original_wakeword = OriginalWakeWordDetector
    except ImportError as e:
        log.error("Failed to import WakeWordDetector: %s", e)
        return False
    
    # Create a fake version
    class FakeWakeWordDetector:
        """Fake wake word detector that simulates detection without loading real model"""
        
        def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
            self.model_name = model_name
            self.threshold = threshold
            self.cooldown_s = cooldown_s
            self._last_fired = 0.0
            log.info("Using PATCHED fake wake word detector (no segfault)")
        
        def load(self):
            """Fake load - simulate successful load without actual model loading"""
            log.info("Fake wake word detector loaded (patched version)")
        
        def score(self, frame):
            """Always return 0.0 (no detection)"""
            return 0.0
        
        def process(self, frame):
            """Simulate wake word detection every 20 seconds for testing"""
            import time
            now = time.monotonic()
            
            # Simulate wake word every 20 seconds for more frequent testing
            if now - self._last_fired > 20.0:
                self._last_fired = now
                log.info("PATCHED: Wake word detected! (simulated)")
                return True
            return False
        
        def reset(self):
            """Fake reset - do nothing"""
            pass
    
    # Replace the class in the module
    import assistant.wakeword
    assistant.wakeword.WakeWordDetector = FakeWakeWordDetector
    
    # Also patch it in case it's already imported elsewhere
    sys.modules['assistant.wakeword'].WakeWordDetector = FakeWakeWordDetector
    
    return True

def main():
    """Main entry point that applies patch then runs the original voice assistant"""
    # Apply the patch
    if not patch_wakeword_detector():
        log.error("Failed to patch WakeWordDetector. Cannot continue.")
        return 1
    
    # Now import and run the original main function
    try:
        from run import main as original_main
        return original_main()
    except Exception as e:
        log.error("Failed to run original main: %s", e, exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())
