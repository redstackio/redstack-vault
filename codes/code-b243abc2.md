---
id: b243abc2-b353-4eaf-9236-12f11a137069
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.851324+00:00'
updated_at: '2023-04-10T20:37:52.896620+00:00'
---

# Code Snippet b243abc2

**Language**: Powershell

```powershell
C:\Windows\System32> icacls config\SAM
config\SAM BUILTIN\Administrators:(I)(F)
           NT AUTHORITY\SYSTEM:(I)(F)
           BUILTIN\Users:(I)(RX)    <-- this is wrong - regular users should not have read access!
```


