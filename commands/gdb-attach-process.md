---
id: d708c53e-d3df-45cf-95eb-388dac99feda
name: gdb-attach-process
type: command
executor: bash
data: gdb attach 5534
output: null
created_at: '2025-12-11T03:47:39.170Z'
updated_at: '2025-12-11T03:47:39.170Z'
platforms:
  - Linux
tags:
  - debug
  - gdb
verified: false
validated: true
submitted: true
---

# gdb-attach-process

## Command

```bash
gdb attach 5534
```

## Description

Attaches the GDB debugger to a running process by PID to inspect and debug crashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `attach` | The process ID to attach to (e.g., 5534) | Yes |

## Examples

### Basic Usage

```bash
gdb attach 5534
```

## Expected Output

Attaches to the process and pauses execution

## Related

- [[procedures/Debug-mruby-Crash-with-GDB]]
- #gdb
