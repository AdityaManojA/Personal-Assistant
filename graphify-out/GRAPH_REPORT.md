# Graph Report - Personal-Assistant  (2026-09-24)

## Corpus Check
- 24 files · ~40,423 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 2, .example 1)

## Summary
- 1446 nodes · 1587 edges · 24 communities (18 shown, 6 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a2653d1c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- vad.py
- config.py
- Speaker
- SentenceBuffer
- audio.py
- Tools
- pathlib
- Voice
- Microphone
- stt.py
- WakeWordDetector
- __init__.py
- load
- Personal Assistant
- google_auth_oauthlib_flow
- Graphify + Antigravity Project Workflow & Setup Guide
- rules/graphify.md
- workflows/graphify.md
- process
- reset
- score
- run.py
- patch_wakeword_detector

## God Nodes (most connected - your core abstractions)
1. `load()` - 298 edges
2. `score()` - 298 edges
3. `process()` - 298 edges
4. `reset()` - 298 edges
5. `Speaker` - 18 edges
6. `Voice` - 14 edges
7. `Microphone` - 14 edges
8. `main()` - 14 edges
9. `load_config()` - 12 edges
10. `Endpointer` - 11 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `list_devices()`  [INFERRED]
  voice-assistant/demo_working.py → voice-assistant/assistant/audio.py
- `main()` --calls--> `Microphone`  [INFERRED]
  voice-assistant/demo_working.py → voice-assistant/assistant/audio.py
- `main()` --calls--> `Speaker`  [INFERRED]
  voice-assistant/demo_working.py → voice-assistant/assistant/audio.py
- `main()` --calls--> `load_config()`  [INFERRED]
  voice-assistant/demo_working.py → voice-assistant/assistant/config.py
- `main()` --calls--> `load_config()`  [INFERRED]
  voice-assistant/run_alfred.py → voice-assistant/assistant/config.py

## Import Cycles
- None detected.

## Communities (24 total, 6 thin omitted)

### Community 0 - "vad.py"
Cohesion: 0.11
Nodes (15): collections, _default_model_path(), Endpointer, _pre_roll_frames(), ndarray, Path, Voice activity detection and utterance endpointing. This is the component that…, Arm the endpointer. Must be called before feeding frames. (+7 more)

### Community 1 - "config.py"
Cohesion: 0.10
Nodes (21): Any, dataclasses, _apply_env_overrides(), AssistantConfig, AudioConfig, _build(), Config, LLMConfig (+13 more)

### Community 2 - "Speaker"
Cohesion: 0.10
Nodes (10): Play an int16 buffer, blocking until done or aborted., Stop playback now and discard whatever is still queued., Streaming PCM playback with an abort that takes effect immediately. ``abort``…, Speaker, NullEngine, PiperEngine, ndarray, Local neural TTS. Roughly 0.1x realtime on a modern CPU core. (+2 more)

### Community 3 - "SentenceBuffer"
Cohesion: 0.28
Nodes (5): re, clean_for_speech(), Text helpers for spoken output., Accumulates streamed tokens and emits whole sentences. Speaking on sentence…, SentenceBuffer

### Community 4 - "audio.py"
Cohesion: 0.14
Nodes (19): numpy, queue, sounddevice, threading, chunker(), ndarray, Microphone capture and speaker playback. Everything downstream wants 16 kHz…, int16 -> float32 in [-1, 1], which is what the models expect. (+11 more)

### Community 5 - "Tools"
Cohesion: 0.12
Nodes (10): Cancel a timer. Args: params: JSON string with "timer_id" or "label" to cancel…, Take a note. Args: params: JSON string with "text" (str) to save as a note…, List recent notes. Args: params: JSON string with optional "limit" (int,…, Collection of tools available to the voice assistant., Get system information. Args: _: Unused parameter (for tool interface…, Remove expired timers., Get the current time. Args: _: Unused parameter (for tool interface…, Set a timer. Args: params: JSON string with "seconds" (int) and optional… (+2 more)

### Community 6 - "pathlib"
Cohesion: 0.11
Nodes (19): datetime, json, logging, os, pathlib, sys, time, typing (+11 more)

### Community 7 - "Voice"
Cohesion: 0.15
Nodes (5): Queue a sentence for speaking., Block until everything queued has been spoken., Barge-in: drop queued sentences and cut playback immediately., Serializes synthesis and playback on a background worker. Callers push…, Voice

### Community 8 - "Microphone"
Cohesion: 0.22
Nodes (3): Microphone, Blocking frame reader over a sounddevice input stream., Throw away anything already buffered — used after barge-in.

### Community 9 - "stt.py"
Cohesion: 0.18
Nodes (10): io, _env_key(), ndarray, Speech to text. Default is faster-whisper running locally on CPU with int8…, Run a fraction of a second of silence through the model so the first real…, Transcriber, _wav_bytes(), main() (+2 more)

### Community 10 - "WakeWordDetector"
Cohesion: 0.20
Nodes (7): ndarray, Path, Scores fixed-size frames and reports when the phrase fires. ``process`` returns…, Feed one frame; True if the wake word just fired., Clear the model's internal audio buffer (call after a barge-in)., WakeWordDetector, main()

### Community 12 - "load"
Cohesion: 0.01
Nodes (298): load(), Fake load - do nothing., Fake load - do nothing., Fake load - do nothing., Fake load - do nothing., Fake load - do nothing., Fake load - do nothing., Fake load - do nothing. (+290 more)

### Community 13 - "Personal Assistant"
Cohesion: 0.18
Nodes (10): Explore the Codebase with Graphify, Features, Graphify Commands, Installation, License, Personal Assistant, Project Structure, Requirements (+2 more)

### Community 18 - "process"
Cohesion: 0.01
Nodes (298): process(), Simulate wake word detection every 30 seconds for testing., Simulate wake word detection every 30 seconds for testing., Simulate wake word detection every 30 seconds for testing., Simulate wake word detection every 30 seconds for testing., Simulate wake word detection every 30 seconds for testing., Simulate wake word detection every 30 seconds for testing., Simulate wake word detection every 30 seconds for testing. (+290 more)

### Community 19 - "reset"
Cohesion: 0.01
Nodes (298): Fake reset - do nothing., Fake reset - do nothing., Fake reset - do nothing., Fake reset - do nothing., Fake reset - do nothing., Fake reset - do nothing., Fake reset - do nothing., Fake reset - do nothing. (+290 more)

### Community 20 - "score"
Cohesion: 0.01
Nodes (298): Always return 0.0 (no detection), Always return 0.0 (no detection), Always return 0.0 (no detection), Always return 0.0 (no detection), Always return 0.0 (no detection), Always return 0.0 (no detection), Always return 0.0 (no detection), Always return 0.0 (no detection) (+290 more)

### Community 21 - "run.py"
Cohesion: 0.16
Nodes (12): argparse, callable, OpenAI, signal, list_devices(), Human-readable device listing for `run.py --devices`., main(), process_with_llm() (+4 more)

### Community 22 - "patch_wakeword_detector"
Cohesion: 0.22
Nodes (4): main(), patch_wakeword_detector(), Patch WakeWordDetector to use a fake version that doesn't segfault, Main entry point that applies patch then runs the original voice assistant

## Knowledge Gaps
- **18 isolated node(s):** `AssistantConfig`, `LLMConfig`, `STTConfig`, `ToolsConfig`, `TTSConfig` (+13 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1318 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `score()` connect `score` to `run_alfred_fixed.py`?**
  _High betweenness centrality (0.301) - this node is a cross-community bridge._
- **Why does `process()` connect `process` to `run_alfred_fixed.py`?**
  _High betweenness centrality (0.289) - this node is a cross-community bridge._
- **Why does `load()` connect `load` to `run_alfred_fixed.py`?**
  _High betweenness centrality (0.270) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Speaker` (e.g. with `play_chime()` and `Voice`) actually correct?**
  _`Speaker` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `AssistantConfig`, `LLMConfig`, `STTConfig` to the rest of the system?**
  _18 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `vad.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11384615384615385 - nodes in this community are weakly interconnected._
- **Should `config.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10333333333333333 - nodes in this community are weakly interconnected._