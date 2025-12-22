---
data: mruby larger.rb
tags:
  - mruby
  - test
type: command
executor: bash
platforms:
  - Linux
id: 0f06506e-cb2b-4adb-94cd-05588f911db5
created_at: '2025-12-11T03:47:47.864Z'
updated_at: '2025-12-11T03:47:47.864Z'
verified: false
validated: true
submitted: true
---
# mruby-larger

## Command

```bash
mruby larger.rb
```

## Description

Runs a script with multiple break statements to demonstrate larger invalid jump offsets in bytecode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `larger.rb` | File with multiple break statements | Yes |

## Examples

### Basic Usage

```bash
mruby larger.rb
```

## Expected Output

Bytecode with larger invalid OP_JMP

## Related

- [[commands/mruby-crash]]
- [[procedures/Execute-and-Analyze-Crashing-Code-in-mruby]]
