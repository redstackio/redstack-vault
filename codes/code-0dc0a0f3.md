---
id: 0dc0a0f3-7632-4573-93eb-082af1a27623
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.169432+00:00'
updated_at: '2023-04-10T20:36:35.279033+00:00'
---

# Code Snippet 0dc0a0f3

**Language**: ps1

```ps1
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "select * from openquery(`"<DatabaseLinkName>`",'select name from <DatabaseNameFromPreviousCommand>.sys.tables')" -Verbose
```


