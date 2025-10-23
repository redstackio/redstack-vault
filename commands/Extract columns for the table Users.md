---
id: 20f1d0dc-c24d-404a-a066-f92388d06349
name: Extract columns for the table Users
type: command
executor: bash
data: '$ SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name
  = ''Users'')

  [*] UserId

  [*] UserName'
output: null
created_at: '2023-04-06T03:56:33.778123+00:00'
updated_at: '2023-04-10T20:22:44.170609+00:00'
---

# Extract columns for the table Users

```bash
$ SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'Users')
[*] UserId
[*] UserName
```


