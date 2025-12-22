---
id: abb2ca03-a454-41a9-b02e-b089e3ff3b36
name: sql-server-get-current-user-and-role
type: command
executor: sql
data: |-
  select suser_sname();
  select system_user;
  select is_srvrolemember('sysadmin');
output: null
created_at: '2023-04-06T03:56:20.717419+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - SQL Server
tags:
  - discovery
  - mssql
verified: true
validated: true
---

# sql-server-get-current-user-and-role

## Command

```sql
select suser_sname();
select system_user;
select is_srvrolemember('sysadmin');
```

## Description

This command executes three SQL queries in a SQL Server session to retrieve the current login name, the system user, and sysadmin role membership status. Use it during database discovery to assess access level after gaining a foothold in the SQL instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| suser_sname() | Built-in function returning SQL Server login name | Yes (no params) |
| system_user | Built-in function returning OS login name | Yes (no params) |
| is_srvrolemember('sysadmin') | Function checking membership in sysadmin role; returns 1 (true) or 0 (false) | Yes (role name fixed) |

## Examples

### Basic Usage

In sqlcmd or SSMS query window:

```sql
select suser_sname();
go
select system_user;
go
select is_srvrolemember('sysadmin');
go
```

### Advanced Usage

Combine into a single batch for scripting:

```sql
select suser_sname() as 'SQL Login', system_user as 'OS User', is_srvrolemember('sysadmin') as 'Is Sysadmin';
```

## Expected Output

For a standard user:

SQL Login
---------
domain\attacker

OS User
-------
DOMAIN\Attacker

Is Sysadmin
-----------
0

For sysadmin:

Is Sysadmin
-----------
1

Success is indicated by returned values without errors like 'permission denied'.

## Related

- [[procedures/Query-SQL-Server-Current-User-and-Sysadmin-Status]]
