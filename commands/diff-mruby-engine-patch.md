---
data: >-
  diff --git a/ext/mruby_engine/mruby-time/src/time.c
  b/ext/mruby_engine/mruby-time/src/time.c
tags:
  - patching
type: command
executor: bash
platforms:
  - macOS
id: 353ee526-5b10-43bb-9ebe-e34cec23b0ed
created_at: '2025-12-11T03:47:47.976Z'
updated_at: '2025-12-11T03:47:47.976Z'
verified: false
validated: true
submitted: true
---
# diff-mruby-engine-patch

## Command

```bash
diff --git a/ext/mruby_engine/mruby-time/src/time.c b/ext/mruby_engine/mruby-time/src/time.c
```

## Description

Generates diff for mruby-engine patch.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--git` | Git format | Yes |
| `files` | Source files | Yes |

## Examples

### Basic Usage

```bash
diff --git a/ext/mruby_engine/mruby-time/src/time.c b/ext/mruby_engine/mruby-time/src/time.c
```

## Expected Output

Patch content.

## Related

- [[procedures/Reproduce-and-Fix-in-mruby-engine]]
