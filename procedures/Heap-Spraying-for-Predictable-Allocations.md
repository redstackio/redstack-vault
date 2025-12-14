---
id: proc-heap-spray-001
tags:
  - heap-spray
  - memory-corruption
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
  - '[[Proc Memory]]'
updated_at: '2025-12-14T17:23:42.240Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Proc Memory]]'
---
# Heap-Spraying-for-Predictable-Allocations

## Summary

This procedure involves spraying the client heap with numerous entities in the Source Engine to create a predictable memory layout, facilitating subsequent pointer leakage and overwrite operations in the CS:GO RCE exploit.

## Description

In the context of exploiting the signedness vulnerability in CSVCMsg_ClassInfo, heap spraying allocates a large number of entities (e.g., 500+) to ensure contiguous placement on the heap. Subsequent deletion of specific entities leaves exploitable pointers, enabling controlled memory manipulation without randomization interference. This is crucial for positioning cvars and vtables predictably. Prerequisites include a running malicious server simulator and a connected vulnerable client.

## Requirements

1. Malicious server setup using Python script to send entity spawn/delete messages.
2. Vulnerable CS:GO client connected to the server.
3. Knowledge of entity allocation patterns in Source Engine.

## Defense

Defensive measures and detection strategies:

- Enable Address Space Layout Randomization (ASLR) and monitor for anomalous memory allocations.
- Patch the signedness bug in message handlers; validate class_id as unsigned.
- Detect rapid entity spawning/deletion via server-side logging and rate limiting.

## Objectives

1. Achieve predictable heap layout for underflow exploitation.
2. Position residual vtable pointers for leakage.
3. Prepare memory for cvar and overwrite phases.

## Instructions

### Step 1: Spawn Entities for Spraying

**Context**: Allocate 500+ entities to fill and predict heap positions.

Use the server simulator to broadcast entity creation messages:

```protobuf
// Crafted message in Python script
CSVCMsg_CreateStringTable with entity data for 500+ spawns
```

> This sends Protobuf messages to force client-side entity allocations, making the last ones contiguous.

### Step 2: Delete Specific Entities

**Context**: Free the last 20 entities to leave vtable pointers dangling.

Send deletion commands:

```protobuf
// Via server simulator
CSVCMsg_RemoveStringTable or entity delete for last 20
```

> Deallocation leaves pointers on heap without immediate cleanup, ready for overlap.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Proc Memory]] Stored Application Data

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/CSGO-Malicious-Server-Simulator]]

## Tags

- [[heap-spray]]
- [[memory-corruption]]
