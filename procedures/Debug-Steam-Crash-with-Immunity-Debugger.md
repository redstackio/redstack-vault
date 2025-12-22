---
tags:
  - debugging
  - overflow
  - stack
type: procedure
tools:
  - '[[tools/Immunity-Debugger]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Windows
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: 0fde00d6-8efd-48b0-afb7-060d4eb17ba3
created_at: '2025-12-14T17:24:18.428Z'
updated_at: '2025-12-14T17:24:18.428Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Debug-Steam-Crash-with-Immunity-Debugger

## Summary

This procedure uses Immunity Debugger to attach to Steam.exe, replay fuzzed responses, and analyze the stack overflow during unicode conversion in the serverbrowser library.

## Description

Attach debugger to Steam process, set breakpoints on UDP reception and string handling. Trigger crash and inspect stack for overflow evidence, such as corrupted return address and EIP control. Confirms lack of canary protection on Windows. Target: Crashing Steam instance. Prerequisites: Immunity Debugger, fuzzed server running. Outcomes: Detailed overflow analysis for ROP development.

## Requirements

1. Immunity Debugger installed on Windows
2. Steam.exe running and crashing reproducibly
3. Knowledge of assembly and stack layouts

## Defense

Defensive measures and detection strategies:

- Enable stack canaries in client binaries
- Monitor for debugger attachments in anti-tampering
- Crash reporting to detect patterns

## Objectives

1. Confirm buffer overflow location
2. Identify exploitable stack corruption
3. Extract base addresses for ROP

## Instructions

### Step 1: Attach to Process

**Context**: Launch Immunity and attach to Steam.exe.

**Command** (In Immunity):
File > Attach > Select Steam.exe

> Attaches debugger. Expected output: Process paused, modules loaded.

### Step 2: Set Breakpoints

**Context**: Break on UDP handling and unicode functions.

**Command** (In Immunity):
F2 on suspected functions (e.g., recvfrom, WideCharToMultiByte)

> Sets BP. Expected output: Hits on query reception.

### Step 3: Replay and Inspect

**Context**: Trigger query, step through crash, examine stack.

**Command** (Step in Immunity):
F7 to step into; View > Stack to inspect

> Analyzes overflow. Expected output: Stack shows overwrite, EIP controlled.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Immunity-Debugger]]

## Tags

- debugging
- overflow
- stack
