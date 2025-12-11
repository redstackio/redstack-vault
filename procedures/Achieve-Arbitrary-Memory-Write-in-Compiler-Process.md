---
tags:
  - memory-write
  - bd-j
  - ps4
  - ps5
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - PS4
  - PS5
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 8c164b96-12f3-437f-9fe3-8b4912279568
created_at: '2025-12-11T03:47:57.335Z'
updated_at: '2025-12-11T03:47:57.335Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Achieve Arbitrary Memory Write in Compiler Process

## Summary

This procedure achieves arbitrary memory writes in the JIT compiler process on PS4 and PS5.

## Description

By sending a CompilerAgentRequest with an untrusted compiler_data pointer, data is copied into JIT memory without validation.

## Requirements

1. Access to compiler receiver thread
2. Crafted request with malicious pointer
3. Network access to send requests

## Defense

Defensive measures and detection strategies:

- Validate pointers in compiler requests
- Monitor for anomalous memory operations

## Objectives

1. Write to JIT memory
2. Execute arbitrary payloads
3. Enable further exploitation

## Instructions

### Step 1: Craft CompilerAgentRequest

**Context**: Include untrusted pointer.

Prepare request with compiler_data pointing to target memory.

> This sets up the write-what-where primitive.

### Step 2: Send Request

**Context**: Copy data into memory.

Transmit the request to the compiler process.

> Expected: Successful memory write and payload execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #memory-write
- #bd-j
