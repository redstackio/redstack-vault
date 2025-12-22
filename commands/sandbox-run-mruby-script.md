---
id: 71c63394-ff73-42cc-b57e-f0d6cecd823b
name: sandbox-run-mruby-script
type: command
executor: bash
data: bin/sandbox new_crashes/fixnum_exception.mrb
output: null
created_at: '2025-12-11T03:47:39.176Z'
updated_at: '2025-12-11T03:47:39.176Z'
platforms:
  - Linux
tags:
  - mruby
  - sandbox
verified: false
validated: true
submitted: true
---

# sandbox-run-mruby-script

## Command

```bash
bin/sandbox new_crashes/fixnum_exception.mrb
```

## Description

Runs an mruby script in a sandboxed environment to test and observe crashes safely, used for reproducing vulnerabilities like the NoMethodError overwrite.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `file` | The script file to execute (e.g., new_crashes/fixnum_exception.mrb) | Yes |

## Examples

### Basic Usage

```bash
bin/sandbox new_crashes/fixnum_exception.mrb
```

### Advanced Usage

```bash
bin/sandbox --verbose new_crashes/fixnum_exception.mrb
```

## Expected Output

[BUG] Segmentation fault and backtrace, or MRubyEngine::EngineTimeQuotaError

## Related

- [[procedures/Execute-mruby-Script-in-Sandbox]]
- #sandbox
