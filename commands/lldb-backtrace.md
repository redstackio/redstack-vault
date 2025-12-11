---
data: bt
tags:
  - debugging
type: command
executor: lldb
platforms:
  - macOS
id: 7ccc2a4c-98e4-40b9-870f-f71418af7cf0
created_at: '2025-12-11T03:47:47.996Z'
updated_at: '2025-12-11T03:47:47.996Z'
verified: false
validated: true
submitted: true
---
# lldb-backtrace

## Command

```bash
bt
```

## Description

Prints backtrace in LLDB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
bt
```

## Expected Output

Stack trace showing crash in strlen from mrb_time_asctime.

## Related

- [[procedures/Debug-mruby-Buffer-Overflow-with-LLDB]]
