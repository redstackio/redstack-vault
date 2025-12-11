---
id: dc66efc9-7b72-40e2-9428-bf7a4f4ec3ca
name: register read
type: command
executor: bash
data: register read
output: null
created_at: '2025-12-11T03:47:48.113Z'
updated_at: '2025-12-11T03:47:48.113Z'
platforms:
  - macOS
tags:
  - debugging
  - lldb
verified: false
validated: true
submitted: true
---

# register read

## Command

```bash
register read
```

## Description

Reads and displays general purpose registers in lldb.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
register read
```

## Expected Output

Values of registers like rax, rbx, etc.

## Related

- [[procedures/Debug-mruby-Crash-Using-lldb]]
- #lldb
