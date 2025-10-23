---
id: e87e3c8f-c220-4c1a-b77d-8d6dffee92b2
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.152574+00:00'
updated_at: '2023-04-10T20:36:32.492507+00:00'
---

# Code Snippet e87e3c8f

**Language**: ps1

```ps1
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "select * from openquery(`"<DatabaseLinkName>`",'select name from sys.databases')" -Verbose
```


