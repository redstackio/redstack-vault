---
data: p *d
tags:
  - debugging
type: command
executor: lldb
platforms:
  - macOS
id: 035409d7-8f9f-4246-8102-c65a076c4c46
created_at: '2025-12-11T03:47:47.984Z'
updated_at: '2025-12-11T03:47:47.984Z'
verified: false
validated: true
submitted: true
---
# lldb-print-d

## Command

```bash
p *d
```

## Description

Prints the contents of d (datetime) struct in LLDB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `*d` | Dereference d pointer | Yes |

## Examples

### Basic Usage

```bash
p *d
```

## Expected Output

Struct values with invalid fields.

## Related

- [[procedures/Debug-mruby-Buffer-Overflow-with-LLDB]]
