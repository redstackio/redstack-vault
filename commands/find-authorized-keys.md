---
data: find . -name 'authorized_keys'
tags:
  - find
  - search
type: command
executor: bash
platforms:
  - Linux
id: a21f38db-97c7-414b-9b50-052b2b703e52
created_at: '2025-12-11T03:47:39.632Z'
updated_at: '2025-12-11T03:47:39.632Z'
verified: false
validated: true
submitted: true
---
# find-authorized-keys

## Command

```bash
find . -name 'authorized_keys'
```

## Description

Searches for files named authorized_keys starting from current directory, used to verify uploaded file location.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `.` | Current directory | Yes |
| `-name 'authorized_keys'` | Search criteria | Yes |

## Examples

### Basic Usage

```bash
find /path -name 'file'
```

## Expected Output

Paths to matching files, e.g., /var/opt/gitlab/.ssh/authorized_keys.

## Related

- [[procedures/Verify-Exploitation-with-Docker]]
- #find
