---
id: cmd-uuid-3
data: ls -la
tags:
  - verification
  - filesystem
type: command
output: Detailed list of files in the current directory
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.737Z'
verified: false
validated: true
submitted: true
---
# ls-check-files

## Command

```bash
ls -la
```

## Description

Lists all files in the current directory with detailed permissions and timestamps, used to verify presence or absence of the 'HACKED' marker file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Long format listing | Yes |
| `-a` | Include hidden files | Yes |

## Examples

### Basic Usage

```bash
ls -la
```

### Advanced Usage

```bash
ls -la | grep HACKED
```

## Expected Output

total 8
drwxr-xr-x 2 user user 4096 Oct  1 12:00 .
drwxr-xr-x 3 user user 4096 Oct  1 12:00 ..
-rw-r--r-- 1 user user   45 Oct  1 12:00 poc.js
-rw-r--r-- 1 user user    0 Oct  1 12:01 HACKED  (post-exploitation)

## Related

- [[Related Procedure: Verify-Clean-Filesystem-Before-Exploitation]]
- [[Related Procedure: Confirm-RCE-Exploitation-Success]]
