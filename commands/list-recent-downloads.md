---
id: cmd-ls-recent-downloads
name: list-recent-downloads
type: command
executor: bash
data: ls -t ~/Downloads/ | head -1
output: 'Newest file, e.g., 2016-08-12_09-34-826_gitlab-org_gitlab-test_export.tar.gz'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.209Z'
platforms:
  - Linux
tags:
  - file-locating
  - downloads
verified: false
validated: true
submitted: true
---

# list-recent-downloads

## Command

```bash
ls -t ~/Downloads/ | head -1
```

## Description

Lists files in ~/Downloads sorted by modification time (newest first) and shows the first one to locate the most recent GitLab export file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| dir | Directory to list (~/Downloads/) | Yes |
| sort | -t for time sort | Yes |
| limit | head -1 for first | Yes |

## Examples

### Basic Usage

```bash
ls -t ~/Downloads/ | head -1
```

### Advanced Usage

```bash
ls -t ~/Downloads/ | head -5
```

## Expected Output

Name of newest file, e.g., export.tar.gz.

## Related

- [[commands/tar-extract-export]]
