---
type: command
executor: sql
data: >-
  SELECT job.job_id, notify_level_email, name, enabled, description, step_name,
  command, server, database_name FROM msdb.dbo.sysjobs job INNER JOIN
  msdb.dbo.sysjobsteps steps ON job.job_id = steps.job_id
output: null
platforms:
  - SQL Server
tags:
  - discovery
  - mssql
verified: true
validated: true
---

# mssql-select-job-details-from-sysjobs-and-sysjobsteps

## Command

```sql
SELECT job.job_id, notify_level_email, name, enabled, description, step_name, command, server, database_name FROM msdb.dbo.sysjobs job INNER JOIN msdb.dbo.sysjobsteps steps ON job.job_id = steps.job_id
```

## Description

This SQL query joins the sysjobs and sysjobsteps tables in msdb to fetch detailed information about SQL Server Agent jobs, including steps, commands, and configurations. Ideal for analyzing job internals for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No runtime parameters; assumes connected SQL session with msdb access. | N/A |

## Examples

### Basic Usage

Run in a SQL client:

```sql
GO
SELECT job.job_id, notify_level_email, name, enabled, description, step_name, command, server, database_name FROM msdb.dbo.sysjobs job INNER JOIN msdb.dbo.sysjobsteps steps ON job.job_id = steps.job_id;
GO
```

### Advanced Usage

Limit to specific job:

```sql
SELECT ... FROM msdb.dbo.sysjobs job INNER JOIN msdb.dbo.sysjobsteps steps ON job.job_id = steps.job_id WHERE job.name = 'Backup Job';
```

## Expected Output

Multi-column result set:

```
job_id  notify_level_email  name  enabled  description  step_name  command  server  database_name
------  ------------------  ----  -------  -----------  ---------  -------  ------  -------------
A1B2...  0                   Backup  1       Weekly bkup  Step1      BACKUP DB...  SERVER1  master
```

## Related

- [[procedures/Enumerate-MSSQL-Server-Agent-Jobs]]
- [[commands/mssql-select-job-id-and-name-from-sysjobs]]
