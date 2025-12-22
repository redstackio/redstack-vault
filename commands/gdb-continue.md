---
data: c
tags:
  - gdb
  - debugging
type: command
executor: gdb
platforms:
  - Linux
id: 7fd4cc3a-397d-470c-a2bf-f50e0a1b909d
created_at: '2025-12-11T03:47:48.062Z'
updated_at: '2025-12-11T03:47:48.062Z'
verified: false
validated: true
submitted: true
---
# gdb-continue

## Command

```gdb
c
```

## Description

Continues execution of the attached process in GDB until a breakpoint or signal like SIGABRT is hit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters | No |

## Examples

### Basic Usage

```gdb
c
```

## Expected Output

Process continues until it receives SIGABRT or another stopping event.

## Related

- [[commands/gdb-attach]]
- [[procedures/Debug-mruby-Crash-with-GDB]]
