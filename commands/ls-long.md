---
data: ls -l
tags:
  - verification
  - file-listing
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.207Z'
id: 6c47fa13-21d0-43f8-abe9-0304226aea3a
verified: false
validated: true
submitted: true
---
# ls-long

## Command

```bash
ls -l
```

## Description

Lists directory contents in long format, showing permissions, ownership, sizes, and types, used to verify setup and post-exploitation changes like symlink targets and file sizes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l | Long format listing | Yes |

## Examples

### Basic Usage

```bash
ls -l
```

### Specific Directory

```bash
ls -l /path/to/dir
```

## Expected Output

Detailed listing, e.g., lrwxrwxrwx 1 user user 4 Oct 1 12:00 a -> flag\ndrwxr-xr-x 2 user user 4096 Oct 1 12:00 b\n-rw-r--r-- 1 root root 131 Oct 1 12:01 flag. Post-exploit, 'flag' size increases to ~131 bytes.

## Related

- [[commands/cat-flag]]
- [[procedures/Verify-Exploitation-Outcome]]
