---
tags:
  - debugging
  - buffer-overflow
type: procedure
tools:
  - '[[tools/GDB]]'
  - '[[tools/strace]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:49.786Z'
sub_techniques: []
id: 238a0e36-e0be-474f-a1fc-f552b3e66af4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Monitor-Overflow-Using-Debugger

## Summary

This procedure uses GDB and strace to observe the buffer overflow during strcpy() execution, capturing stack traces, registers, and memory dumps to confirm corruption.

## Description

In the exploitation flow, debugging tools track the overflow in curl on Linux, revealing details like RIP 0x7ffff7e31b80 and stack at 0x7fffffffd988. Prerequisites: GDB/strace installed, vulnerable curl running. Outcomes: Evidence of overflow for payload refinement.

## Requirements

1. GDB and strace installed on Linux
2. Core dumps enabled (ulimit -c unlimited)
3. Access to curl binary

## Defense

Defensive measures and detection strategies:

- Disable core dumps in production
- Monitor debugger attachments (e.g., ptrace restrictions)
- Anomaly detection on process traces

## Objectives

1. Capture strcpy() execution
2. Inspect stack and registers
3. Validate overflow location

## Instructions

### Step 1: Attach GDB

**Context**: Run curl under GDB to breakpoint at strcpy().

**Command**:

```bash
gdb ./curl
(gdb) break strcpy
(gdb) run -d payload.txt http://target
```

> Hits breakpoint; expected: Stack trace #0 __strcpy_evex at ../sysdeps/x86_64/multiarch/strcpy-evex.S:94.

### Step 2: Examine Memory

**Context**: Dump stack post-overflow.

**Command**:

```bash
(gdb) info registers  # Shows RIP 0x7ffff7e31b80
(gdb) x/32x $rsp  # Memory around 0x7fffffffd988
```

> Reveals corrupted return address.

### Step 3: Use strace for Calls

**Context**: Trace system interactions.

**Command**:

```bash
strace -e trace=memory ./curl -d payload http://target
```

> Output: Abnormal reads/writes indicating overflow.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GDB]]
- [[tools/strace]]

## Tags

- debugging
- buffer-overflow
