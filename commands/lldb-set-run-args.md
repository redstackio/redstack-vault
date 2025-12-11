---
data: settings set -- target.run-args "crash.rb"
tags:
  - debugging
type: command
executor: lldb
platforms:
  - macOS
id: af3b2d12-366c-44bf-96b3-ddad57d4466f
created_at: '2025-12-11T03:47:48.006Z'
updated_at: '2025-12-11T03:47:48.006Z'
verified: false
validated: true
submitted: true
---
# lldb-set-run-args

## Command

```bash
settings set -- target.run-args "crash.rb"
```

## Description

Sets run arguments for the target in LLDB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `crash.rb` | Argument | Yes |

## Examples

### Basic Usage

```bash
settings set -- target.run-args "crash.rb"
```

## Expected Output

None (configuration command).

## Related

- [[procedures/Debug-mruby-Buffer-Overflow-with-LLDB]]
