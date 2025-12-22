---
tags:
  - exploit-crafting
  - buffer-overflow
  - malicious-file
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
updated_at: '2025-12-14T17:24:08.226Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[T1203.001]]'
id: fc09d57f-cb8a-4717-a339-335e7ef5faea
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Craft Malicious Closed Captions File for Buffer Overflow

## Summary

This procedure creates a specially crafted closed captions file that exploits the buffer overflow in CS:GO's CHudCloseCaption::SplitCommand by providing oversized input strings to overflow fixed-size arrays.

## Description

The vulnerability allows arbitrary input to be parsed without bounds, where commands prefixed with '<' and followed by long strings (>256 chars) overflow the cmd array, and args after ':' overflow the args array. The file is typically a text-based .closecaption or similar format loaded by the game, leading to stack corruption and potential RCE on Windows.

## Requirements

1. Text editor or script to generate long strings
2. Knowledge of closed caption file format (simple text with <command:args> structure)
3. Target game version vulnerable to the issue

## Defense

Defensive measures and detection strategies:

- Patch game to include bounds checking
- Scan for malformed closed caption files
- Educate users on avoiding untrusted game files

## Objectives

1. Generate input exceeding array sizes to trigger overflow
2. Ensure payload structure matches parsing expectations
3. Prepare file for delivery and loading

## Instructions

### Step 1: Structure the File Format

**Context**: Build the basic syntax for closed caption entries.

Create a text file with lines like "<command>" where command is the payload.

> Use UTF-16 or ANSI encoding matching game expectations; avoid null bytes initially.

### Step 2: Overflow the Cmd Array

**Context**: Craft a string longer than 256 characters after '<'.

Append a repeating pattern (e.g., 300+ 'A's) after '<' to exceed cmd[256], ensuring the while loop copies beyond bounds.

> Example payload: "<AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA>"

### Step 3: Optionally Overflow Args and Finalize

**Context**: Add args after ':' for double overflow if needed.

Include ":BBBBBBBB..." with >256 'B's to target args array.

> Save as .vdf or .txt compatible with game's caption loading; test in a controlled environment to confirm crash.

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

- exploit-crafting
- buffer-overflow
- csgo
