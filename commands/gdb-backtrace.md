---
data: bt
tags:
  - gdb
  - debugging
type: command
executor: gdb
platforms:
  - Linux
id: 8358a0d4-9394-4807-ae0c-7a3cf441d57f
created_at: '2025-12-11T03:47:48.051Z'
updated_at: '2025-12-11T03:47:48.051Z'
verified: false
validated: true
submitted: true
---
# gdb-backtrace

## Command

```gdb
bt
```

## Description

Prints the backtrace of the call stack in GDB after a crash, showing the sequence of function calls leading to the failure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters | No |

## Examples

### Basic Usage

```gdb
bt
```

## Expected Output

Stack trace showing the assertion failure in mpd_msword and related calls in mruby.

## Related

- [[commands/gdb-attach]]
- [[procedures/Debug-mruby-Crash-with-GDB]]
