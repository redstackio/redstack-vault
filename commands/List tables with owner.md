---
id: e449e314-f952-4c89-b967-8960d359acf4
name: List tables with owner
type: command
executor: bash
data: SELECT owner, table_name FROM all_tables;
output: null
created_at: '2023-04-06T03:56:35.238340+00:00'
updated_at: '2023-04-10T20:23:09.986053+00:00'
---

# List tables with owner

```bash
SELECT owner, table_name FROM all_tables;
```


