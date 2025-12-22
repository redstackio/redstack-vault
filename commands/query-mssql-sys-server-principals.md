---
id: c0c54e93-5e9a-415e-8ad5-aaa671a7be10
name: query-mssql-sys-server-principals
type: command
executor: sql
data: SELECT * FROM sys.server_principals WHERE type_desc != 'SERVER_ROLE';
output: null
created_at: '2023-04-06T03:56:20.842671+00:00'
updated_at: '2023-04-10T20:36:42.877343+00:00'
platforms:
  - Windows
  - Linux
  - Database
tags:
  - mssql
  - enumeration
  - discovery
verified: true
validated: true
---

# query-mssql-sys-server-principals

## Command

```sql
SELECT * FROM sys.server_principals WHERE type_desc != 'SERVER_ROLE';
```

## Description

This SQL command queries the sys.server_principals system view in Microsoft SQL Server to enumerate all server-level principals (logins) excluding built-in server roles. It is used during database discovery to identify user accounts, their types, and status for potential targeting or auditing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| type_desc != 'SERVER_ROLE' | Filter clause to exclude server roles like sysadmin or dbcreator, focusing on logins | Yes |
| * (SELECT *) | Selects all columns including name, principal_id, sid, type_desc, is_disabled, create_date | Built-in |

## Examples

### Basic Usage

Execute directly in SSMS or via sqlcmd:

```sql
SELECT * FROM sys.server_principals WHERE type_desc != 'SERVER_ROLE';
```

### Advanced Usage (with Output to File via sqlcmd)

```bash
sqlcmd -S $_SERVER -U $_USERNAME -P $_PASSWORD -Q "SELECT * FROM sys.server_principals WHERE type_desc != 'SERVER_ROLE';" -o logins.txt
```

## Expected Output

A result set table with columns such as:

name | principal_id | type_desc | is_disabled | create_date
----|--------------|-----------|-------------|------------
'sa' | 1 | SQL_LOGIN | 0 | 2023-01-01 00:00:00
'DOMAIN\user1' | 5 | WINDOWS_LOGIN | 0 | 2023-02-15 10:30:00

Success is indicated by rows returned without permission errors (e.g., no 'SELECT permission denied'). Empty results may mean no logins or insufficient access.

## Related

- [[procedures/Enumerate-MSSQL-Server-Logins]]
- [[techniques/Account-Discovery|T1087]]
