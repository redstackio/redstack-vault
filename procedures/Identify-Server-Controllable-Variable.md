---
id: proc-csgo-controllable-var
tags:
  - reverse-engineering
  - global-variables
  - payload-staging
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Discovery]]'
updated_at: '2025-12-14T17:24:08.944Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Process Discovery]]'
---
# Identify-Server-Controllable-Variable

## Summary

This procedure identifies a server-controlled global variable in the CS:GO client with a known, predictable address for staging exploit payloads, such as the map name string copied from server messages.

## Description

Analysis of CS:GO's Protocol Buffer messages reveals server-sent data like map names are unsanitized and copied to fixed global locations in client_panorama.dll. This allows attackers to place ROP chains at known offsets without additional disclosures. The target environment is Windows with C++ and Protocol Buffers; prerequisites include reverse-engineering tools or pseudocode from decompilers. Expected outcome: A reliable staging point for payloads.

## Requirements

1. Access to CS:GO binaries for static analysis (e.g., IDA Pro or Ghidra).
2. Knowledge of Protocol Buffer definitions for server messages.
3. Running client for dynamic verification.

## Defense

Defensive measures and detection strategies:

- Sanitize all server-to-client string copies with bounds checking.
- Randomize global variable addresses or use stack allocation.
- Log anomalous map name lengths or contents.

## Objectives

1. Primary objective: Locate a fixed-address variable for payload injection.
2. Secondary objective: Confirm no null-byte truncation issues.
3. Expected outcome: Variable selected for use in payload crafting.

## Instructions

### Step 1: Analyze Protocol Buffers

**Context**: Review message definitions to find controllable fields.

Examine CSVCMsg_ServerInfo or similar for map name field.

> Parse .proto files; identify string fields copied to globals. Expected output: Map name as candidate.

### Step 2: Reverse Engineer Client Handler

**Context**: Decompile the message handler to trace copies.

Use disassembler on client_panorama.dll to find strcpy-like calls.

> Trace from handler to global var assignment. Expected output: Offset of global (e.g., +0x1234 from base).

### Step 3: Verify Predictability

**Context**: Test in running client to ensure address stability.

Send test map name and inspect memory.

> Use debugger to confirm copy location. Expected output: Consistent address across runs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Process Discovery]] Process Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[reverse-engineering]]
- [[global-variables]]
- [[payload-staging]]
