---
id: cmd-info-eip
data: i r eip
tags:
  - gdb
  - registers
type: command
output: null
executor: gdb
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.176Z'
verified: false
validated: true
submitted: true
---
# info-registers-eip

## Command

```gdb
i r eip
```

## Description

Within a GDB session, displays the current value of the EIP (Instruction Pointer) register, useful for verifying control flow hijacking in exploits like heap overflows.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `i` | Short for 'info' | Yes |
| `r` | Short for 'registers' | Yes |
| `eip` | Specific register to inspect (x86 Instruction Pointer) | Yes |

## Examples

### Basic Usage

```gdb
i r eip
```

### Advanced Usage

```gdb
info registers eip
```
(Full form)

## Expected Output

eip            0x42424242      0x42424242

Indicates EIP overwritten to attacker value.

## Related

- [[commands/gdb-debug-php-script]]
- [[procedures/Debug-and-Demonstrate-EIP-Control-with-GDB]]
