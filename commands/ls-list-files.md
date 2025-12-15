---
id: cmd-ls-001
data: ls -alh
tags:
  - file-listing
type: command
output: |-
  total 2.0M
  -rw-r--r-- 1 user user 990K Oct 1 lorem-1MB
  -rw-r--r-- 1 user user 2.1K nginx.conf
  -rw-r--r-- 1 user user 8.6K validator.yaml
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.392Z'
verified: false
validated: true
submitted: true
---
# ls-list-files

## Command

```bash
ls -alh
```

## Description

Lists directory contents in long format with human-readable sizes, including hidden files, to verify payload file size.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-a` | Include hidden files | No |
| `-l` | Long format | No |
| `-h` | Human-readable sizes | No |

## Examples

### Basic Usage

```bash
ls -alh
```

### Advanced Usage

```bash
ls -alh /path/to/dir
```

## Expected Output

Detailed file listing with sizes, permissions, and dates.

## Related

- [[Related Command: head-display-file-content]]
