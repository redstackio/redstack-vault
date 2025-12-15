---
id: proc-6
tags:
  - csgo
  - fake-vtable
  - convars
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
updated_at: '2025-12-14T17:23:54.599Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Dynamic-link Library Injection]]'
---
# Set-Up-Fake-Objects-Using-Convars-for-OOB-Control

## Summary

This procedure crafts convar messages to allocate strings on the heap and store pointers in engine.dll's global array, forming fake objects and vtables for OOB exploitation.

## Description

CMsg_CVars messages copy attacker-controlled strings to heap and update global convar objects. Strings are shaped to mimic object structures, with pointers chaining to other convars for vtable faking at controlled offsets.

## Requirements

1. ASLR broken from prior parsing
2. Knowledge of convar array layout

## Defense

- Bounds check convar indices
- Validate string copies and pointer stores
- Sanitize incoming CMsg_CVars

## Objectives

1. Place controlled data in global array
2. Create fake vtable for dereference
3. Prepare for OOB trigger

## Instructions

### Step 1: Send Convar Messages

**Context**: Server sends CMsg_CVars with crafted payloads.

Handled by poc.py using protobuf.

> Example: String 'A' * 0x100 + fake_ptr. Expected output: Client heap updated; no crash.

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
- fake-vtable
- convars
