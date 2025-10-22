---
id: e2befbc3-a054-49b7-841d-d935dcaf9243
name: Extracting column_name from project_id.dataset_name.table_name
type: command
executor: bash
data: SELECT column_name FROM project_id.dataset_name.INFORMATION_SCHEMA.COLUMNS WHERE
  table_name = 'table_name'
output: null
created_at: '2023-04-06T03:56:32.353180+00:00'
updated_at: '2023-04-10T20:21:05.529526+00:00'
---

# Extracting column_name from project_id.dataset_name.table_name

```bash
SELECT column_name FROM project_id.dataset_name.INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'table_name'
```
