---
data: diff --git a/mrbgems/mruby-time/src/time.c b/mrbgems/mruby-time/src/time.c
tags:
  - patching
type: command
executor: bash
platforms:
  - macOS
id: 9b87586e-0e07-4ed6-a941-7ccb61803c39
created_at: '2025-12-11T03:47:47.982Z'
updated_at: '2025-12-11T03:47:47.982Z'
verified: false
validated: true
submitted: true
---
# diff-mruby-patch

## Command

```bash
diff --git a/mrbgems/mruby-time/src/time.c b/mrbgems/mruby-time/src/time.c
```

## Description

Generates diff for mruby patch adding range checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--git` | Git format | Yes |
| `a/mrbgems/mruby-time/src/time.c` | Original file | Yes |
| `b/mrbgems/mruby-time/src/time.c` | Modified file | Yes |

## Examples

### Basic Usage

```bash
diff --git a/mrbgems/mruby-time/src/time.c b/mrbgems/mruby-time/src/time.c
```

## Expected Output

Patch content adding range check.

## Related

- [[procedures/Apply-mruby-Buffer-Overflow-Patch]]
