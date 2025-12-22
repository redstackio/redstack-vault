---
id: 4e2a58d7-8937-4748-a37d-3198b568e9dd
name: mssql-enumerate-database-roles-query
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:20.923476+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - SQL Server
tags:
  - mssql
  - enumeration
  - sql-query
validated: true
---

# mssql-enumerate-database-roles-query

## Code

```sql
SELECT DB1.name AS DatabaseRoleName,
isnull (DB2.name, 'No members') AS DatabaseUserName
FROM sys.database_role_members AS DRM
RIGHT OUTER JOIN sys.database_principals AS DB1
ON DRM.role_principal_id = DB1.principal_id
LEFT OUTER JOIN sys.database_principals AS DB2
ON DRM.member_principal_id = DB2.principal_id
WHERE DB1.type = 'R'
ORDER BY DB1.name;
```

## Description

This SQL code snippet enumerates all database roles in an MSSQL instance and lists their user or principal members. It uses RIGHT and LEFT OUTER JOINs on sys.database_role_members and sys.database_principals to ensure all roles are shown, even those without members (displayed as 'No members'). The filter DB1.type = 'R' limits results to database roles only. This is a key discovery technique for understanding permission structures in MSSQL environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a parameter-free query; it operates on the current database context. For customization, add WHERE clauses manually (e.g., for specific roles). | N/A |

## Usage

Copy and paste this code into a SQL query tool like SSMS or execute via sqlcmd/PowerShell after connecting to the target MSSQL instance. Use it in red team engagements after gaining database access to map roles for escalation (e.g., identifying db_owner members). It can be embedded in scripts for automated enumeration or modified to target specific databases with a preceding 'USE [DBName];' statement.

## Detection

- Monitor SQL Server error logs and audit trails for executions of queries referencing sys.database_role_members or sys.database_principals from low-privilege accounts.
- Use SQL Server Profiler or Extended Events to trace SELECT statements on system views during discovery phases.
- Alert on unusual query patterns from non-administrative users, especially if combined with other enumeration queries (e.g., for logins or permissions).

## Related

- [[procedures/Enumerate-MSSQL-Database-Roles-and-User-Members]]
