---
id: 24a6589b-2ce8-49b3-91ec-87d576a1cfca
name: sql-query-list-impersonable-principals
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:21.008865+00:00'
updated_at: '2023-04-10T20:36:39.961985+00:00'
platforms:
  - SQL Server
tags:
  - mssql
  - query
  - recon
validated: true
---

# sql-query-list-impersonable-principals

## Code

```sql
select distinct b.name
from sys.server_permissions a
inner join sys.server_principals b
on a.grantor_principal_id = b.principal_id
where a.permission_name = 'impersonate'
```

## Description

This SQL query retrieves a distinct list of server principals (logins) that the current user has permission to impersonate. It joins sys.server_permissions and sys.server_principals to filter for 'IMPERSONATE' permissions, aiding in identifying escalation paths in SQL Server environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | This query has no variables; it runs in the current context | N/A |

## Usage

Execute this query within a SQL Server session (e.g., via sqlcmd, SSMS, or embedded in a procedure) after gaining initial low-privileged access. Use the output to select a target for impersonation in privilege escalation workflows, such as assuming a sysadmin role to access restricted data or execute commands.

## Detection

- Audit SQL Server error logs and traces for queries accessing sys.server_permissions.
- Enable Extended Events for permission-related activities.
- Monitor for unusual SELECT statements on system views from low-priv accounts.

## Related

- [[procedures/SQL-Server-Impersonation-Privilege-Escalation]]
- [[commands/sqlcmd-list-impersonable-principals]]
