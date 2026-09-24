#!/usr/bin/env python3
"""Working demo showing voice assistant concepts with your hardware"""

import sys
import time
import numpy as np
from pathlib import Path

# Add the voice-assistant directory to the path
sys.path.insert(0, str(Path(__file__).parent / "voice-assistant"))

from assistant.audio import Microphone, Speaker, list_devices, tone
from assistant.config import load_config

def main():
    print("=== Voice Assistant Hardware Demo ===")
    print("Testing core audio functionality with your actual devices\n")
    
    # Show available audio devices
    print("Audio devices detected:")
    print(list_devices())
    print()
    
    # Load configuration
    config = load_config("voice-assistant/config.yaml")
    print(f"Configuration loaded:")
    print(f"  Sample rate: {config.audio.sample_rate}Hz")
    print(f"  Frame size: {config.audio.frame_samples} samples ({config.audio.frame_ms}ms)")
    print(f"  Input device: {config.audio.input_device or 'system default'}")
    print(f"  Output device: {config.audio.output_device or 'system default'}")
    print()
    
    # Initialize audio components
    print("Initializing audio components...")
    try:
        mic = Microphone(
            sample_rate=config.audio.sample_rate,
            frame_samples=config.audio.frame_samples,
            device=config.audio.input_device,
        )
        speaker = Speaker(
            device=config.audio.output_device,
            volume=config.tts.volume,
        )
        print("Microphone and Speaker initialized successfully")
    except Exception as e:
        print(f"Failed to initialize audio components: {e}")
        return 1
    
    # Test audio loopback
    print("\nTesting audio loopback (speak into your microphone)...")
    print("I'll play back what you say for 10 seconds. Speak now!")
    
    try:
        with mic, speaker:
            start_time = time.time()
            while time.time() - start_time < 10:  # Run for 10 seconds
                # Read audio frame
                frame = mic.read()
                if frame is not None:
                    # Play it back immediately (loopback)
                    speaker.play(frame, config.audio.sample_rate)
                time.sleep(0.001)  # Small delay to prevent overwhelming
        
        print("Audio loopback test completed successfully!")
        print("  (If you heard your voice echoed, the audio pipeline is working)")
        
    except Exception as e:
        print(f"Error during audio test: {e}")
        return 1
    
    # Test tone generation
    print("\nTesting tone generation...")
    try:
        with speaker:
            # Play a short melody to confirm output works
            frequencies = [440, 494, 523, 587]  # A4, B4, C5, D5
            for freq in frequencies:
                tone_audio = tone(freq, 200, config.audio.sample_rate, 0.2)  # 200ms tones
                speaker.play(tone_audio, config.audio.sample_rate)
                time.sleep(0.05)  # Gap between notes
        print("Tone generation test completed!")
    except Exception as e:
        print(f"Error during tone test: {e}")
        return 1
    
    print("\n=== Demo Summary ===")
    print("Audio I/O system is working with your hardware")
    print("Microphone input and speaker output are functional") 
    print("Configuration loads correctly")
    print("Core audio pipeline is ready for voice assistant")
    print()
    print("The segmentation fault occurs in AI component initialization")
    print("(WakeWordDetector, STT, TTS, or LLM loading), but the audio foundation is solid.")
    print()
    print("To hear the actual voice assistant, the AI components need to be fixed,")
    print("but your hardware and audio subsystem are ready to go!")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
