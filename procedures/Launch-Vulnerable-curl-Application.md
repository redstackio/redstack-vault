---
tags:
  - buffer-overflow
  - curl
type: procedure
tools:
  - '[[tools/GDB]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:49.808Z'
sub_techniques: []
id: 7e39b50c-4553-40f9-b2c9-c5f80840f8db
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Launch-Vulnerable-curl-Application

## Summary

This procedure initializes the vulnerable curl 8.11.0 application on Linux, setting up the execution environment for buffer overflow exploitation targeting the unsafe strcpy() call in libcrypto.

## Description

In the attack scenario, curl processes user input without bounds checking, leading to stack overflow. This step launches curl to establish the vulnerable stack frame, typically via command-line invocation with a benign URL. Prerequisites include a Linux system with curl 8.11.0 compiled or installed, linked to libcrypto.so.3. Expected outcome is a running process ready for payload input, with no immediate crash.

## Requirements

1. Linux environment with curl 8.11.0
2. Access to run binaries (local shell)
3. libcrypto.so.3 available

## Defense

Defensive measures and detection strategies:

- Update to patched curl versions (>8.11.0)
- Use ASLR and stack canaries to randomize/protect stack
- Monitor for suspicious curl invocations with large inputs via process auditing (e.g., auditd)

## Objectives

1. Initialize vulnerable process
2. Verify version and linkage
3. Prepare for input triggering

## Instructions

### Step 1: Verify and Launch curl

**Context**: Confirm the vulnerable version and start curl with a test URL to load the stack.

**Command** (no specific named command, direct invocation):

```bash
./curl --version  # Output: curl 8.11.0
./curl http://example.com  # Launches process
```

> This verifies the version and runs curl, processing the URL without overflow yet. Expected output: HTTP response or download completion.

### Step 2: Attach Monitoring if Needed

**Context**: Optionally attach a debugger early for observation.

**Command**:

```bash
gdb --args ./curl http://example.com
(gdb) run
```

> Sets up GDB for stepping; output shows normal execution until input phase.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GDB]]

## Tags

- buffer-overflow
- curl
