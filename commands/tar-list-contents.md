---
id: cmd-tar-ztvf
name: tar-list-contents
type: command
executor: bash
data: tar -ztvf export.tar.gz
output: >-
  Detailed listing including drwxr-xr-x ... ./uploads/passwd -> /tmp/passwd with
  size 0
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.188Z'
platforms:
  - Linux
tags:
  - listing
  - tar
  - verification
verified: false
validated: true
submitted: true
---

# tar-list-contents

## Command

```bash
tar -ztvf export.tar.gz
```

## Description

Lists verbose contents of a gzip tar archive, showing permissions, symlinks, and sizes to verify preservation in GitLab export testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| file | Archive path (export.tar.gz) | Yes |
| options | -ztvf for list, gzip, verbose, file | Yes |

## Examples

### Basic Usage

```bash
tar -ztvf export.tar.gz
```

### Advanced Usage

```bash
tar -tvf non-gz.tar
```

## Expected Output

Verbose listing with details like lrwxr-xr-x ... symlink -> target (size 0 for symlinks).

## Related

- [[commands/tar-create-export]]
