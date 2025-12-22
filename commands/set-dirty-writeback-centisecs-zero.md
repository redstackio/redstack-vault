---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: set-dirty-writeback-centisecs-zero
type: command
executor: bash
data: echo 0 > /proc/sys/vm/dirty_writeback_centisecs
output: null
created_at: '2023-04-06T03:56:19Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - kernel
  - exploit-prep
verified: true
validated: true
---

# set-dirty-writeback-centisecs-zero

## Command

```bash
echo 0 > /proc/sys/vm/dirty_writeback_centisecs
```

## Description

Sets the Linux kernel's dirty_writeback_centisecs parameter to 0 via /proc filesystem to disable delayed page writeback, stabilizing race conditions for exploits like DirtyCow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `0` | Value to set (disables writeback delay) | Yes |
| `/proc/sys/vm/dirty_writeback_centisecs` | Kernel parameter path | Yes |

## Examples

### Basic Usage

```bash
echo 0 > /proc/sys/vm/dirty_writeback_centisecs
```

### Verify Setting

```bash
cat /proc/sys/vm/dirty_writeback_centisecs
```

## Expected Output

No output on success (silent). Verification shows "0".

## Related

- [[procedures/dirtycow-linux-privilege-escalation]]
- [[commands/compile-dirtycow-exploit]]
