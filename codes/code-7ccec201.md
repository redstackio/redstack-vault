---
id: 7ccec201-9743-4c7b-88b8-be1748735de0
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.090028+00:00'
updated_at: '2023-04-10T20:36:31.429174+00:00'
---

# Code Snippet 7ccec201

**Language**: ps1

```ps1
Get-SQLServerLinkCrawl -Instance "<DBSERVERNAME\DBInstance>" -Verbose
select * from openquery("<instance>",'select * from openquery("<instance2>",''select * from master..sysservers'')')
```


