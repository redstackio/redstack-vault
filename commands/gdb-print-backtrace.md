---
id: 6e72b317-0026-48a0-a2d2-71cf6bcc4ecd
name: gdb-print-backtrace
type: command
executor: bash
data: bt
output: null
created_at: '2025-12-11T03:47:39.162Z'
updated_at: '2025-12-11T03:47:39.162Z'
platforms:
  - Linux
tags:
  - debug
  - gdb
verified: false
validated: true
submitted: true
---

# gdb-print-backtrace

## Command

```bash
bt
```

## Description

Prints the backtrace of all stack frames in GDB to analyze the call stack at crash time.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
bt
```

## Expected Output

A stack trace showing the call stack at the time of the crash, including functions like mark_context_stack, incremental_gc, etc.

## Related

- [[procedures/Debug-mruby-Crash-with-GDB]]
- #gdb
