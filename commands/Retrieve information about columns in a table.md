---
id: 82b31120-87c6-49d1-89a7-65fe73b34468
name: Retrieve information about columns in a table
type: command
executor: bash
data: select name, tbname, coltype from sysibm.syscolumns -- also valid syscat and
  sysstat
output: null
created_at: '2023-04-06T03:56:32.778156+00:00'
updated_at: '2023-04-10T20:22:00.136780+00:00'
---

# Retrieve information about columns in a table

```bash
select name, tbname, coltype from sysibm.syscolumns -- also valid syscat and sysstat
```
