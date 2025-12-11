---
data: ./mruby/bin/mruby crash.rb
tags:
  - testing
type: command
executor: bash
platforms:
  - macOS
id: a7b33321-67af-405d-a58a-0598c16858fb
created_at: '2025-12-11T03:47:47.979Z'
updated_at: '2025-12-11T03:47:47.979Z'
verified: false
validated: true
submitted: true
---
# mruby-patched-execute

## Command

```bash
./mruby/bin/mruby crash.rb
```

## Description

Runs patched mruby on crash script to verify fix.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `crash.rb` | Script file | Yes |

## Examples

### Basic Usage

```bash
./mruby/bin/mruby crash.rb
```

## Expected Output

ArgumentError: out of Time range.

## Related

- [[procedures/Test-Patched-mruby-Version]]
