---
id: cmd-004
data: sudo chmod 04755 /suidfs/passwd
tags:
  - permissions
type: command
output: Permissions set to 4755
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.213Z'
verified: false
validated: true
submitted: true
---
# sudo-chmod-setuid-binary

## Command

```bash
sudo chmod 04755 /suidfs/passwd
```

## Description

Sets setuid bit and permissions on the binary (owner rwx, group rx, others rx).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 04755 | Setuid permissions | Yes |
| /suidfs/passwd | Target file | Yes |

## Examples

### Basic Usage

```bash
sudo chmod 04755 /suidfs/passwd
```

## Expected Output

Mode updated to 4755.

## Related

- [[commands/sudo-chown-root-binary]]
