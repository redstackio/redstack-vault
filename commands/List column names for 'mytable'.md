---
id: c2921a79-d8df-42b0-85e0-0bd8b94a5f0b
name: List column names for 'mytable'
type: command
executor: bash
data: SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name
  = 'mytable'); -- for the current DB only
output: null
created_at: '2023-04-06T03:56:33.675975+00:00'
updated_at: '2023-04-10T20:22:44.531078+00:00'
---

# List column names for 'mytable'

```bash
SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'mytable'); -- for the current DB only
```


