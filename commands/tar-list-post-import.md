---
id: cmd-tar-tzvf-post-import
name: tar-list-post-import
type: command
executor: bash
data: tar -tzvf ~/Downloads/2016-08-12_09-45-747_root_test-uploads_export.tar.gz
output: Listing showing lrwxr-xr-x ... ./uploads/passwd -> /tmp/passwd with size 0
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.184Z'
platforms:
  - Linux
tags:
  - listing
  - tar
  - post-import
verified: false
validated: true
submitted: true
---

# tar-list-post-import

## Command

```bash
tar -tzvf ~/Downloads/2016-08-12_09-45-747_root_test-uploads_export.tar.gz
```

## Description

Lists verbose contents of the post-import exported archive to confirm symlinks are preserved but not dereferenced (size 0).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| file | Archive path | Yes |
| options | -tzvf | Yes |

## Examples

### Basic Usage

```bash
tar -tzvf post_import.tar.gz
```

### Advanced Usage

```bash
tar -tvf non-gz.tar
```

## Expected Output

Detailed listing with symlinks shown as size 0, e.g., lrwxr-xr-x -> /tmp/passwd.

## Related

- [[commands/list-recent-downloads-post-import]]
