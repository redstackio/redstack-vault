---
id: 27844d19-421b-47a1-9165-50e7c97f17eb
name: lldb ./dev/bin/mruby crash.rb
type: command
executor: bash
data: lldb ./dev/bin/mruby crash.rb
output: null
created_at: '2025-12-11T03:47:48.202Z'
updated_at: '2025-12-11T03:47:48.202Z'
platforms:
  - macOS
tags:
  - debugging
  - lldb
verified: false
validated: true
submitted: true
---

# lldb ./dev/bin/mruby crash.rb

## Command

```bash
lldb ./dev/bin/mruby crash.rb
```

## Description

Starts the lldb debugger with mruby and the crash script for analyzing the segmentation fault.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./dev/bin/mruby` | The executable | Yes |
| `crash.rb` | The argument (script) | Yes |

## Examples

### Basic Usage

```bash
lldb ./dev/bin/mruby crash.rb
```

## Expected Output

Sets up the debugging session.

## Related

- [[procedures/Debug-mruby-Crash-Using-lldb]]
- #lldb
