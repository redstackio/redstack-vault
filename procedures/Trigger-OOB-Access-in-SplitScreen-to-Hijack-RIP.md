---
id: proc-7
tags:
  - csgo
  - oob-read
  - rip-hijack
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Hollowing]]'
updated_at: '2025-12-14T17:23:54.586Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Process Hollowing]]'
---
# Trigger-OOB-Access-in-SplitScreen-to-Hijack-RIP

## Summary

This procedure sends a malformed CSVCMsg_SplitScreen with an unchecked 'slot' index to perform an out-of-bounds read from engine.dll's global array, fetching and dereferencing fake pointers to hijack RIP.

## Description

The 'slot' field indexes a static array without bounds check. OOB value fetches attacker pointer (to fake object), deref at +8 gets fake vtable, then +0xAC calls controlled function, pivoting RIP.

## Requirements

1. Fake objects set up in convars
2. Known array offsets

## Defense

- Add bounds checking to 'slot' in SplitScreen handler
- Validate all pointer dereferences
- ASLR and DEP enforcement

## Objectives

1. Access OOB array element
2. Dereference to gain code control
3. Set up for ROP

## Instructions

### Step 1: Send Malformed Message

**Context**: Server transmits CSVCMsg_SplitScreen with slot=0x100.

Handled by poc.py.

> Expected output: Client executes deref; RIP controlled.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Process Hollowing]] Modify Registry Run Keys / Startup Folder (analogy for control hijack)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Python]]

## Tags

- csgo
- oob-read
- rip-hijack
