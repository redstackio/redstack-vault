---
id: cfcbbbfa-4ff3-49ec-ace3-d1f4396d50d3
name: Retrieve job_id and name from sysjobs table
type: command
executor: bash
data: SELECT job_id, [name] FROM msdb.dbo.sysjobs;
output: null
created_at: '2023-04-06T03:56:20.549175+00:00'
updated_at: '2023-04-10T20:36:44.632664+00:00'
---

# Retrieve job_id and name from sysjobs table

```bash
SELECT job_id, [name] FROM msdb.dbo.sysjobs;
```


