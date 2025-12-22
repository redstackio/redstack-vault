---
id: 42f68627-7e7f-46c7-b4fe-10cb66b6051b
name: socat-tcp-listener-on-port
type: command
executor: bash
data: 'socat file:`tty`,raw,echo=0 tcp-listen:$_PORT'
output: null
created_at: '2023-04-06T03:56:24.983692+00:00'
updated_at: '2023-04-10T20:25:31.247390+00:00'
platforms:
  - Linux
  - Unix
tags:
  - socat
  - listener
  - tty
  - reverse-shell
verified: true
validated: true
---

# socat-tcp-listener-on-port

## Command

```bash
socat file:`tty`,raw,echo=0 tcp-listen:$_PORT
```

## Description

Creates a TCP listener that forwards connections to a raw TTY, providing immediate interactive shell support without additional upgrades.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| socat | Relay tool | Yes |
| file:`tty` | Bind to current terminal | Yes |
| raw | Raw mode for TTY | Yes |
| echo=0 | Disable echo | Yes |
| tcp-listen | TCP listen mode | Yes |
| $_PORT | Port to listen on (e.g., 12345) | Yes |

## Examples

### Listener on Port 12345

```bash
socat file:`tty`,raw,echo=0 tcp-listen:12345
```

### With Reuse Address

```bash
socat file:`tty`,raw,echo=0 tcp-listen:12345,reuseaddr
```

## Expected Output

2023/04/06 12:00:00 socat[1234] N listening on $_ADDRESS:$_PORT
Upon connection: Direct shell prompt.

## Related

- [[procedures/Spawn-TTY-Shell-from-Existing-Session]]
- [[commands/install-socat-on-ubuntu]]
