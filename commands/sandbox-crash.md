---
data: sandbox crash.rb
tags:
  - sandbox
  - crash
type: command
executor: bash
platforms:
  - Linux
id: 4d0f6566-fec0-423c-ad4e-d163024cece0
created_at: '2025-12-11T03:47:47.872Z'
updated_at: '2025-12-11T03:47:47.872Z'
verified: false
validated: true
submitted: true
---
# sandbox-crash

## Command

```bash
sandbox crash.rb
```

## Description

Runs a crashing Ruby script in the sandbox environment to reproduce segmentation fault, affecting parent MRI VM.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `crash.rb` | File containing invalid Ruby code | Yes |

## Examples

### Basic Usage

```bash
sandbox crash.rb
```

## Expected Output

Segmentation fault

## Related

- [[commands/mruby-crash]]
- [[procedures/Execute-and-Analyze-Crashing-Code-in-mruby]]
