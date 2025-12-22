---
data: mruby crash.rb
tags:
  - mruby
  - execution
type: command
executor: bash
platforms:
  - mruby
id: d545c4ef-0a03-4f43-9519-f5031f0a2ce6
created_at: '2025-12-11T03:47:47.906Z'
updated_at: '2025-12-11T03:47:47.906Z'
verified: false
validated: true
submitted: true
---
# mruby-run-script

## Command

```bash
mruby crash.rb
```

## Description

Runs a Ruby script using the mruby interpreter, used to trigger the segmentation fault vulnerability when the script contains a method call with exactly 127 arguments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `crash.rb` | The script file containing the method call with 127 arguments | Yes |

## Examples

### Basic Usage

```bash
mruby crash.rb
```

## Expected Output

Segmentation fault

## Related

- [[commands/sandbox-run-script]]
- [[procedures/Execute-mruby-Crash-Script]]
