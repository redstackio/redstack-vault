---
id: 7316234e-2a50-4a44-8ea1-bd7fd3b1e4bb
name: Retrieve job details from sysjobs and sysjobsteps tables
type: command
executor: bash
data: SELECT job.job_id, notify_level_email, name, enabled, description, step_name,
  command, server, database_name FROM msdb.dbo.sysjobs job INNER JOIN msdb.dbo.sysjobsteps
  steps ON job.job_id = steps.job_id
output: null
created_at: '2023-04-06T03:56:20.549249+00:00'
updated_at: '2023-04-10T20:36:44.632664+00:00'
---

# Retrieve job details from sysjobs and sysjobsteps tables

```bash
SELECT job.job_id, notify_level_email, name, enabled, description, step_name, command, server, database_name FROM msdb.dbo.sysjobs job INNER JOIN msdb.dbo.sysjobsteps steps ON job.job_id = steps.job_id
```
