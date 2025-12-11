---
data: mruby crash.rb
tags:
  - mruby
  - crash
type: command
executor: bash
platforms:
  - Linux
id: c38745bc-8768-4a53-8492-f60b32954b9c
created_at: '2025-12-11T03:47:47.874Z'
updated_at: '2025-12-11T03:47:47.874Z'
verified: false
validated: true
submitted: true
---
# mruby-crash

## Command

```bash
mruby crash.rb
```

## Description

Runs a crashing Ruby script using the mruby interpreter to reproduce a segmentation fault due to invalid bytecode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `crash.rb` | File containing invalid Ruby code | Yes |

## Examples

### Basic Usage

```bash
mruby crash.rb
```

## Expected Output

Segmentation fault

## Related

- [[commands/sandbox-crash]]
- [[procedures/Execute-and-Analyze-Crashing-Code-in-mruby]]
