---
id: 49ecb622-1210-48fe-816f-df921ffc2590
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:20.549123+00:00'
updated_at: '2023-04-10T20:36:44.633856+00:00'
---

# Code Snippet 49ecb622

**Language**: ps1

```ps1
SELECT job_id, [name] FROM msdb.dbo.sysjobs;
SELECT job.job_id, notify_level_email, name, enabled, description, step_name, command, server, database_name FROM msdb.dbo.sysjobs job INNER JOIN msdb.dbo.sysjobsteps steps ON job.job_id = steps.job_id
Get-SQLAgentJob -Instance "<DBSERVERNAME\DBInstance>" -username sa -Password Password1234 -Verbose
```
