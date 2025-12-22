---
tags:
  - buffer-overflow
  - strcpy
type: procedure
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:49.795Z'
sub_techniques: []
id: b647892c-ba8b-4488-b5ff-c65cd41420af
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Trigger-Buffer-Overflow-with-Oversized-Input

## Summary

This procedure supplies oversized user input to curl, exploiting the lack of bounds checking in strcpy() to overflow a stack buffer and corrupt memory, including the return address.

## Description

The vulnerability occurs in curl's handling of input (e.g., via -d flag or URL params) copied via strcpy() in libcrypto without validation. Target environment is Linux with curl 8.11.0. Outcomes include stack corruption, segfault, and setup for control flow hijack. Prerequisites: Running curl process.

## Requirements

1. Vulnerable curl 8.11.0
2. Ability to pipe or pass large strings
3. Python or similar for payload generation

## Defense

Defensive measures and detection strategies:

- Input sanitization and length limits in applications
- Stack protection (canaries, NX bits)
- Log large input attempts and crashes (e.g., via syslog)

## Objectives

1. Cause buffer overrun
2. Verify crash via segfault
3. Corrupt stack for further exploitation

## Instructions

### Step 1: Generate Oversized Payload

**Context**: Create input exceeding buffer size (e.g., 1024 bytes) to trigger overflow.

**Command**:

```bash
python3 -c 'print("A"*1024)' > payload.txt
```

> Generates file with repeated 'A's; use for input.

### Step 2: Feed Payload to curl

**Context**: Provide the oversized input to invoke strcpy().

**Command**:

```bash
cat payload.txt | ./curl -d @- http://target/endpoint
```

> Curl processes input, strcpy() overflows; expected output: Segmentation fault, core dump possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- buffer-overflow
- strcpy
