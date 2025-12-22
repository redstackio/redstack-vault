---
id: d271c377-b308-4b3b-8153-6b818f21438c
name: SQL-Query-List-Sysadmin-Principals
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:20.900542+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - discovery
  - sql-query
validated: true
---

# SQL-Query-List-Sysadmin-Principals

## Code

```sql
SELECT name,type_desc,is_disabled FROM sys.server_principals WHERE IS_SRVROLEMEMBER ('sysadmin',name) = 1
```

## Description

This SQL code snippet enumerates all server principals in an MSSQL instance that belong to the sysadmin role, returning their names, types (e.g., SQL login or Windows user), and disabled status. It is used in discovery phases to identify privileged accounts for potential targeting in privilege escalation or lateral movement.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The query contains no variables or placeholders; it is self-contained and executes directly against the sys.server_principals view. | N/A |

## Usage

Execute this query in an MSSQL client (e.g., sqlcmd, SSMS) after connecting with valid credentials. It is typically run during post-exploitation on a compromised database server to map administrative access. For example, paste into a query window and run to output a list of sysadmins, which can then be exported or used to inform further attacks like targeting the 'sa' account.

## Detection

- Monitor SQL Server logs for queries accessing sys.server_principals or using IS_SRVROLEMEMBER on sysadmin.
- Enable SQL Audit for SELECT statements on system views and alert on unusual role enumeration from non-administrative accounts.
- Look for anomalous query patterns in extended events or SIEM data, such as repeated executions from external IPs.

## Related

- [[procedures/Query-MSSQL-Server-for-Sysadmins]]
