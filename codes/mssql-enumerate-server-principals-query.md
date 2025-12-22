---
id: 89cd3828-a12d-49df-b705-62b9fd4252d4
name: mssql-enumerate-server-principals-query
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:20.842601+00:00'
updated_at: '2023-04-10T20:36:42.878508+00:00'
platforms:
  - Windows
  - Linux
  - Database
tags:
  - mssql
  - query
  - enumeration
validated: true
---

# mssql-enumerate-server-principals-query

## Code

```sql
Select * from sys.server_principals where type_desc != 'SERVER_ROLE'
```

## Description

This SQL code snippet queries the sys.server_principals view to list all server logins on an MSSQL instance, excluding server roles. It retrieves essential details like login names, types (SQL or Windows), and status flags, serving as a foundational discovery tool in database security assessments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | This is a static query with no variables; customize filters if needed (e.g., add WHERE name LIKE '%admin%') | N/A |

## Usage

Execute this code in a SQL client connected to the target MSSQL server, such as SSMS, sqlcmd, or integrated into a script (e.g., Python with pymssql). It is typically used after gaining initial database access to map accounts for further exploitation, like identifying weak SQL logins for brute-force attempts.

## Detection

- SQL Server logs showing SELECT on sys.server_principals from non-admin users.
- Audit traces capturing anomalous enumeration queries during off-hours.
- Extended Events monitoring for system view access patterns indicative of reconnaissance.

## Related

- [[procedures/Enumerate-MSSQL-Server-Logins]]
- [[techniques/Account-Discovery|T1087]]
