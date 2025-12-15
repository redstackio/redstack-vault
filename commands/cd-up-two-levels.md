---
id: cmd-cd-up-two
name: cd-up-two-levels
type: command
executor: bash
data: cd ../..
output: Current directory changed to /tmp
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.191Z'
platforms:
  - Linux
tags:
  - navigation
  - testing
verified: false
validated: true
submitted: true
---

# cd-up-two-levels

## Command

```bash
cd ../..
```

## Description

Changes directory up two levels (e.g., from /tmp/export/uploads to /tmp) after symlink creation to repackage the export.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| dir | Relative path (../..) | Yes |

## Examples

### Basic Usage

```bash
cd ../..
```

### Advanced Usage

```bash
cd ../../..
```

## Expected Output

Shell prompt updates; verify with pwd showing /tmp.

## Related

- [[commands/create-symlink-passwd]]
