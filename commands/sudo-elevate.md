---
data: sudo -i
tags:
  - privilege-escalation
  - sudo
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.536Z'
id: 61521c3f-64ac-4060-9378-eb175017d854
verified: false
validated: true
submitted: true
---
# sudo-elevate

## Command

```bash
sudo -i
```

## Description

Elevates the current user to root privileges using sudo with interactive shell, exploiting configurations allowing passwordless access. Used in privilege escalation scenarios where direct calls are bypassed via file modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Start an interactive root shell | No |

## Examples

### Basic Usage

```bash
sudo -i
```

### Advanced Usage

```bash
sudo -i -u root /bin/bash
```

## Expected Output

A root shell prompt (e.g., root@deck:~#), granting full administrative access.

## Related

- [[Related Procedure|procedures/Steam-Deck-Privilege-Escalation-via-Bashrc-Modification]]
