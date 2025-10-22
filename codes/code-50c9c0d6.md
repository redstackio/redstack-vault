---
id: 50c9c0d6-37ca-464c-8ade-2afbe6f993c5
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.109333+00:00'
updated_at: '2023-04-10T20:36:45.035412+00:00'
---

# Code Snippet 50c9c0d6

**Language**: ps1

```ps1
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "select * from openquery(`"<DBSERVERNAME\DBInstance>`",'select @@version')" -Verbose
```
