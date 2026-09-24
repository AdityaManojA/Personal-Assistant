#!/usr/bin/env python3
"""Working voice assistant demo - real audio, mocked AI for testing"""

import sys
import time
import numpy as np
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "voice-assistant"))

from assistant.audio import Microphone, Speaker, list_devices, tone, to_float32
from assistant.config import load_config
from assistant.vad import Endpointer

# Mock AI components (bypass loading issues)
class MockWakeWordDetector:
    def __init__(self, *args, **kwargs):
        self._last_fired = 0.0
        print("🎤 Using MOCK wake word detector (says 'hey alfred' every 15s)")
    
    def load(self): 
        print("✅ Mock wake word detector loaded")
    def process(self, frame):
        now = time.monotonic()
        if now - self._last_fired > 15.0:  # Every 15 seconds for demo
            self._last_fired = now
            print("🔔 MOCK: Wake word detected! (simulated 'hey alfred')")
            return True
        return False
    def reset(self): pass

class MockTranscriber:
    def __init__(self, *args, **kwargs):
        print("🎤 Using MOCK STT (returns predefined phrases)")
    def load(self): print("✅ Mock STT loaded")
    def transcribe(self, audio):
        import random
        phrases = [
            "hey alfred what time is it",
            "hey alfred tell me a joke", 
            "hey alfred what's the weather",
            "hey alfred stop"
        ]
        return random.choice(phrases)

class MockPiperEngine:
    def __init__(self, *args, **kwargs):
        print("🔊 Using MOCK TTS engine")
    def load(self): print("✅ Mock TTS engine loaded")

class MockTTSVoice:
    def __init__(self, config, speaker):
        self.config = config
        self.speaker = speaker
        print("🔊 Using MOCK TTS voice")
    def load(self): print("✅ Mock TTS voice loaded")
    defrosted")
    def say(self, text):
        print(f"🗣️  ASSISTANT WOULD SAY: {text}")
        time.sleep(len(text) * 0.03)  # Simulate speech time
    def wait(self): pass
    def start(self): pass
    def stop(self): pass

class MockLLMClient:
    def __init__(self, *args, **kwargs):
        print("🧠 Using MOCK LLM (returns predefined responses)")
    class chat:
        class completions:
            @staticmethod
            def create(*args, **kwargs):
                class FakeChoice:
                    class message:
                        content = "I'm Alfred, your voice assistant! All systems are operational."
                class FakeCompletion:
                    choices = [FakeChoice()]
                return FakeCompletion()

def main():
    print("🎤 ALFRED VOICE ASSISTANT - WORKING DEMO")
    print("=" * 50)
    
    config = load_config("voice-assistant/config.yaml")
    
    # Initialize REAL audio components
    print("🎧 Initializing REAL audio hardware...")
    mic = Microphone(
        sample_rate=config.audio.sample_rate,
        frame_samples=config.audio.frame_samples,
        device=config.audio.input_device,
    )
    speaker = Speaker(
        device=config.audio.output_device,
        volume=config.tts.volume,
    )
    print("✅ REAL Microphone and Speaker initialized")
    
    # Initialize MOCK AI components
    wakeword = MockWakeWordDetector(
        model_name=config.wakeword.model,
        threshold=config.wakeword.threshold,
        cooldown_s=config.wakeword.cooldown_s,
    )
    wakeword.load()
    
    vad = Endpointer(
        config=config.vad,
        sample_rate=config.audio.sample_rate,
        frame_samples=config.audio.frame_samples,
    )
    
    stt = MockTranscriber(
        config=config.stt,
        api_key=config.api_key,
        sample_rate=config.audio.sample_rate,
    )
    stt.load()
    
    tts_engine = MockPiperEngine(voice=config.tts.voice)
    tts = MockTTSVoice(config=config.tts, speaker=speaker)
    tts.load()
    
    llm_client = MockLLMClient(
        base_url=config.llm.base_url,
        api_key=config.api_key,
    )
    
    print("\n🎯 ALL SYSTEMS READY!")
    print("💬 Say 'hey alfred' (or wait 15 seconds for auto-trigger)")
    print("💬 Try: 'what time is it', 'tell me a joke', 'what's the weather'")
    print("💬 Say 'hey alfred stop' to end demo")
    print("=" * 50)
    
    try:
        with mic, speaker:
            while True:
                frame = mic.read()
                if wakeword.process(frame):
                    print("\n🔔 WAKE WORD DETECTED!")
                    if config.wakeword.activation_sound:
                        chime = tone(800, 150, config.audio.sample_rate, 0.2)
                        speaker.play(chime, config.audio.sample_rate)
                        time.sleep(0.3)
                    
                    print("🎧 Listening for command...")
                    vad.begin()
                    audio_frames = []
                    speech_started = False
                    
                    while True:
                        frame = mic.read(timeout=2.0)
                        if frame is None:
                            continue
                        result = vad.feed(frame)
                        
                        if result == "speech_start":
                            speech_started = True
                            audio_frames.append(frame)
                        elif result == "utterance_end" and speech_started:
                            audio_frames.append(frame)
                            break
                        elif result == "timeout":
                            print("⏰ Listening timeout")
                            break
                        elif speech_started:
                            audio_frames.append(frame)
                    
                    if not audio_frames:
                        print("🤫 No speech detected")
                        continue
                    
                    audio_data = np.concatenate(audio_frames)
                    audio_float = to_float32(audio_data)
                    
                    print("🔄 Transcribing...")
                    text = stt.transcribe(audio_float)
                    print(f"🎯 YOU SAID: '{text}'")
                    
                    if "stop" in text.lower():
                        print("👋 Stop command received. Goodbye!")
                        break
                    
                    print("🧠 Processing with AI...")
                    response = "I'm Alfred, your voice assistant! All systems are working perfectly."
                    if "time" in text.lower():
                        response = f"The current time is {time.strftime('%I:%M %p')}"
                    elif "joke" in text.lower():
                        response = "Why don't scientists trust atoms anymore? Because they make up everything!"
                    elif "weather" in text.lower():
                        response = "I can't check real weather yet, but I hope it's nice where you are!"
                    elif "your name" in text.lower():
                        response = "I'm Alfred, named after Batman's loyal butler - ready to serve you!"
                    
                    print(f"🤖 ALFRED RESPONDS: {response}")
                    print("🔊 Speaking response...")
                    tts.say(response)
                    tts.wait()
                    
    except KeyboardInterrupt:
        print("\n👋 Shutting down Alfred. Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        tts.stop()
        tts.wait()
        mic.stop()
        speaker.close()
        wakeword.reset()
        vad.begin()

if __name__ == "__main__":
    main()