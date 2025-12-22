---
tags:
  - debugging
  - gdb
  - segfault
type: procedure
tools:
  - '[[tools/GDB]]'
  - '[[tools/pngcrush]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/gdb-backtrace]]'
  - '[[commands/gdb-info-registers]]'
  - '[[commands/pngcrush-process-splt-png]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.371Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 75fd80a1-28ee-45a4-a1d4-913e29d90d59
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Debug-Segfault-with-GDB

## Summary

This procedure employs GDB to debug the segmentation fault in pngcrush, capturing backtraces and register states to pinpoint the double-free in libc_free called from png_free_data.

## Description

GDB attaches to the process, catches the SIGSEGV, and allows inspection of the call stack and CPU registers at the crash point. The backtrace reveals the flow from main (pngcrush.c:6061) through png_free_data (png.c:542) to libc_free (malloc.c:3709), with registers showing an invalid pointer (e.g., rdi=0x5555555555555555) being freed. This confirms the memory corruption from sPLT chunk handling. Requires debug symbols in pngcrush binary for full source visibility.

## Requirements

1. GDB installed on Linux
2. pngcrush compiled with -g for debug info
3. Core dump or live process from crash

## Defense

Defensive measures and detection strategies:

- Enable core dumps and analyze with GDB in production for crash forensics
- Use static analyzers like Coverity to detect double-frees pre-deployment
- Restrict PNG chunk types in processing libraries

## Objectives

1. Capture crash backtrace to identify call chain
2. Inspect registers for invalid pointers
3. Correlate segfault to double-free vulnerability

## Instructions

### Step 1: Launch GDB and Run pngcrush

**Context**: Start GDB with arguments to reproduce the crash and catch the signal.

```bash
gdb --args ./pngcrush -reduce -brute ps1n0g08.png /dev/null
```

Then `(gdb) run` to execute.

### Step 2: Get Backtrace on Crash

**Context**: Upon SIGSEGV, print the stack trace to see the function call leading to the free.

**Command** ([[commands/gdb-backtrace]]):
```bash
(gdb) bt
```

> Displays frames: #0 libc_free (malloc.c:3709), #1 png_free_data (png.c:542), #2 main (pngcrush.c:6061).

**Expected Output**: Full backtrace confirming double-free invocation from PNG chunk freeing in main.

### Step 3: Inspect Registers

**Context**: Examine CPU registers to identify the corrupted pointer causing the invalid free.

**Command** ([[commands/gdb-info-registers]]):
```bash
(gdb) i r
```

> Shows rdi=0x5555555555555555 (pointer to invalid memory), rip=0x7ffff784a939 (in libc_free), rax=0x0, etc.

**Expected Output**: Register dump highlighting the bogus address in rdi, passed to free.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used

- [[commands/gdb-backtrace]]
- [[commands/gdb-info-registers]]

## Tools Used

- [[tools/GDB]]

## Tags

- debugging
- gdb
- segfault
