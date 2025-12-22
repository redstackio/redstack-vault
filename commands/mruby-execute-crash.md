---
data: ./dev/bin/mruby crash.rb
tags:
  - execution
type: command
executor: bash
platforms:
  - macOS
id: d789c342-1cf9-4fba-ab40-69fe1377cac4
created_at: '2025-12-11T03:47:48.017Z'
updated_at: '2025-12-11T03:47:48.017Z'
verified: false
validated: true
submitted: true
---
# mruby-execute-crash

## Command

```bash
./dev/bin/mruby crash.rb
```

## Description

Executes a crash script with mruby binary to trigger segmentation fault due to buffer overflow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `crash.rb` | Script file | Yes |

## Examples

### Basic Usage

```bash
./dev/bin/mruby crash.rb
```

## Expected Output

Segmentation fault: 11

## Related

- [[procedures/Execute-mruby-Crash-Script]]
