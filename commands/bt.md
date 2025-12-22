---
id: 3be18715-c0cb-4e3d-9fb9-e016ed532190
name: bt
type: command
executor: bash
data: bt
output: null
created_at: '2025-12-11T03:47:48.117Z'
updated_at: '2025-12-11T03:47:48.117Z'
platforms:
  - macOS
tags:
  - debugging
  - lldb
verified: false
validated: true
submitted: true
---

# bt

## Command

```bash
bt
```

## Description

Displays the backtrace in lldb after a crash.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
bt
```

## Expected Output

Backtrace showing crash in ary_concat and call stack.

## Related

- [[procedures/Debug-mruby-Crash-Using-lldb]]
- #lldb
