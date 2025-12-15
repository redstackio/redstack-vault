---
id: proc-4
tags:
  - csgo
  - heap-spray
  - aslr
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Windows
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Dynamic-link Library Injection]]'
updated_at: '2025-12-14T17:23:54.621Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Dynamic-link Library Injection]]'
---
# Spray-Heap-with-Sendprop-Objects-to-Enable-ASLR-Break

## Summary

This procedure sprays the client heap with controlled sendprop_t objects via protobuf messages to fragment memory and enable recovery of engine.dll pointers from leaks.

## Description

Server sends repeated CSVCMsg_SendTable messages (256 iterations) each containing multiple sendprop_t structures with unique identifiers (e.g., type=0x1337ee00, num_bits=0x00ff00ff). Deallocation cycles mix these with leaked regions, allowing pattern matching to locate pointers.

## Requirements

1. Stable client connection
2. Protobuf serialization in server script

## Defense

- Bounds check and limit incoming SendTable message volume
- Randomize heap allocations
- Detect rapid protobuf floods

## Objectives

1. Allocate identifiable objects on heap
2. Facilitate pointer location in leaks
3. Avoid client crash from spray

## Instructions

### Step 1: Send Spray Messages

**Context**: During connection, server floods CSVCMsg_SendTable.

Handled automatically by poc.py after connection.

> Messages crafted with unique props. Expected output: Client processes without desync; heap filled.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Dynamic-link Library Injection]] Dynamic-link Library Injection

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Python]]

## Tags

- csgo
- heap-spray
- aslr
