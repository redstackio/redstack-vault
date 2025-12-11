---
id: 8a807f1c-5a29-4c05-a783-b743cbdc9f9d
name: sandbox-recursive-to-i
type: command
executor: bash
data: sandbox recursive_to_i.rb
output: null
created_at: '2025-12-11T03:47:47.934Z'
updated_at: '2025-12-11T03:47:47.934Z'
platforms:
  - Linux
  - macOS
tags:
  - sandbox
  - exploit
verified: false
validated: true
submitted: true
---

# sandbox-recursive-to-i

## Command

```bash
sandbox recursive_to_i.rb
```

## Description

Executes the recursive_to_i.rb script in the mruby-engine sandbox to trigger stack overflow, showing the vulnerability in a restricted environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `recursive_to_i.rb` | The script file to execute | Yes |

## Examples

### Basic Usage

```bash
sandbox recursive_to_i.rb
```

## Expected Output

Segmentation fault due to process stack overflow.

## Related

- [[procedures/Execute-Script-in-mruby-to-Trigger-Stack-Overflow]]
- #sandbox
