---
id: proc-craft-tlrf-overflow
tags:
  - payload-crafting
  - heap-overflow
  - exploit-development
type: procedure
tools:
  - '[[tools/Hex-Editor]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Nintendo 3DS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:41.402Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Craft-Malicious-TLRF-Chunk-for-Heap-Overflow

## Summary

This procedure crafts a malicious Swapnote message file by modifying TLRF chunk data to trigger a heap buffer overflow, enabling controlled data copy beyond buffer boundaries for heap manipulation.

## Description

Building on reverse engineering insights, attackers edit a valid .plt message file to set oversized values in the TLRF_buffer. Specifically, large sizes (e.g., 0x1000) at offsets 0x70C and 0x71C, paired with source offsets (e.g., 0x6DC, 0x6EC), cause memcpy to overflow fixed-size heap buffers. This sets up unsafe unlink for arbitrary code execution. The target environment is 3DS Swapnote; outcomes include a deployable payload file.

## Requirements

1. Valid Swapnote message file template
2. Hex editor tool for binary modification
3. Understanding of TLRF chunk structure from reverse engineering

## Defense

Defensive measures and detection strategies:

- Validate message file sizes before parsing
- Implement bounds checks in memcpy operations via patches
- Scan for malformed TLRF chunks in exchanged messages

## Objectives

1. Embed overflow-triggering values in TLRF chunk
2. Ensure payload maintains message file validity
3. Prepare for heap manipulation leading to RCE

## Instructions

### Step 1: Load Template File

**Context**: Start with a benign Swapnote message.

Open a valid .plt file in [[tools/Hex-Editor]].

### Step 2: Modify Sizes and Offsets

**Context**: Insert overflow parameters.

Navigate to TLRF_buffer: set bytes at 0x70C and 0x71C to 0x00 0x10 0x00 0x00 (size 0x1000), and at 0x6DC/0x6EC to controlled source offsets. Append attacker data for post-overflow copy.

### Step 3: Validate Payload

**Context**: Test file integrity.

Save and attempt to load in a controlled 3DS environment to confirm parsing without immediate crash.

**Expected Output**: Modified .plt file with embedded exploit primitives.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Hex-Editor]]

## Tags

- [[payload-crafting]]
- [[heap-overflow]]
