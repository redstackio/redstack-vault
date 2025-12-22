---
type: command
executor: sql
data: 'SELECT job_id, [name] FROM msdb.dbo.sysjobs;'
output: null
platforms:
  - SQL Server
tags:
  - discovery
  - mssql
verified: true
validated: true
---

# mssql-select-job-id-and-name-from-sysjobs

## Command

```sql
SELECT job_id, [name] FROM msdb.dbo.sysjobs;
```

## Description

This SQL query retrieves the job_id and name of all SQL Server Agent jobs from the msdb database. Use it as an initial discovery step to identify automated tasks on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The query has no runtime parameters; run in a connected SQL session. | N/A |

## Examples

### Basic Usage

Execute in SSMS or sqlcmd after connecting to the instance.

```sql
GO
SELECT job_id, [name] FROM msdb.dbo.sysjobs;
GO
```

### Advanced Usage

Filter by enabled jobs:

```sql
SELECT job_id, [name] FROM msdb.dbo.sysjobs WHERE enabled = 1;
```

## Expected Output

A table with columns job_id (uniqueidentifier) and name (nvarchar):

```
job_id                                name
------------------------------------  ------------------------------
A1B2C3D4-E5F6-7890-ABCD-EF1234567890  Weekly Backup Job
B2C3D4E5-F6G7-8901-BCDE-FG2345678901  Data Export Task
```

## Related

- [[procedures/Enumerate-MSSQL-Server-Agent-Jobs]]
- [[commands/mssql-select-job-details-from-sysjobs-and-sysjobsteps]]
