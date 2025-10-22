---
id: 51ff15e6-9f3a-42b3-9908-6ab6d2832c59
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:26.712955+00:00'
updated_at: '2023-04-10T20:37:05.988285+00:00'
---

# Code Snippet 51ff15e6

**Language**: Powershell

```powershell
$f=New-object -comObject HNetCfg.FwPolicy2;$f.rules |  where {$_.action -eq "0"} | select name,applicationname,localports
```
