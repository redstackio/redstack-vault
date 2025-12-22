---
data: register read
tags:
  - debugging
type: command
executor: lldb
platforms:
  - macOS
id: 25a17d79-d6dc-4078-bd14-ce17d272ef1c
created_at: '2025-12-11T03:47:47.994Z'
updated_at: '2025-12-11T03:47:47.994Z'
verified: false
validated: true
submitted: true
---
# lldb-register-read

## Command

```bash
register read
```

## Description

Reads general purpose registers in LLDB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```bash
register read
```

## Expected Output

Register values at crash time.

## Related

- [[procedures/Debug-mruby-Buffer-Overflow-with-LLDB]]
