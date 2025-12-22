---
data: p *tm
tags:
  - debugging
type: command
executor: lldb
platforms:
  - macOS
id: 4c99f96c-c905-426a-97c6-18433bb4b700
created_at: '2025-12-11T03:47:47.987Z'
updated_at: '2025-12-11T03:47:47.987Z'
verified: false
validated: true
submitted: true
---
# lldb-print-tm

## Command

```bash
p *tm
```

## Description

Prints the contents of tm struct in LLDB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `*tm` | Dereference tm pointer | Yes |

## Examples

### Basic Usage

```bash
p *tm
```

## Expected Output

Struct values showing invalid tm_mon=6484120.

## Related

- [[procedures/Debug-mruby-Buffer-Overflow-with-LLDB]]
