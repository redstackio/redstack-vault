---
id: 929315e5-719e-48f2-9249-7d5c9d14abeb
name: Performing UNION ALL SELECT operation with column_name and 1
type: command
executor: bash
data: UNION ALL SELECT column_name,1,1 FROM (select column_name AS new_name from `project_id.dataset_name.table_name`)
  AS A GROUP BY column_name
output: null
created_at: '2023-04-06T03:56:32.353507+00:00'
updated_at: '2023-04-10T20:21:05.529526+00:00'
---

# Performing UNION ALL SELECT operation with column_name and 1

```bash
UNION ALL SELECT column_name,1,1 FROM (select column_name AS new_name from `project_id.dataset_name.table_name`) AS A GROUP BY column_name
```
