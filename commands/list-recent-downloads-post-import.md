---
id: cmd-ls-recent-post-import
name: list-recent-downloads-post-import
type: command
executor: bash
data: ls -t ~/Downloads/ | head -1
output: >-
  Newest imported export, e.g.,
  2016-08-12_09-45-747_root_test-uploads_export.tar.gz
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.186Z'
platforms:
  - Linux
tags:
  - file-locating
  - downloads
  - post-import
verified: false
validated: true
submitted: true
---

# list-recent-downloads-post-import

## Command

```bash
ls -t ~/Downloads/ | head -1
```

## Description

Lists the newest file in ~/Downloads after GitLab import to locate the re-exported archive for symlink status check.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| dir | ~/Downloads/ | Yes |
| sort | -t | Yes |
| limit | head -1 | Yes |

## Examples

### Basic Usage

```bash
ls -t ~/Downloads/ | head -1
```

### Advanced Usage

```bash
ls -t ~/Downloads/ | head -3
```

## Expected Output

Newest file name, e.g., post-import export.tar.gz.

## Related

- [[commands/tar-list-post-import]]
