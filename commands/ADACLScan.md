---
id: 95e37f66-6bbb-4619-be6a-07d168445550
name: ADACLScan
type: command
executor: bash
data: ADACLScan.ps1 -Base "DC=contoso;DC=com" -Filter "(&(AdminCount=1))" -Scope subtree
  -EffectiveRightsPrincipal User1 -Output HTML -Show
output: null
created_at: '2023-04-06T03:56:06.673244+00:00'
updated_at: '2023-04-10T20:25:59.724416+00:00'
---

# ADACLScan

```bash
ADACLScan.ps1 -Base "DC=contoso;DC=com" -Filter "(&(AdminCount=1))" -Scope subtree -EffectiveRightsPrincipal User1 -Output HTML -Show
```
