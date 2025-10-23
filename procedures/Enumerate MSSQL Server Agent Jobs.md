---
id: daaeb732-2cfd-41ef-bee7-7824b26cf938
name: Enumerate MSSQL Server Agent Jobs
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:20.555981+00:00'
updated_at: '2023-04-10T20:36:44.603308+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Browser Bookmark Discovery|T1217 - Browser Bookmark Discovery]]'
tags:
- '[[Agent Jobs]]'
- '[[List All Jobs]]'
- '[[MSSQL Server]]'
commands:
- '[[Retrieve job details from sysjobs and sysjobsteps tables]]'
- '[[Retrieve job details using PowerShell]]'
- '[[Retrieve job_id and name from sysjobs table]]'
---

# Enumerate MSSQL Server Agent Jobs

## Summary

This procedure involves enumerating all agent jobs on a MSSQL server. By doing so, an attacker can gain insight into what tasks are being automated and potentially identify targets for further exploitation. This technique can also be used to identify system owners and users, which can aid in latera

## Description

# Description

This procedure involves enumerating all agent jobs on a MSSQL server. By doing so, an attacker can gain insight into what tasks are being automated and potentially identify targets for further exploitation. This technique can also be used to identify system owners and users, which can aid in lateral movement. 

To accomplish this, the attacker would utilize the 'SQL Agent Jobs Details' command to list all jobs on the server. The output would include the job name, status, and last run time. 

From a business perspective, identifying automated tasks can aid in identifying potential areas for optimization or streamlining of processes. However, from a security perspective, it is important to ensure that only authorized users have access to this information.

 

## Requirements

1. Valid credentials for the MSSQL server

 

## Defense

1. Ensure that only authorized users have access to the MSSQL server

1. Implement strong authentication measures, such as multi-factor authentication

1. Monitor for and promptly respond to any suspicious activity on the MSSQL server

 

## Objectives

1. Enumerate all agent jobs on the MSSQL server

1. Identify potential targets for further exploitation

1. Identify system owners and users

 

# Instructions

1. This command retrieves the list of SQL Agent Jobs and their details. The first SELECT statement retrieves the list of SQL Agent Jobs with their job_id and name. The second SELECT statement retrieves the details of each SQL Agent Job, such as notify_level_email, enabled, description, and the command to be executed. The Get-SQLAgentJob cmdlet is used to retrieve the details of SQL Agent Jobs on a specified SQL Server instance. Replace <DBSERVERNAME\DBInstance> with the name of the SQL Server instance you want to retrieve the details from. Replace sa and Password1234 with the appropriate credentials to connect to the SQL Server instance.

 



**Code**: [[SELECT job_id, [name] FROM msdb.dbo.sysjobs;
SELEC]]



> The first SELECT statement retrieves the job_id and name of all SQL Agent Jobs present on the server. The second SELECT statement retrieves the details of each SQL Agent Job, such as notify_level_email, enabled, description, and the command to be executed. The Get-SQLAgentJob cmdlet is used to retrieve the details of SQL Agent Jobs on a specified SQL Server instance. The -Instance parameter specifies the name of the SQL Server instance you want to retrieve the details from. The -username and -Password parameters are used to specify the credentials to connect to the SQL Server instance. The -Verbose parameter is used to display detailed information about the command execution.



**Command** ([[Retrieve job_id and name from sysjobs table]]):

```bash
SELECT job_id, [name] FROM msdb.dbo.sysjobs;
```





**Command** ([[Retrieve job details from sysjobs and sysjobsteps tables]]):

```bash
SELECT job.job_id, notify_level_email, name, enabled, description, step_name, command, server, database_name FROM msdb.dbo.sysjobs job INNER JOIN msdb.dbo.sysjobsteps steps ON job.job_id = steps.job_id
```





**Command** ([[Retrieve job details using PowerShell]]):

```bash
Get-SQLAgentJob -Instance "<DBSERVERNAME\DBInstance>" -username sa -Password Password1234 -Verbose
```



## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Browser Bookmark Discovery|T1217 - Browser Bookmark Discovery]]

## Commands Used

- [[Retrieve job details from sysjobs and sysjobsteps tables]]
- [[Retrieve job details using PowerShell]]
- [[Retrieve job_id and name from sysjobs table]]

## Tags

- [[Agent Jobs]]
- [[List All Jobs]]
- [[MSSQL Server]]


