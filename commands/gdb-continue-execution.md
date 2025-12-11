---
id: 904e30f4-7111-447e-828c-01dc0ff113e3
name: gdb-continue-execution
type: command
executor: bash
data: c
output: null
created_at: '2025-12-11T03:47:39.165Z'
updated_at: '2025-12-11T03:47:39.165Z'
platforms:
  - Linux
tags:
  - debug
  - gdb
verified: false
validated: true
submitted: true
---

# gdb-continue-execution

## Command

```bash
c
```

## Description

Continues execution in GDB after attaching, allowing the program to run until a signal or breakpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
c
```

## Expected Output

Continues the program until a signal or breakpoint, in this case leading to SIGSEGV

## Related

- [[procedures/Debug-mruby-Crash-with-GDB]]
- #gdb
