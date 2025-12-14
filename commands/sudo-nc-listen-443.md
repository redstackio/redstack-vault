---
id: cmd-uuid-001
data: sudo nc -nvlp 443
tags:
  - listener
  - reverse-shell
type: command
output: 'Listening on [0.0.0.0] (family 0, port 443)'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.867Z'
verified: false
validated: true
submitted: true
---
# sudo-nc-listen-443

## Command

```bash
sudo nc -nvlp 443
```

## Description

Starts a Netcat TCP listener on port 443 as root, used to receive reverse shells without DNS resolution and with verbose output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | No DNS resolution | Yes |
| `-v` | Verbose output | Yes |
| `-l` | Listen mode | Yes |
| `p 443` | Port 443 | Yes |

## Examples

### Basic Usage

```bash
sudo nc -nvlp 443
```

### Advanced Usage

```bash
sudo nc -nvlp 4444 -s 0.0.0.0
```

## Expected Output

"Listening on [0.0.0.0] (family 0, port 443)" followed by connection details upon incoming shell.

## Related

- [[commands/bash-reverse-shell]]
- [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]
