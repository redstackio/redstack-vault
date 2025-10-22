---
id: 16ef218e-0f64-46ed-a285-19302da765e6
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:19.148465+00:00'
updated_at: '2023-04-10T20:34:32.708487+00:00'
---

# Code Snippet 16ef218e

**Language**: Powershell

```powershell
find / -writable ! -user `whoami` -type f ! -path "/proc/*" ! -path "/sys/*" -exec ls -al {} \; 2>/dev/null
find / -perm -2 -type f 2>/dev/null
find / ! -path "*/proc/*" -perm -2 -type f -print 2>/dev/null
```
