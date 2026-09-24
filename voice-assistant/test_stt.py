#!/usr/bin/env python3
"""Test STT component with live microphone input"""

import sys
import time
import numpy as np
from pathlib import Path

# Add the voice-assistant directory to the path
sys.path.insert(0, str(Path(__file__).parent / "voice-assistant"))

from assistant.audio import Microphone
from assistant.stt import Transcriber
from assistant.config import load_config

def main():
    print("=== STT (Speech-to-Text) Test ===")
    print("Testing speech recognition with your microphone\n")
    
    # Load configuration
    config = load_config("voice-assistant/config.yaml")
    print(f"Configuration loaded:")
    print(f"  STT backend: {config.stt.backend}")
    print(f"  STT model: {config.stt.model}")
    print(f"  Sample rate: {config.audio.sample_rate}Hz")
    print()
    
    # Initialize audio input
    print("Initializing microphone...")
    try:
        mic = Microphone(
            sample_rate=config.audio.sample_rate,
            frame_samples=config.audio.frame_samples,
            device=config.audio.input_device,
        )
        print("Microphone initialized successfully")
    except Exception as e:
        print(f"Failed to initialize microphone: {e}")
        return 1
    
    # Initialize STT transcriber
    print("Initializing STT transcriber...")
    try:
        stt = Transcriber(
            config=config.stt,
            api_key=config.api_key,  # This might be None, but let's see
            sample_rate=config.audio.sample_rate,
        )
        print("STT transcriber initialized successfully")
    except Exception as e:
        print(f"Failed to initialize STT transcriber: {e}")
        return 1
    
    # Load the STT model
    print("Loading STT model (this may take a moment)...")
    try:
        stt.load()
        print("STT model loaded successfully")
    except Exception as e:
        print(f"Failed to load STT model: {e}")
        return 1
    
    print("\n=== Ready to test STT ===")
    print("Speak into your microphone - I'll transcribe what you say")
    print("Say 'stop test' to end the session")
    print()
    
    try:
        with mic:
            while True:
                # Collect audio for ~2 seconds
                print("Listening... (speak now)")
                audio_frames = []
                start_time = time.time()
                
                while time.time() - start_time < 2.0:  # Collect 2 seconds of audio
                    frame = mic.read()
                    if frame is not None:
                        audio_frames.append(frame)
                    time.sleep(0.001)
                
                if not audio_frames:
                    print("No audio captured, trying again...")
                    continue
                
                # Concatenate audio frames
                audio_data = np.concatenate(audio_frames, axis=0)
                
                # Convert to float32 for STT (if needed)
                if audio_data.dtype != np.float32:
                    # Assuming int16 audio from microphone
                    audio_float = audio_data.astype(np.float32) / 32768.0
                else:
                    audio_float = audio_data
                
                # Transcribe
                print("Transcribing...")
                try:
                    text = stt.transcribe(audio_float)
                    if text.strip():
                        print(f"You said: \"{text}\"")
                        
                        # Check for stop command
                        if "stop test" in text.lower():
                            print("Stop command detected. Ending test.")
                            break
                    else:
                        print("(No speech detected)")
                        
                except Exception as e:
                    print(f"Error during transcription: {e}")
                    
                print()  # Blank line for readability
                
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    except Exception as e:
        print(f"Error during test: {e}")
    finally:
        print("Cleaning up...")
        mic.stop()
    
    print("STT test completed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
