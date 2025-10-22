---
id: cca6246d-3d68-4e9d-8239-5293174fb291
name: List tables with owner and columns with 'PASS'
type: command
executor: bash
data: SELECT owner, table_name FROM all_tab_columns WHERE column_name LIKE '%PASS%';
output: null
created_at: '2023-04-06T03:56:35.238442+00:00'
updated_at: '2023-04-10T20:23:09.986053+00:00'
---

# List tables with owner and columns with 'PASS'

```bash
SELECT owner, table_name FROM all_tab_columns WHERE column_name LIKE '%PASS%';
```
