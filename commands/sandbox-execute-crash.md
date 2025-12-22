---
data: ./bin/sandbox crash.rb
tags:
  - execution
type: command
executor: bash
platforms:
  - macOS
id: f203c2de-bf41-4490-b093-53a0720a2c32
created_at: '2025-12-11T03:47:47.978Z'
updated_at: '2025-12-11T03:47:47.978Z'
verified: false
validated: true
submitted: true
---
# sandbox-execute-crash

## Command

```bash
./bin/sandbox crash.rb
```

## Description

Runs crash script in mruby-engine sandbox.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `crash.rb` | Script file | Yes |

## Examples

### Basic Usage

```bash
./bin/sandbox crash.rb
```

## Expected Output

Segmentation fault or EngineRuntimeError in patched version.

## Related

- [[procedures/Reproduce-and-Fix-in-mruby-engine]]
