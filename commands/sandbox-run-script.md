---
data: sandbox crash.rb
tags:
  - sandbox
  - execution
type: command
executor: bash
platforms:
  - mruby
id: 9bba920d-c766-46e9-860b-db01ace18bb4
created_at: '2025-12-11T03:47:47.901Z'
updated_at: '2025-12-11T03:47:47.902Z'
verified: false
validated: true
submitted: true
---
# sandbox-run-script

## Command

```bash
sandbox crash.rb
```

## Description

Runs a Ruby script in a sandboxed mruby environment, triggering the segmentation fault when the script has a method call with 127 arguments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `crash.rb` | The script file containing the method call with 127 arguments | Yes |

## Examples

### Basic Usage

```bash
sandbox crash.rb
```

## Expected Output

Segmentation fault

## Related

- [[commands/mruby-run-script]]
- [[procedures/Execute-mruby-Crash-Script]]
