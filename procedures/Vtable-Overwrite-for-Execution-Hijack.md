---
id: proc-vtable-overwrite-001
tags:
  - vtable-overwrite
  - execution-hijack
type: procedure
tools:
  - '[[tools/CSGO-Malicious-Server-Simulator]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:23:42.201Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Vtable-Overwrite-for-Execution-Hijack

## Summary

Uses the ClassInfo underflow to overwrite an entity's vtable pointer with the ROP chain address, hijacking control flow during deallocation to execute arbitrary code on the CS:GO client.

## Description

After re-spraying the heap, a negative class_id causes allocation after the last entity, allowing out-of-bounds write to overwrite the vtable. Connection break triggers deallocation, calling the fake vtable and ROP. Targets Windows Source Engine.

## Requirements

1. ROP chain in buffer from prior step.
2. Heap sprayed for entity positioning.
3. Calculated overwrite offset.

## Defense

Defensive measures and detection strategies:

- Validate vtable pointers on allocation/deallocation.
- Use safe unlinking in heap managers.
- Patch underflow and monitor entity manipulations.

## Objectives

1. Overwrite vtable with ROP address.
2. Trigger deallocation to hijack flow.
3. Execute ROP for RCE (e.g., calc.exe).

## Instructions

### Step 1: Re-Spray Heap

**Context**: Ensure last entity is positioned for overwrite.

Repeat spraying as in initial procedure.

### Step 2: Send Overwrite ClassInfo

**Context**: Underflow to write ROP address into vtable.

```python
msg = CSVCMsg_ClassInfo()
msg.class_id = negative_value  # For precise offset
send_to_client(msg)
```

> Allocates and writes beyond, overwriting vtable.

### Step 3: Break Connection to Trigger

**Context**: Deallocation calls fake vtable.

Close server connection:

```python
# In simulator
disconnect_client()
```

> Executes ROP, launches calc.exe.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[DLL Search Order Hijacking]] Hijack Execution Flow: DLL Hijacking

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/CSGO-Malicious-Server-Simulator]]

## Tags

- [[vtable-overwrite]]
- [[execution-hijack]]
