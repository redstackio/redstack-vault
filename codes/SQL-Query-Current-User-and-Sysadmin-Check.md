---
id: ee55ad54-5198-4e01-bbc7-e402f2903f6e
name: SQL-Query-Current-User-and-Sysadmin-Check
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:20.717346+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - SQL Server
tags:
  - discovery
  - mssql
validated: true
---

# SQL-Query-Current-User-and-Sysadmin-Check

## Code

```sql
select suser_sname()
Select system_user
select is_srvrolemember('sysadmin')
```

## Description

This SQL code snippet queries the current SQL Server user details and checks for sysadmin privileges. It uses built-in system functions to output the login name, OS user, and role membership, providing essential discovery information in database penetration testing without requiring additional tools.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; uses fixed system functions | N/A |

## Usage

Execute this code directly in a SQL Server session via sqlcmd, SSMS, or an exploited application's query interface after initial access. It is typically used in the discovery phase to evaluate privilege levels and plan escalation. For example, paste into a query window and run to quickly assess access.

## Detection

- Audit logs showing execution of SUSER_SNAME, SYSTEM_USER, or IS_SRVROLEMEMBER functions from unexpected accounts.
- Query monitoring tools like SQL Server Profiler capturing these SELECT statements.
- Anomalous access patterns to system catalogs from non-admin users.

## Related

- [[procedures/Query-SQL-Server-Current-User-and-Sysadmin-Status]]
