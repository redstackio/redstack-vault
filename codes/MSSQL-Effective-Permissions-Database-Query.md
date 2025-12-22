---
id: 0e989fa9-61c6-429f-a895-ef7ad2496fc5
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:20.987153+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - MSSQL Server
tags:
  - discovery
  - permissions
  - mssql
validated: true
---

# MSSQL-Effective-Permissions-Database-Query

## Code

```sql
SELECT * FROM fn_my_permissions(NULL, 'DATABASE');
```

## Description

This SQL code snippet queries the effective permissions on a SQL Server database using the built-in fn_my_permissions system function. When executed in the context of a database, it lists all permissions granted to the current user (or specified principal) for database-level operations, such as SELECT, INSERT, UPDATE, DELETE, or CONTROL. It is useful in red team engagements for discovering access rights without needing elevated privileges, helping to identify escalation opportunities.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| principal | The security principal (user, role, or login) to check permissions for; use NULL for current user | NULL or 'domain\\user' |
| object_type | The type of securable object to check (e.g., 'DATABASE', 'TABLE', 'SCHEMA') | 'DATABASE' |

## Usage

Execute this query directly in SQL Server Management Studio (SSMS), via sqlcmd, or embedded in a procedure like [[procedures/Query-MSSQL-Effective-Database-Permissions]]. For targeted checks, replace NULL with a specific user if you have VIEW DEFINITION permission. Adapt object_type for finer granularity, e.g., 'TABLE' for specific tables. Deliver via initial access vectors like compromised service accounts or SQL injection if unauthenticated.

## Detection

- Monitor SQL Server error logs and audit traces for executions of fn_my_permissions, which may indicate reconnaissance.
- Enable Query Store or Extended Events to log queries accessing system functions.
- Look for anomalous patterns in login activity followed by permission queries from unexpected hosts or users.
- Use tools like SQL Server Audit to flag GRANT/WITH GRANT OPTION checks on database objects.

## Related

- [[procedures/Query-MSSQL-Effective-Database-Permissions]]
- [[tools/sqlcmd]]
