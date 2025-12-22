---
id: 0912be57-4917-4621-a0e0-8fe11500d515
name: >-
  diff --git a/mrbgems/mruby-compiler/core/codegen.c
  b/mrbgems/mruby-compiler/core/codegen.c
type: command
executor: bash
data: >-
  diff --git a/mrbgems/mruby-compiler/core/codegen.c
  b/mrbgems/mruby-compiler/core/codegen.c
output: null
created_at: '2025-12-11T03:47:48.104Z'
updated_at: '2025-12-11T03:47:48.104Z'
platforms:
  - macOS
tags:
  - patch
  - diff
verified: false
validated: true
submitted: true
---

# diff --git a/mrbgems/mruby-compiler/core/codegen.c b/mrbgems/mruby-compiler/core/codegen.c

## Command

```bash
diff --git a/mrbgems/mruby-compiler/core/codegen.c b/mrbgems/mruby-compiler/core/codegen.c
```

## Description

Shows the difference (patch) for fixing the bug in codegen.c by modifying stack push conditions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--git` | Git format | Yes |
| `a/mrbgems/...` | Original file | Yes |
| `b/mrbgems/...` | Modified file | Yes |

## Examples

### Basic Usage

```bash
diff --git a/mrbgems/mruby-compiler/core/codegen.c b/mrbgems/mruby-compiler/core/codegen.c
```

## Expected Output

The patch content showing changes to conditionally push to stack.

## Related

- #mruby
