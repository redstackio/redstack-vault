---
id: 134b9210-0dd3-410b-b5ac-74cff275aab9
name: Extract tables from Injection database
type: command
executor: bash
data: '$ SELECT name FROM Injection..sysobjects WHERE xtype = ''U''

  [*] Profiles

  [*] Roles

  [*] Users'
output: null
created_at: '2023-04-06T03:56:33.778050+00:00'
updated_at: '2023-04-10T20:22:44.170609+00:00'
---

# Extract tables from Injection database

```bash
$ SELECT name FROM Injection..sysobjects WHERE xtype = 'U'
[*] Profiles
[*] Roles
[*] Users
```
