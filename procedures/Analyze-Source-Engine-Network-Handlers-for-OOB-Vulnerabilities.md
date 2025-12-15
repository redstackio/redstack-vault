---
id: proc-source-oob-analysis
tags:
  - recon
  - oob-read
  - source-engine
type: procedure
tools:
  - '[[tools/IDA-Pro]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Windows
  - Gaming
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:24:08.905Z'
skill_level: advanced
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Analyze-Source-Engine-Network-Handlers-for-OOB-Vulnerabilities

## Summary

This procedure involves static analysis of Source Engine network message handlers to identify out-of-bounds read vulnerabilities, such as in GlowPropTurnOff, by reviewing protobuf definitions and assembly code for insufficient bounds checking on entity indices.

## Description

In the attack scenario, an attacker reviews the usermessages.proto file from SteamDatabase and disassembles the handler in client binaries using IDA Pro. The vulnerability arises because entity indices are checked only for >=0 but not for upper bounds, allowing large indices to cause overflow after a left shift by 4 bits, leading to arbitrary memory access in the entitylist array. This is a prerequisite for crafting exploits in games like CS:GO.

## Requirements

1. Access to Source Engine binaries (e.g., CS:GO client)
2. IDA Pro or similar disassembler
3. Knowledge of protobuf and x86 assembly

## Defense

Defensive measures and detection strategies:

- Implement full bounds checking in network handlers (e.g., ent_idx < MAX_ENTITIES)
- Use address sanitizers during development to detect OOB accesses
- Monitor for unusual memory access patterns in game clients

## Objectives

1. Identify vulnerable handlers for OOB reads
2. Confirm root cause in assembly
3. Prepare for payload crafting

## Instructions

### Step 1: Review Protobuf Definitions

**Context**: Examine network message structures to understand entity index handling.

No command; manually review usermessages.proto for GlowPropTurnOff, noting ent_idx field as int32.

> Locate the file from SteamDatabase and search for relevant messages.

### Step 2: Disassemble Handler

**Context**: Analyze assembly to spot missing upper bound checks.

Use [[tools/IDA-Pro]] to load client.dll or similar, navigate to GlowPropTurnOff handler.

> Look for code like: mov eax, ent_idx; test eax, eax; js short loc; shl eax, 4; mov ecx, entitylist[eax]. Confirm no cmp eax, MAX_ENT check.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/IDA-Pro]]

## Tags

- recon
- disassembly
- vulnerability-analysis
