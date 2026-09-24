# Graph Report - Personal-Assistant  (2026-09-24)

## Corpus Check
- 17 files · ~6,585 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 3 file(s) not represented in the graph (top: (none) 2, .example 1)

## Summary
- 223 nodes · 327 edges · 18 communities (13 shown, 5 thin omitted)
- Extraction: 99% EXTRACTED · 1% INFERRED · 0% AMBIGUOUS · INFERRED: 3 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e38353e7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Endpointer
- config.py
- Speaker
- SentenceBuffer
- audio.py
- Tools
- run.py
- Voice
- Microphone
- Transcriber
- WakeWordDetector
- __init__.py
- PiperEngine
- Personal Assistant
- google_auth_oauthlib_flow
- Graphify + Antigravity Project Workflow & Setup Guide
- rules/graphify.md
- workflows/graphify.md

## God Nodes (most connected - your core abstractions)
1. `Speaker` - 17 edges
2. `Voice` - 14 edges
3. `main()` - 14 edges
4. `Microphone` - 12 edges
5. `Tools` - 11 edges
6. `Endpointer` - 11 edges
7. `Transcriber` - 9 edges
8. `WakeWordDetector` - 9 edges
9. `tone()` - 8 edges
10. `load_config()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `play_chime()` --uses--> `Speaker`  [INFERRED]
  voice-assistant/assistant/tts.py → voice-assistant/assistant/audio.py
- `Voice` --uses--> `Speaker`  [INFERRED]
  voice-assistant/assistant/tts.py → voice-assistant/assistant/audio.py
- `main()` --calls--> `Microphone`  [EXTRACTED]
  voice-assistant/run.py → voice-assistant/assistant/audio.py
- `main()` --calls--> `Speaker`  [EXTRACTED]
  voice-assistant/run.py → voice-assistant/assistant/audio.py
- `main()` --calls--> `load_config()`  [EXTRACTED]
  voice-assistant/run.py → voice-assistant/assistant/config.py

## Import Cycles
- None detected.

## Communities (18 total, 5 thin omitted)

### Community 0 - "Endpointer"
Cohesion: 0.12
Nodes (13): _default_model_path(), Endpointer, _pre_roll_frames(), ndarray, Path, Arm the endpointer. Must be called before feeding frames., Feed one int16 frame. Returns ``"speech_start"``, ``"utterance_end"``,…, Re-slice an arbitrary frame length into model-sized chunks. (+5 more)

### Community 1 - "config.py"
Cohesion: 0.10
Nodes (21): Any, dataclasses, _apply_env_overrides(), AssistantConfig, AudioConfig, _build(), Config, LLMConfig (+13 more)

### Community 2 - "Speaker"
Cohesion: 0.21
Nodes (4): Play an int16 buffer, blocking until done or aborted., Stop playback now and discard whatever is still queued., Streaming PCM playback with an abort that takes effect immediately. ``abort``…, Speaker

### Community 3 - "SentenceBuffer"
Cohesion: 0.28
Nodes (5): re, clean_for_speech(), Text helpers for spoken output., Accumulates streamed tokens and emits whole sentences. Speaking on sentence…, SentenceBuffer

### Community 4 - "audio.py"
Cohesion: 0.11
Nodes (23): callable, OpenAI, queue, sounddevice, threading, chunker(), list_devices(), ndarray (+15 more)

### Community 5 - "Tools"
Cohesion: 0.12
Nodes (10): Cancel a timer. Args: params: JSON string with "timer_id" or "label" to cancel…, Take a note. Args: params: JSON string with "text" (str) to save as a note…, List recent notes. Args: params: JSON string with optional "limit" (int,…, Collection of tools available to the voice assistant., Get system information. Args: _: Unused parameter (for tool interface…, Remove expired timers., Get the current time. Args: _: Unused parameter (for tool interface…, Set a timer. Args: params: JSON string with "seconds" (int) and optional… (+2 more)

### Community 6 - "run.py"
Cohesion: 0.11
Nodes (22): argparse, collections, datetime, io, json, logging, numpy, os (+14 more)

### Community 7 - "Voice"
Cohesion: 0.15
Nodes (5): Queue a sentence for speaking., Block until everything queued has been spoken., Barge-in: drop queued sentences and cut playback immediately., Serializes synthesis and playback on a background worker. Callers push…, Voice

### Community 8 - "Microphone"
Cohesion: 0.24
Nodes (3): Microphone, Blocking frame reader over a sounddevice input stream., Throw away anything already buffered — used after barge-in.

### Community 9 - "Transcriber"
Cohesion: 0.31
Nodes (5): _env_key(), ndarray, Run a fraction of a second of silence through the model so the first real…, Transcriber, _wav_bytes()

### Community 10 - "WakeWordDetector"
Cohesion: 0.22
Nodes (6): ndarray, Path, Scores fixed-size frames and reports when the phrase fires. ``process`` returns…, Feed one frame; True if the wake word just fired., Clear the model's internal audio buffer (call after a barge-in)., WakeWordDetector

### Community 12 - "PiperEngine"
Cohesion: 0.18
Nodes (6): NullEngine, PiperEngine, ndarray, Local neural TTS. Roughly 0.1x realtime on a modern CPU core., Return int16 PCM for the given text., Used when tts.backend is 'none' — prints instead of speaking.

### Community 13 - "Personal Assistant"
Cohesion: 0.18
Nodes (10): Explore the Codebase with Graphify, Features, Graphify Commands, Installation, License, Personal Assistant, Project Structure, Requirements (+2 more)

## Knowledge Gaps
- **18 isolated node(s):** `graphify`, `Workflow: graphify`, `1. New Project Setup (One-Time)`, `WakeWordConfig`, `VadConfig` (+13 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 115 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tools` connect `Tools` to `run.py`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Why does `Speaker` connect `Speaker` to `audio.py`, `PiperEngine`, `run.py`, `Voice`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Why does `Voice` connect `Voice` to `Speaker`, `audio.py`, `PiperEngine`, `run.py`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Speaker` (e.g. with `play_chime()` and `Voice`) actually correct?**
  _`Speaker` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `graphify`, `Workflow: graphify`, `1. New Project Setup (One-Time)` to the rest of the system?**
  _18 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Endpointer` be split into smaller, more focused modules?**
  _Cohesion score 0.1225296442687747 - nodes in this community are weakly interconnected._
- **Should `config.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10333333333333333 - nodes in this community are weakly interconnected._