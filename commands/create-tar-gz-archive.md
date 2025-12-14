---
data: tar -czvf test.tar.gz .
tags:
  - archiving
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-25T00:00:00Z'
updated_at: '2025-12-14T17:24:08.332Z'
id: a2e90334-009b-45c3-a5b1-26f6a935f79e
verified: false
validated: true
submitted: true
---
# create-tar-gz-archive

## Command

```bash
tar -czvf test.tar.gz .
```

## Description

Creates a gzip-compressed tar archive of the current directory, preserving symlinks, for preparing malicious GitLab exports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c` | Create new archive | Yes |
| `-z` | Gzip compression | Yes |
| `-v` | Verbose output | Yes |
| `-f` | Output file (test.tar.gz) | Yes |
| `.` | Current directory contents | Yes |

## Examples

### Basic Usage

```bash
tar -czvf test.tar.gz .
```

### Advanced Usage

```bash
tar -czvf malicious-export.tar.gz --exclude=*.log .
```

## Expected Output

Verbose output showing files added, e.g., 'VERSION
project.json
project.bundle', resulting in test.tar.gz.

## Related

- [[commands/list-directory-with-symlinks]]
