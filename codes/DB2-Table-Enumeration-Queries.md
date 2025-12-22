---
id: 86760a13-8ed9-48cb-bea4-210f21b31f04
name: DB2-Table-Enumeration-Queries
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:32.805720+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Database
  - DB2
tags:
  - SQL-Injection
  - Database-Enumeration
validated: true
---

# DB2-Table-Enumeration-Queries

## Code

```sql
select table_name from sysibm.tables
select name from sysibm.systables
```

## Description

This SQL code snippet contains two queries for enumerating table names in an IBM DB2 database. The first query lists tables from the current schema using the TABLES view, while the second lists all tables database-wide using the SYSTABLES view. It is designed for injection into vulnerable applications to perform schema reconnaissance without direct database access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | No variables; static queries ready for injection | N/A |

## Usage

Inject these queries via UNION-based SQL injection in web applications, e.g., append ' UNION SELECT table_name FROM sysibm.tables -- to a vulnerable parameter. Execute sequentially for complete coverage. Useful in penetration testing to map database structure before targeting specific tables for data extraction.

## Detection

- Monitor application logs for queries accessing SYSIBM views.
- WAF rules detecting UNION SELECT patterns or DB2-specific catalog access.
- Database audit logs showing anomalous SELECTs on system tables from unexpected users.

## Related

- [[procedures/List-Tables-via-DB2-SQL-Injection]]
