---
id: cmd-tar-czf-export
name: tar-create-export
type: command
executor: bash
data: tar -czf export.tar.gz -C ./export .
output: Archive created with symlinked files
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.189Z'
platforms:
  - Linux
tags:
  - archiving
  - tar
  - testing
verified: false
validated: true
submitted: true
---

# tar-create-export

## Command

```bash
tar -czf export.tar.gz -C ./export .
```

## Description

Creates a gzip-compressed tar archive of ./export contents, including symlinks, for upload and import testing in GitLab.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| output | Archive name (export.tar.gz) | Yes |
| dir | Source dir (-C ./export) | Yes |
| options | -czf for create, gzip, file | Yes |

## Examples

### Basic Usage

```bash
tar -czf export.tar.gz -C ./export .
```

### Advanced Usage

```bash
tar -czf modified.tar.gz -C /tmp/dir .
```

## Expected Output

Archive created; verify with ls -l export.tar.gz.

## Related

- [[commands/tar-list-contents]]
