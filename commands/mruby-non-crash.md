---
data: mruby non-crash.rb
tags:
  - mruby
  - test
type: command
executor: bash
platforms:
  - Linux
id: df92b8f1-d064-4c72-a103-e59b15f32f43
created_at: '2025-12-11T03:47:47.869Z'
updated_at: '2025-12-11T03:47:47.869Z'
verified: false
validated: true
submitted: true
---
# mruby-non-crash

## Command

```bash
mruby non-crash.rb
```

## Description

Runs a similar non-crashing script with lowercase variable to compare behavior and highlight bug specificity to constants.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `non-crash.rb` | File with lowercase variable instead of constant | Yes |

## Examples

### Basic Usage

```bash
mruby non-crash.rb
```

## Expected Output

No crash

## Related

- [[commands/mruby-crash]]
- [[procedures/Execute-and-Analyze-Crashing-Code-in-mruby]]
