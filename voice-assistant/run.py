#!/usr/bin/env python3
"""Main entry point for the voice assistant.

Pipeline: microphone -> wake word -> VAD endpointing -> Whisper -> NIM -> Piper
"""

from __future__ import annotations

import argparse
import logging
import os
import signal
import sys
import time
from pathlib import Path

import numpy as np

# Local imports
from assistant.audio import Microphone, Speaker, list_devices, tone, to_float32
from assistant.config import load_config
from assistant.stt import Transcriber
from assistant.tts import Voice as TTSVoice, PiperEngine
from assistant.text import SentenceBuffer
from assistant.vad import Endpointer
from assistant.wakeword import WakeWordDetector

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
)
log = logging.getLogger(__name__)


def setup_signal_handlers(shutdown_event):
    """Set up signal handlers for graceful shutdown."""

    def handler(signum, frame):
        log.info("Received signal %s, shutting down...", signum)
        shutdown_event.set()

    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)


def main() -> int:
    parser = argparse.ArgumentParser(description="Voice assistant")
    parser.add_argument(
        "--devices",
        action="store_true",
        help="List audio devices and exit",
    )
    parser.add_argument(
        "--config",
        type=Path,
        help="Path to config.yaml",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if args.devices:
        print(list_devices())
        return 0

    # Load configuration
    config = load_config(args.config)
    log.info("Configuration loaded")

    # Check for API key
    if not config.api_key:
        log.error(
            "NVIDIA API key not found. Set %s in environment or .env file",
            config.llm.api_key_env,
        )
        return 1

    # Initialize components
    log.info("Initializing components...")

    # Audio I/O
    mic = Microphone(
        sample_rate=config.audio.sample_rate,
        frame_samples=config.audio.frame_samples,
        device=config.audio.input_device,
    )
    speaker = Speaker(
        device=config.audio.output_device,
        volume=config.tts.volume,
    )

    # Wake word detection
    wakeword = WakeWordDetector(
        model_name=config.wakeword.model,
        threshold=config.wakeword.threshold,
        cooldown_s=config.wakeword.cooldown_s,
    )
    wakeword.load()

    # Voice activity detection (using Endpointer)
    vad = Endpointer(
        config=config.vad,
        sample_rate=config.audio.sample_rate,
        frame_samples=config.audio.frame_samples,
    )

    # Speech to text
    stt = Transcriber(
        config=config.stt,
        api_key=config.api_key,
        sample_rate=config.audio.sample_rate,
    )

    # Text to speech
    tts_engine = PiperEngine(voice=config.tts.voice)
    tts = TTSVoice(config=config.tts, speaker=speaker)

    # LLM client (OpenAI-compatible for NIM)
    from openai import OpenAI
    llm_client = OpenAI(
        base_url=config.llm.base_url,
        api_key=config.api_key,
    )

    # Sentence buffer for streaming TTS
    sentence_buffer = SentenceBuffer(min_chars=24)

    # Tool implementations would go here - for now we'll stub them
    # In a full implementation, these would be imported from a tools module
    available_tools = {
        "time": lambda: time.strftime("%I:%M %p"),
        "timers": lambda: "No active timers",  # Stub
        "notes": lambda: "Notes feature not implemented yet",  # Stub
        "system": lambda: f"System: {sys.platform}",  # Stub
    }

    # Load models that need it
    log.info("Loading models...")
    wakeword.load()  # Already called in constructor, but being explicit
    stt.load()
    tts_engine.load()
    tts.load()

    log.info("All components initialized")

    # Main loop
    log.info("Starting voice assistant. Say '%s' to begin.", config.wakeword.model.replace('_', ' '))

    try:
        with mic, speaker:
            tts.start()
            while True:
                # Wait for wake word
                frame = mic.read()
                if wakeword.process(frame):
                    log.info("Wake word detected!")
                    # Play activation sound if enabled
                    if config.wakeword.activation_sound:
                        # Play a short chime
                        chime = tone(800, 150, config.audio.sample_rate, 0.2)
                        speaker.play(chime, config.audio.sample_rate)

                    # Process utterance with VAD
                    log.info("Listening for command...")
                    vad.begin()  # Reset for new utterance
                    audio_frames = []
                    speech_started = False

                    while True:
                        frame = mic.read(timeout=1.0)  # 1 second timeout for responsiveness
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
                            log.info("Listening timeout")
                            break
                        elif speech_started:
                            audio_frames.append(frame)

                    if not audio_frames:
                        log.info("No speech detected")
                        continue

                    # Concatenate audio frames
                    audio_data = np.concatenate(audio_frames)

                    # Convert to float32 for STT
                    audio_float = to_float32(audio_data)

                    # Transcribe
                    log.info("Transcribing...")
                    try:
                        text = stt.transcribe(audio_float)
                        if not text.strip():
                            log.info("Empty transcription")
                            continue
                        log.info("User said: %s", text)
                    except Exception as e:
                        log.error("STT failed: %s", e)
                        continue

                    # Process with LLM (with tool use)
                    try:
                        response = process_with_llm(
                            llm_client=llm_client,
                            config=config,
                            user_text=text,
                            available_tools=available_tools,
                        )
                    except Exception as e:
                        log.error("LLM processing failed: %s", e)
                        response = "Sorry, I encountered an error processing your request."

                    # Speak response
                    log.info("Assistant: %s", response)
                    tts.say(response)
                    tts.wait()  # Wait for speech to finish before continuing

    except KeyboardInterrupt:
        log.info("Shutting down...")
    except Exception as e:
        log.error("Fatal error: %s", e, exc_info=True)
        return 1
    finally:
        # Cleanup
        tts.stop()
        tts.wait()
        mic.stop()
        speaker.close()
        wakeword.reset()
        vad.begin()  # Reset VAD state

    return 0


def process_with_llm(
    llm_client: OpenAI,
    config,
    user_text: str,
    available_tools: dict[str, callable],
) -> str:
    """Process user text with LLM, handling tool calls."""

    messages = [
        {"role": "system", "content": config.system_prompt},
        {"role": "user", "content": user_text},
    ]

    for round_num in range(config.llm.max_tool_rounds):
        try:
            response = llm_client.chat.completions.create(
                model=config.llm.model,
                messages=messages,
                temperature=config.llm.temperature,
                max_tokens=config.llm.max_tokens,
                timeout=config.llm.timeout_s,
            )

            message = response.choices[0].message
            content = message.content or ""

            # Check if the model wants to use tools
            # This is a simplified version - in practice, you'd check for tool calls in the response
            # For now, we'll just return the content
            messages.append({"role": "assistant", "content": content})

            # If no tool calls or we've hit max rounds, return the response
            if not getattr(message, 'tool_calls', None) or round_num >= config.llm.max_tool_rounds - 1:
                return content

            # Handle tool calls (simplified)
            # In a full implementation, you'd execute the tools and add results to messages
            log.debug("Tool calls detected but not fully implemented: %s", getattr(message, 'tool_calls', None))

        except Exception as e:
            log.error("LLM API error: %s", e)
            return f"Sorry, I had trouble connecting to my brain: {e}"

    return "I'm having trouble processing that right now."


if __name__ == "__main__":
    sys.exit(main())