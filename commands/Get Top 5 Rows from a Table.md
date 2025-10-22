---
id: 1a9d5bbe-1355-433a-b029-ed06d3d906c1
name: Get Top 5 Rows from a Table
type: command
executor: bash
data: Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query 'select TOP 5 * from
  <DatabaseName>.dbo.<TableName>'
output: null
created_at: '2023-04-06T03:56:19.967905+00:00'
updated_at: '2023-04-10T20:36:38.969554+00:00'
---

# Get Top 5 Rows from a Table

```bash
Get-SQLQuery -Instance "<DBSERVERNAME\DBInstance>" -Query 'select TOP 5 * from <DatabaseName>.dbo.<TableName>'
```
