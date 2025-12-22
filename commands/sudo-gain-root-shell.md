---
type: command
executor: bash
data: sudo -i
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - sudo
  - root-shell
  - privilege-escalation
verified: true
validated: true
---

# sudo-gain-root-shell

## Command

```bash
sudo -i
```

## Description

Invokes an interactive root shell via sudo without password after successful injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Run command as root with login environment | Yes |

## Examples

### Basic Usage

```bash
sudo -i
```

Follow with `id` to verify root.

## Expected Output

Root shell prompt (`#`) with no password prompt. `id` outputs: `uid=0(root) gid=0(root) groups=0(root)`.

## Related

- [[procedures/Linux-Privilege-Escalation-via-SUDO-Injection]]
