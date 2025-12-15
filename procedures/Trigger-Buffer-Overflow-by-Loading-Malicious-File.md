---
tags:
  - rce
  - file-loading
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
  - Gaming
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:08.213Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1203.001]]'
id: 85d2d81f-1291-4380-8fa4-b094f94972d5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Trigger Buffer Overflow by Loading Malicious File

## Summary

This procedure delivers and loads the crafted closed captions file into CS:GO, triggering the buffer overflow in the parsing functions to achieve remote code execution.

## Description

By tricking the victim into loading the file via the game's closed captioning feature (e.g., console command or resource replacement), the SplitCommand function processes the oversized input, overflowing stack arrays and allowing control over execution flow. This client-side exploit targets Windows gamers, potentially running shellcode for RCE.

## Requirements

1. Malicious file from prior crafting step
2. Delivery method (e.g., social engineering, mod sharing)
3. Victim running vulnerable CS:GO version

## Defense

Defensive measures and detection strategies:

- Disable or restrict closed caption file loading
- Use antivirus to scan game files
- Monitor for unexpected process injections in game memory

## Objectives

1. Deliver file to victim
2. Activate parsing through game feature
3. Confirm code execution via overflow

## Instructions

### Step 1: Deliver the File

**Context**: Get the malicious file onto the victim's system.

Share via email, Discord, or game forums as a "custom captions mod."

> Ensure file is named convincingly, e.g., "custom_captions.txt"

### Step 2: Instruct Loading

**Context**: Guide victim to load via game console or settings.

Use console command like "closecaptionfile custom_captions.txt" in CS:GO console (opened with ~ key).

> Alternatively, replace game resource files in the captions directory.

### Step 3: Verify Execution

**Context**: Observe overflow effects.

Trigger gameplay or events that parse captions; look for crashes or injected code behavior (e.g., via debugger).

> Success: Stack smash leads to EIP overwrite and arbitrary code run.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- [[T1203.001]] Exploitation for Client Execution

## Commands Used


## Tools Used


## Tags

- rce
- file-loading
- csgo
