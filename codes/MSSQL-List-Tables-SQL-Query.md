---
id: e36a61a9-10e4-4344-9035-fb983f301910
name: MSSQL-List-Tables-SQL-Query
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:20.798261+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - mssql
  - discovery
  - query
validated: true
---

# MSSQL-List-Tables-SQL-Query

## Code

```sql
select table_name from information_schema.tables
```

## Description

This SQL query retrieves the names of all tables (both user and system) in the current MSSQL database by querying the standard INFORMATION_SCHEMA.TABLES view. It is a lightweight, permission-efficient way to enumerate database structure during discovery phases of an attack, helping identify tables for further querying without needing elevated privileges.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | This is a static query with no variables; customize by adding WHERE clauses (e.g., table_type='BASE TABLE' for user tables only) | N/A |

## Usage

Execute this query via sqlcmd, PowerShell Invoke-Sqlcmd, or any SQL client connected to the MSSQL instance. It is typically used after gaining initial database access to map out schema. For example, embed in a command like sqlcmd -Q "[this query]" or run in SSMS for interactive sessions. Combine with other queries like SELECT * FROM information_schema.columns for full schema details.

## Detection

- Monitor SQL Server error logs and audit trails for SELECT queries on INFORMATION_SCHEMA views from unexpected users or IPs.
- Use SQL Profiler or Extended Events to trace metadata queries.
- Baseline normal query patterns; anomalous enumeration without business context indicates compromise.

## Related

- [[procedures/List-MSSQL-Database-Tables]] (procedure that uses this code)
- [[tools/sqlcmd]] (tool for executing this code)
