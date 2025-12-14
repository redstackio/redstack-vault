---
id: cmd-sudo-elevate-001
data: sudo -n -i
tags:
  - privilege-escalation
  - sudo
type: command
output: 'root@edgeos:~#'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:27.920Z'
verified: false
validated: true
submitted: true
---
# sudo-root-elevate

## Command

```bash
sudo -n -i
```

## Description

Attempts non-interactive root elevation using hijacked session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | Non-interactive | Yes |
| `-i` | Interactive shell | Yes |

## Examples

### Basic Usage

```bash
sudo -n -i
```

### Advanced Usage

```bash
sudo -n -u root /bin/bash
```

## Expected Output

Root shell prompt.

## Related

- [[commands/cat-proc-env]]
