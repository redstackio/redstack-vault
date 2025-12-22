---
type: procedure
description: >-
  Enumerates SQL Server Agent jobs to discover automated tasks, job details, and
  potential exploitation opportunities on a Microsoft SQL Server instance.
verified: true
submitted: false
tactics:
  - '[[tactics/Discovery|TA0007]]'
techniques:
  - '[[techniques/System-Information-Discovery|T1082]]'
sub_techniques: []
tags:
  - mssql
  - sql-server
  - agent-jobs
  - discovery
commands:
  - '[[commands/mssql-select-job-id-and-name-from-sysjobs]]'
  - '[[commands/mssql-select-job-details-from-sysjobs-and-sysjobsteps]]'
  - '[[commands/mssql-get-sqlagentjob-powershell]]'
platforms:
  - Windows
  - SQL Server
tools: []
validated: true
---

# Enumerate-MSSQL-Server-Agent-Jobs

## Summary

This procedure enumerates all SQL Server Agent jobs on a Microsoft SQL Server instance, revealing automated tasks, job configurations, execution commands, and associated users or systems. It is useful in red team engagements for discovering scheduled operations that may expose sensitive data, credentials, or escalation paths.

## Description

SQL Server Agent jobs automate routine tasks such as backups, maintenance, or data processing. Enumerating these jobs provides attackers with insights into system workflows, potentially identifying misconfigured jobs that run with elevated privileges or contain hardcoded credentials. This procedure uses direct SQL queries against the msdb database and PowerShell cmdlets to retrieve job lists and details. It assumes authenticated access to the SQL instance via SQL Server Management Studio (SSMS), sqlcmd, or PowerShell. The technique aligns with discovery phases where attackers map internal processes for lateral movement or persistence opportunities.

## Requirements

1. Valid SQL Server credentials with read access to the msdb database (e.g., db_datareader role or equivalent).
2. Network access to the SQL Server instance (default port 1433/TCP).
3. Tools: SQL client like SSMS, sqlcmd, or PowerShell with SQL Server module (SqlServer).
4. For PowerShell method: The SqlServer module installed on the executing host.

## Defense

- Restrict access to msdb database views (sysjobs, sysjobsteps) to only necessary roles; use principle of least privilege.
- Enable SQL Server auditing for queries against msdb to log enumeration attempts.
- Monitor for anomalous queries or PowerShell executions targeting job-related tables.
- Use database activity monitoring (DAM) tools to alert on access to sensitive system views.

## Objectives

1. List all SQL Server Agent jobs with IDs and names.
2. Retrieve detailed job configurations, including steps, commands, and execution contexts.
3. Identify potential exploitation targets like privileged job commands or owner details.
4. Validate successful enumeration without triggering alerts.

## Instructions

### Step 1: Connect to the SQL Server Instance

**Context**: Establish a connection to the target SQL Server using a client tool. This step ensures you have the necessary access before querying job data. Replace placeholders with actual instance details.

Use sqlcmd or SSMS to connect:

```bash
sqlcmd -S <SERVER_NAME> -U <USERNAME> -P <PASSWORD>
```

> Once connected, proceed to query execution. Expected: Successful login prompt (1>).

### Step 2: Retrieve Job IDs and Names

**Context**: Start with a basic enumeration to list all jobs, identifying names and IDs for further targeting. This reveals the scope of automated tasks without exposing sensitive details.

**Command** ([[commands/mssql-select-job-id-and-name-from-sysjobs]]):

```sql
SELECT job_id, [name] FROM msdb.dbo.sysjobs;
```

> This query targets the sysjobs table in msdb, returning unique job IDs and human-readable names. Run it in your SQL client. If jobs exist, it helps prioritize interesting ones (e.g., backup or data export jobs). GO to execute.

### Step 3: Retrieve Detailed Job Information

**Context**: Expand on the basic list by joining sysjobs with sysjobsteps to uncover job steps, including executable commands, databases, and notification settings. This step uncovers potential credential leaks or RCE vectors in job scripts.

**Command** ([[commands/mssql-select-job-details-from-sysjobs-and-sysjobsteps]]):

```sql
SELECT job.job_id, notify_level_email, name, enabled, description, step_name, command, server, database_name FROM msdb.dbo.sysjobs job INNER JOIN msdb.dbo.sysjobsteps steps ON job.job_id = steps.job_id;
```

> Execute this JOIN query to get comprehensive details. Look for 'command' fields containing scripts or executables that could be hijacked. Expected: Rows showing job configs; empty if no jobs or access denied.

### Step 4: Use PowerShell for Remote Enumeration (Alternative)

**Context**: If direct SQL access is limited, use PowerShell from a compromised host to query the instance remotely. This method leverages the SqlServer module for structured output and is useful in Windows environments.

**Command** ([[commands/mssql-get-sqlagentjob-powershell]]):

```powershell
Get-SQLAgentJob -Instance "<DBSERVERNAME\DBInstance>" -username sa -Password Password1234 -Verbose
```

> Install SqlServer module if needed (Install-Module SqlServer). Replace instance, username, and password. This cmdlet fetches job objects; pipe to Format-Table for readability (e.g., | Format-Table Name, Enabled, Description). Expected: Object list with job properties; verbose output shows connection details.
