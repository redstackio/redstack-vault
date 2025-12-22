---
id: cmd-005
data: ln -s /suidfs/passwd /usr/bin/setpasswd
tags:
  - symlink
type: command
output: Symlink created
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.211Z'
verified: false
validated: true
submitted: true
---
# ln-symlink-backdoor

## Command

```bash
ln -s /suidfs/passwd /usr/bin/setpasswd
```

## Description

Creates a symbolic link to the setuid binary for easy invocation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /suidfs/passwd | Target | Yes |
| /usr/bin/setpasswd | Symlink path | Yes |

## Examples

### Basic Usage

```bash
ln -s /suidfs/passwd /usr/bin/setpasswd
```

## Expected Output

Symlink established.

## Related

- [[commands/sudo-chmod-setuid-binary]]
