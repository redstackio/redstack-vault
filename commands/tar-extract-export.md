---
id: cmd-tar-xzf-export
name: tar-extract-export
type: command
executor: bash
data: >-
  tar -xzf ~/Downloads/2016-08-12_09-34-826_gitlab-org_gitlab-test_export.tar.gz
  -C /tmp/export
output: 'Files extracted including project.bundle, project.json, etc.'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.204Z'
platforms:
  - Linux
tags:
  - extraction
  - tar
  - gitlab
verified: false
validated: true
submitted: true
---

# tar-extract-export

## Command

```bash
tar -xzf ~/Downloads/2016-08-12_09-34-826_gitlab-org_gitlab-test_export.tar.gz -C /tmp/export
```

## Description

Extracts the specified GitLab export .tar.gz file to /tmp/export directory for inspection of contents like project.json in symlink or token extraction tests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| file | Input archive path | Yes |
| dir | Output directory (-C /tmp/export) | Yes |
| options | -xzf for extract, gzip, file | Yes |

## Examples

### Basic Usage

```bash
tar -xzf export.tar.gz -C /tmp/export
```

### Advanced Usage

```bash
tar -xzf large_export.tar.gz -C ./extracted
```

## Expected Output

Files extracted silently; verify with ls /tmp/export showing project.json, etc.

## Related

- [[commands/list-recent-downloads]]
