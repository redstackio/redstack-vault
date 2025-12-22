---
data: lldb ./dev/bin/mruby crash.rb
tags:
  - debugging
type: command
executor: bash
platforms:
  - macOS
id: 6a2fc4dc-bbba-4abe-aa76-7f61e1a809fe
created_at: '2025-12-11T03:47:48.014Z'
updated_at: '2025-12-11T03:47:48.014Z'
verified: false
validated: true
submitted: true
---
# lldb-launch-mruby

## Command

```bash
lldb ./dev/bin/mruby crash.rb
```

## Description

Launches LLDB debugger on mruby with the crash script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./dev/bin/mruby` | mruby binary | Yes |
| `crash.rb` | Script | Yes |

## Examples

### Basic Usage

```bash
lldb ./dev/bin/mruby crash.rb
```

## Expected Output

Debugger session showing process launch and crash.

## Related

- [[procedures/Debug-mruby-Buffer-Overflow-with-LLDB]]
