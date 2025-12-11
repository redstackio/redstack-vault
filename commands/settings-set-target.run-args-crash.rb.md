---
id: 61b9a0ce-bda8-4a87-9cf5-4de3c409a16e
name: settings set -- target.run-args "crash.rb"
type: command
executor: bash
data: settings set -- target.run-args "crash.rb"
output: null
created_at: '2025-12-11T03:47:48.134Z'
updated_at: '2025-12-11T03:47:48.134Z'
platforms:
  - macOS
tags:
  - debugging
  - lldb
verified: false
validated: true
submitted: true
---

# settings set -- target.run-args "crash.rb"

## Command

```bash
settings set -- target.run-args "crash.rb"
```

## Description

Sets the run arguments for the target in lldb.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-- target.run-args` | Specifies run arguments | Yes |
| `"crash.rb"` | The argument value | Yes |

## Examples

### Basic Usage

```bash
settings set -- target.run-args "crash.rb"
```

## Expected Output

None specified, sets the configuration.

## Related

- [[procedures/Debug-mruby-Crash-Using-lldb]]
- #lldb
