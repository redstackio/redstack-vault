---
id: 3328aaed-40c4-43c9-a47c-e24a0804c81e
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.696660+00:00'
updated_at: '2023-04-10T20:37:53.214435+00:00'
---

# Code Snippet 3328aaed

**Language**: Powershell

```powershell
reg query HKLM\SYSTEM\CurrentControlSet\Services\SNMP /s
Get-ChildItem -path HKLM:\SYSTEM\CurrentControlSet\Services\SNMP -Recurse
```
