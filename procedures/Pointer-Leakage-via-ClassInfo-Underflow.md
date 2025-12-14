---
id: proc-leak-underflow-001
tags:
  - pointer-leak
  - aslr-bypass
  - underflow
type: procedure
tools:
  - '[[tools/CSGO-Malicious-Server-Simulator]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Thread Execution Hijacking]]'
updated_at: '2025-12-14T17:23:42.218Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Thread Execution Hijacking]]'
---
# Pointer-Leakage-via-ClassInfo-Underflow

## Summary

Exploits the signedness bug in CSVCMsg_ClassInfo to perform an array index underflow, overwriting a cvar string's null terminator and leaking a vtable pointer for ASLR bypass in CS:GO RCE.

## Description

The class_id field (int32) is treated as signed but indexed into an unsigned array of size nClasses, allowing negative values to underflow and write out-of-bounds. This extends the cvar string to include the adjacent vtable pointer. Querying the cvar then leaks it, enabling base address calculation for client_panorama.dll. Applies to Source Engine on Windows.

## Requirements

1. Prepared heap with cvar and vtable positioned.
2. Protobuf crafting capability in server.
3. Negative class_id computation (e.g., -1 to underflow by 1).

## Defense

Defensive measures and detection strategies:

- Cast class_id to unsigned or validate >=0 before indexing.
- Bound checks on array access in message handlers.
- Log anomalous cvar queries post-message processing.

## Objectives

1. Trigger underflow to overwrite null terminator.
2. Leak vtable pointer via extended string.
3. Compute module base for further exploitation.

## Instructions

### Step 1: Craft and Send Malicious ClassInfo

**Context**: Use negative class_id to allocate class-infos next to cvar and extend string.

In server script:

```python
# Example in Python simulator
msg = CSVCMsg_ClassInfo()
msg.class_id = -1  # Triggers underflow
send_to_client(msg)
```

> Processes message, writes beyond bounds, includes vtable in string.

### Step 2: Query Leaked Cvar

**Context**: Retrieve extended string containing pointer.

Send query:

```protobuf
CCLCmd_Cvar query for the manipulated cvar
```

> Client returns string with pointer; parse to calculate base = pointer - offset.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Thread Execution Hijacking]] Input Capture (via memory leak)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/CSGO-Malicious-Server-Simulator]]

## Tags

- [[pointer-leak]]
- [[aslr-bypass]]
- [[underflow]]
