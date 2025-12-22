---
id: cmd-cd-uploads
name: cd-uploads-dir
type: command
executor: bash
data: cd /tmp/export/uploads
output: Current directory changed
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.194Z'
platforms:
  - Linux
tags:
  - navigation
  - testing
verified: false
validated: true
submitted: true
---

# cd-uploads-dir

## Command

```bash
cd /tmp/export/uploads
```

## Description

Changes directory to /tmp/export/uploads to prepare for creating symlinks in GitLab export testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| dir | Target directory (/tmp/export/uploads) | Yes |

## Examples

### Basic Usage

```bash
cd /tmp/export/uploads
```

### Advanced Usage

```bash
cd /path/to/dir
```

## Expected Output

Shell prompt updates to new directory; verify with pwd.

## Related

- [[commands/create-symlink-passwd]]
