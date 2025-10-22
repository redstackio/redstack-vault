---
id: b2acd20b-c91a-4e31-af48-5df38bbfaba1
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:06.673183+00:00'
updated_at: '2023-04-10T20:25:59.719096+00:00'
---

# Code Snippet b2acd20b

**Language**: Powershell

```powershell
ADACLScan.ps1 -Base "DC=contoso;DC=com" -Filter "(&(AdminCount=1))" -Scope subtree -EffectiveRightsPrincipal User1 -Output HTML -Show
```
