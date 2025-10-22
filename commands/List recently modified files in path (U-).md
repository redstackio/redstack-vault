---
id: 2b6e1e4d-76e8-4c10-bd73-935f2adc1b70
name: List recently modified files in path (U:)
type: command
executor: bash
data: 'Get-Childitem u:\ -Recurse | where-object {!($_.psiscontainer)} | where { $_.LastWriteTime
  -gt $(Get-Date).AddDays(-1) } | foreach {"$($_.LastWriteTime) :: $($_.Fullname)
  " }

  '
output: null
created_at: '2020-07-14T18:21:10.754923+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List recently modified files in path (U:)

```bash
Get-Childitem u:\ -Recurse | where-object {!($_.psiscontainer)} | where { $_.LastWriteTime -gt $(Get-Date).AddDays(-1) } | foreach {"$($_.LastWriteTime) :: $($_.Fullname) " }

```
