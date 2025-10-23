---
id: ba13c157-bc5d-4e86-9cba-96cd2fc82b24
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.213829+00:00'
updated_at: '2023-04-10T20:36:40.328326+00:00'
---

# Code Snippet ba13c157

**Language**: ps1

```ps1
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query "select * from openquery(`"<DatabaseLinkName>`"'select * from <DatabaseNameFromPreviousCommand>.dbo.<TableNameFromPreviousCommand> where <ColumnNameFromPreviousCommand>=<ColumnValueFromPreviousCommand>')" -Verbose
```


