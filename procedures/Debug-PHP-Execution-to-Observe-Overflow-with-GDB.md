---
id: proc-debug-php-gdb
tags:
  - gdb
  - debugging
  - memory-analysis
type: procedure
tools:
  - '[[tools/GDB]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - 32-bit
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Discovery]]'
updated_at: '2025-12-14T17:28:20.130Z'
skill_level: advanced
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Process Discovery]]'
---
# Debug-PHP-Execution-to-Observe-Overflow-with-GDB

## Summary

This procedure uses GDB to debug a PHP process executing the vulnerable script, setting breakpoints to inspect the integer overflow in allocation and observe the heap write overflow leading to SIGSEGV.

## Description

In a 32-bit Linux setup with PHP 7.1, attach GDB to PHP running the test script. Break at ext/pgsql/pgsql.c:4384 to see overflowed size (0x10 bytes), then continue to PQescapeStringInternal in libpq.so.5 where large writes cause fault, revealing memory corruption for exploitation planning.

## Requirements

1. GDB installed on 32-bit Linux
2. PHP compiled with debug symbols
3. Test script from prior procedure

## Defense

Defensive measures and detection strategies:

- Use address sanitizers (ASan) in PHP builds to detect overflows at runtime
- Log debugger attachments or unusual process signals (SIGSEGV)
- Deploy heap integrity checks in production

## Objectives

1. Visualize allocation overflow in registers
2. Trace write operations causing corruption
3. Gather data for exploit development

## Instructions

### Step 1: Prepare and Run Under GDB

**Context**: Launch PHP in GDB with the script.

```bash
gdb --args php test_overflow.php
```

> Starts GDB with PHP and arguments.

### Step 2: Set Breakpoint and Inspect

**Context**: Break at vulnerable line and examine.

In GDB:

```gdb
break ext/pgsql/pgsql.c:4384
run
info registers
x/10x $esp
continue
```

> Breakpoint at allocation; run shows overflow ((0x7fffffff * 2 + 0x14) & 0xfffffffc = 0x10); inspect stack; continue to SIGSEGV in libpq.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Process Discovery]] Process Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GDB]]
- [[tools/PHP]]

## Tags

- gdb
- debugging
- memory-analysis
