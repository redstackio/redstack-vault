---
id: 55a46bb9-d2b9-47df-b85e-c7392c54b0e7
name: r
type: command
executor: bash
data: r
output: null
created_at: '2025-12-11T03:47:48.126Z'
updated_at: '2025-12-11T03:47:48.126Z'
platforms:
  - macOS
tags:
  - debugging
  - lldb
verified: false
validated: true
submitted: true
---

# r

## Command

```bash
r
```

## Description

Runs the program in lldb to hit the crash point.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
r
```

## Expected Output

Process launched, stops at crash with EXC_BAD_ACCESS.

## Related

- [[procedures/Debug-mruby-Crash-Using-lldb]]
- #lldb
