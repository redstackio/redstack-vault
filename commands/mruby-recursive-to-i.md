---
id: a1f2d27f-2ad8-420c-a29b-738a189fa55b
name: mruby-recursive-to-i
type: command
executor: bash
data: mruby recursive_to_i.rb
output: null
created_at: '2025-12-11T03:47:47.940Z'
updated_at: '2025-12-11T03:47:47.940Z'
platforms:
  - Linux
  - macOS
tags:
  - mruby
  - exploit
verified: false
validated: true
submitted: true
---

# mruby-recursive-to-i

## Command

```bash
mruby recursive_to_i.rb
```

## Description

Runs the recursive_to_i.rb script using the mruby interpreter to trigger a C-level stack overflow and segmentation fault, demonstrating the vulnerability in vanilla mruby.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `recursive_to_i.rb` | The script file to execute | Yes |

## Examples

### Basic Usage

```bash
mruby recursive_to_i.rb
```

## Expected Output

Segmentation fault due to process stack overflow.

## Related

- [[procedures/Execute-Script-in-mruby-to-Trigger-Stack-Overflow]]
- #mruby
