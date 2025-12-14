---
id: cmd-uuid-003
data: ln -s /etc/passwd passwdsym
tags:
  - symlink
  - linux
type: command
output: No output on success; creates the symlink in the current directory
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.367Z'
verified: false
validated: true
submitted: true
---
# ln-create-symlink-passwd

## Command

```bash
ln -s /etc/passwd passwdsym
```

## Description

Creates a symbolic link named 'passwdsym' pointing to /etc/passwd.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Symbolic link mode | Yes |
| `/etc/passwd` | Target file | Yes |
| `passwdsym` | Link name | Yes |

## Examples

### Basic Usage

```bash
ln -s /etc/passwd passwdsym
```

### Advanced Usage

```bash
ln -s /etc/shadow sensitive
```

## Expected Output

(Silent on success)

## Related

- [[commands/curl-access-symlink]]
- [[procedures/Create-Symlink-to-Sensitive-File]]
