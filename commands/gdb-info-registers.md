---
data: info registers
tags:
  - gdb
  - debugging
type: command
executor: gdb
platforms:
  - Linux
id: 6582b1d5-0da5-4a5c-9572-2a4e534798c5
created_at: '2025-12-11T03:47:48.048Z'
updated_at: '2025-12-11T03:47:48.048Z'
verified: false
validated: true
submitted: true
---
# gdb-info-registers

## Command

```gdb
info registers
```

## Description

Displays the current values of CPU registers in GDB at the time of crash, useful for low-level analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters | No |

## Examples

### Basic Usage

```gdb
info registers
```

## Expected Output

List of register values like rax=0x0, rbx=0x7ffff7f9b000, etc.

## Related

- [[commands/gdb-attach]]
- [[procedures/Debug-mruby-Crash-with-GDB]]
