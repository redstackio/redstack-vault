---
id: c60ccd42-25e6-4de1-a88a-9462672b157b
name: target create "./dev/bin/mruby"
type: command
executor: bash
data: target create "./dev/bin/mruby"
output: null
created_at: '2025-12-11T03:47:48.140Z'
updated_at: '2025-12-11T03:47:48.140Z'
platforms:
  - macOS
tags:
  - debugging
  - lldb
verified: false
validated: true
submitted: true
---

# target create "./dev/bin/mruby"

## Command

```bash
target create "./dev/bin/mruby"
```

## Description

Creates the target executable in lldb for debugging.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./dev/bin/mruby` | The target executable | Yes |

## Examples

### Basic Usage

```bash
target create "./dev/bin/mruby"
```

## Expected Output

Current executable set to './dev/bin/mruby' (x86_64).

## Related

- [[procedures/Debug-mruby-Crash-Using-lldb]]
- #lldb
