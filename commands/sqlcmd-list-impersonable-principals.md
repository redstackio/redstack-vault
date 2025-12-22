---
id: 6ed79db7-f91e-48aa-b484-271980b59757
name: sqlcmd-list-impersonable-principals
type: command
executor: bash
data: >-
  sqlcmd -S $_SERVER -U $_USERNAME -P $_PASSWORD -Q "select distinct b.name from
  sys.server_permissions a inner join sys.server_principals b on
  a.grantor_principal_id = b.principal_id where a.permission_name =
  'impersonate'"
output: null
created_at: '2023-04-06T03:56:21.008928+00:00'
updated_at: '2023-04-10T20:36:39.959103+00:00'
platforms:
  - Windows
  - Linux
tags:
  - mssql
  - query
verified: true
validated: true
---

# sqlcmd-list-impersonable-principals

## Command

```bash
sqlcmd -S $_SERVER -U $_USERNAME -P $_PASSWORD -Q "select distinct b.name from sys.server_permissions a inner join sys.server_principals b on a.grantor_principal_id = b.principal_id where a.permission_name = 'impersonate'"
```

## Description

This command uses sqlcmd to connect to a SQL Server instance and execute a query that lists server principals (logins) the current user can impersonate. It is used during privilege escalation reconnaissance to identify exploitable permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVER | SQL Server hostname or IP (e.g., localhost or 192.168.1.100) | Yes |
| $_USERNAME | SQL login username | Yes |
| $_PASSWORD | SQL login password | Yes |
| -S | Specifies the server instance | Built-in |
| -U | Specifies the username | Built-in |
| -P | Specifies the password | Built-in |
| -Q | Executes the query and exits | Built-in |

## Examples

### Basic Usage

```bash
sqlcmd -S localhost -U lowpriv -P pass123 -Q "select distinct b.name from sys.server_permissions a inner join sys.server_principals b on a.grantor_principal_id = b.principal_id where a.permission_name = 'impersonate'"
```

### Advanced Usage

For trusted connections (Windows auth):
```bash
sqlcmd -S localhost -E -Q "select distinct b.name from sys.server_permissions a inner join sys.server_principals b on a.grantor_principal_id = b.principal_id where a.permission_name = 'impersonate'"
```

## Expected Output

A list of impersonable login names, e.g.:
```
name
--------------------
sa
service_account
lowpriv_user

(3 rows affected)
```

## Related

- [[procedures/SQL-Server-Impersonation-Privilege-Escalation]]
- [[commands/sqlcmd-impersonate-login]]
