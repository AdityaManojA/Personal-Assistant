# Graph Report - Personal-Assistant  (2026-09-24)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 202 nodes · 311 edges · 12 communities (11 shown, 1 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a157b05e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- vad.py
- config.py
- Speaker
- run.py
- audio.py
- Tools
- stt.py
- Voice
- Microphone
- Transcriber
- WakeWordDetector
- __init__.py

## God Nodes (most connected - your core abstractions)
1. `Speaker` - 17 edges
2. `Voice` - 14 edges
3. `main()` - 14 edges
4. `Microphone` - 12 edges
5. `Endpointer` - 11 edges
6. `Tools` - 11 edges
7. `WakeWordDetector` - 9 edges
8. `Transcriber` - 9 edges
9. `PiperEngine` - 8 edges
10. `load_config()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `play_chime()` --uses--> `Speaker`  [INFERRED]
  voice-assistant/assistant/tts.py → voice-assistant/assistant/audio.py
- `Voice` --uses--> `Speaker`  [INFERRED]
  voice-assistant/assistant/tts.py → voice-assistant/assistant/audio.py
- `main()` --calls--> `Endpointer`  [EXTRACTED]
  voice-assistant/run.py → voice-assistant/assistant/vad.py
- `main()` --calls--> `WakeWordDetector`  [EXTRACTED]
  voice-assistant/run.py → voice-assistant/assistant/wakeword.py
- `main()` --calls--> `Speaker`  [EXTRACTED]
  voice-assistant/run.py → voice-assistant/assistant/audio.py

## Import Cycles
- None detected.

## Communities (12 total, 1 thin omitted)

### Community 0 - "vad.py"
Cohesion: 0.11
Nodes (16): collections, pathlib, _default_model_path(), Endpointer, _pre_roll_frames(), ndarray, Path, Voice activity detection and utterance endpointing. This is the component that… (+8 more)

### Community 1 - "config.py"
Cohesion: 0.10
Nodes (21): Any, dataclasses, _apply_env_overrides(), AssistantConfig, AudioConfig, _build(), Config, LLMConfig (+13 more)

### Community 2 - "Speaker"
Cohesion: 0.10
Nodes (10): Play an int16 buffer, blocking until done or aborted., Stop playback now and discard whatever is still queued., Streaming PCM playback with an abort that takes effect immediately. ``abort``…, Speaker, NullEngine, PiperEngine, ndarray, Local neural TTS. Roughly 0.1x realtime on a modern CPU core. (+2 more)

### Community 3 - "run.py"
Cohesion: 0.11
Nodes (18): argparse, callable, OpenAI, re, signal, sys, list_devices(), Human-readable device listing for `run.py --devices`. (+10 more)

### Community 4 - "audio.py"
Cohesion: 0.16
Nodes (17): numpy, queue, sounddevice, threading, chunker(), ndarray, Microphone capture and speaker playback. Everything downstream wants 16 kHz…, int16 -> float32 in [-1, 1], which is what the models expect. (+9 more)

### Community 5 - "Tools"
Cohesion: 0.12
Nodes (10): Cancel a timer. Args: params: JSON string with "timer_id" or "label" to cancel…, Take a note. Args: params: JSON string with "text" (str) to save as a note…, List recent notes. Args: params: JSON string with optional "limit" (int,…, Collection of tools available to the voice assistant., Get system information. Args: _: Unused parameter (for tool interface…, Remove expired timers., Get the current time. Args: _: Unused parameter (for tool interface…, Set a timer. Args: params: JSON string with "seconds" (int) and optional… (+2 more)

### Community 6 - "stt.py"
Cohesion: 0.15
Nodes (12): datetime, io, json, logging, os, time, typing, uuid (+4 more)

### Community 7 - "Voice"
Cohesion: 0.15
Nodes (5): Queue a sentence for speaking., Block until everything queued has been spoken., Barge-in: drop queued sentences and cut playback immediately., Serializes synthesis and playback on a background worker. Callers push…, Voice

### Community 8 - "Microphone"
Cohesion: 0.22
Nodes (3): Microphone, Blocking frame reader over a sounddevice input stream., Throw away anything already buffered — used after barge-in.

### Community 9 - "Transcriber"
Cohesion: 0.31
Nodes (5): _env_key(), ndarray, Run a fraction of a second of silence through the model so the first real…, Transcriber, _wav_bytes()

### Community 10 - "WakeWordDetector"
Cohesion: 0.22
Nodes (6): ndarray, Path, Scores fixed-size frames and reports when the phrase fires. ``process`` returns…, Feed one frame; True if the wake word just fired., Clear the model's internal audio buffer (call after a barge-in)., WakeWordDetector

## Knowledge Gaps
- **7 isolated node(s):** `AssistantConfig`, `LLMConfig`, `STTConfig`, `ToolsConfig`, `TTSConfig` (+2 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 98 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tools` connect `Tools` to `stt.py`?**
  _High betweenness centrality (0.168) - this node is a cross-community bridge._
- **Why does `Speaker` connect `Speaker` to `run.py`, `audio.py`, `Voice`?**
  _High betweenness centrality (0.121) - this node is a cross-community bridge._
- **Why does `Voice` connect `Voice` to `Speaker`, `run.py`, `audio.py`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Speaker` (e.g. with `play_chime()` and `Voice`) actually correct?**
  _`Speaker` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `AssistantConfig`, `LLMConfig`, `STTConfig` to the rest of the system?**
  _7 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `vad.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10826210826210826 - nodes in this community are weakly interconnected._
- **Should `config.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10333333333333333 - nodes in this community are weakly interconnected._