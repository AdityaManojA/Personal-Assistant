lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass



lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

lass FakeWakeWordDetector:
    """Fake wake word detector that simulates detection."""
    
    def __init__(self, model_name="hey_jarvis", threshold=0.5, cooldown_s=1.2, model_path=None):
        self.model_name = model_name
        self.threshold = threshold
        self.cooldown_s = cooldown_s
        self._last_fired = 0.0
        log.info("Using FAKE wake word detector for testing")
    
    def load(self):
        """Fake load - do nothing."""
        log.info("Fake wake word detector loaded")
    
    def score(self, frame):
        """Always return 0.0 (no detection)"""
        return 0.0
    
    def process(self, frame):
        """Simulate wake word detection every 30 seconds for testing."""
        import time
        now = time.monotonic()
        
        # Simulate wake word every 30 seconds
        if now - self._last_fired > 30.0:
            self._last_fired = now
            log.info("FAKE: Wake word detected! (simulated)")
            return True
        return False
    
    def reset(self):
        """Fake reset - do nothing."""
        pass

