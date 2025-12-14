---
tags:
  - gdb
  - heap-overflow
  - crash-analysis
type: procedure
tools:
  - '[[tools/GDB]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
  - PHP
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
id: 15143b37-c976-47ab-8499-498151402b88
created_at: '2025-12-14T17:28:20.063Z'
updated_at: '2025-12-14T17:28:20.063Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-Heap-Overflow-and-SIGSEGV-with-GDB

## Summary

This procedure continues GDB debugging to observe the heap buffer overflow during string writing, confirming memory corruption and segmentation fault.

## Description

From the breakpoint in php_escape_html_entities_ex(), resume execution and monitor writes around line 1378 where the large input is copied to the small buffer. The overrun corrupts adjacent heap chunks, potentially overwriting PHP objects, leading to SIGSEGV. Validates the chain from integer overflow to exploitable crash in 32-bit PHP 7.1.

## Requirements

1. Ongoing GDB session from previous debugging
2. PHP with debug symbols
3. Awareness of heap layout in glibc

## Defense

Defensive measures and detection strategies:

- Enable heap canaries and safe unlinking in glibc
- Deploy PHP-FPM with resource limits to kill crashing workers
- Use fuzzing tools like AFL to proactively find such issues

## Objectives

1. Witness buffer overrun during copy operation
2. Observe SIGSEGV from heap corruption
3. Identify corruption patterns for exploitation

## Instructions

### Step 1: Resume Execution

**Context**: Continue from allocation point to reach writing phase.

In GDB: `continue` or `next` through to line 1378.

> Expected: Execution proceeds to string processing loop.

### Step 2: Monitor Writes

**Context**: Inspect memory writes beyond buffer bounds.

Set watchpoint on buffer end: `watch *(char*)buffer + alloc_size`, then continue. Observe writes at line 1378 overflowing.

> Expected: Watchpoint triggers on overrun; heap chunks corrupted.

### Step 3: Capture SIGSEGV

**Context**: Let the fault occur and analyze the crash.

Continue until SIGSEGV; use `bt` for backtrace and `info registers` for state.

> Expected: Segmentation fault due to invalid memory access post-corruption.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GDB]]
- [[tools/PHP]]

## Tags

- [[heap-overflow]]
- [[sigsegv]]
- [[debugging]]
