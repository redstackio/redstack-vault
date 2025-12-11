---
data: target create "./dev/bin/mruby"
tags:
  - debugging
type: command
executor: lldb
platforms:
  - macOS
id: 46c9fb00-122d-4171-98b9-546f3c0103f5
created_at: '2025-12-11T03:47:48.011Z'
updated_at: '2025-12-11T03:47:48.011Z'
verified: false
validated: true
submitted: true
---
# lldb-target-create

## Command

```bash
target create "./dev/bin/mruby"
```

## Description

Sets the target executable in LLDB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./dev/bin/mruby` | Path to binary | Yes |

## Examples

### Basic Usage

```bash
target create "./dev/bin/mruby"
```

## Expected Output

Current executable set to './dev/bin/mruby' (x86_64).

## Related

- [[procedures/Debug-mruby-Buffer-Overflow-with-LLDB]]
