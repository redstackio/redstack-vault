---
id: 46c4dbe0-7322-4bf3-9526-6f8f1c2c75a3
name: MSSQL-Query-Database-Principals-Excluding-Roles
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:20.876459+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - mssql
  - enumeration
  - sql-query
validated: true
---

# MSSQL-Query-Database-Principals-Excluding-Roles

## Code

```sql
Select * from sys.database_principals where type_desc != 'database_role';
```

## Description

This SQL code snippet queries the sys.database_principals system view in Microsoft SQL Server to retrieve all database-level principals (such as users and application roles) while excluding database roles. It provides essential details for discovering user accounts in a target database, aiding in account enumeration during security assessments or attacks. The query is lightweight and focuses on non-role entities that can be directly exploited or impersonated.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | This is a static query with no user-defined variables; customize the WHERE clause if needed for further filtering (e.g., by authentication type). | N/A |

## Usage

Execute this query in an MSSQL client like sqlcmd, Azure Data Studio, or SQL Server Management Studio (SSMS) after authenticating to the target database. It is typically used in procedures for database discovery, such as [[procedures/Enumerate-MSSQL-Database-Users]], where it forms the core of user enumeration. For example, integrate it into a sqlcmd invocation for remote execution during red team engagements.

## Detection

- Monitor SQL Server error logs and audit trails for SELECT queries on sys.database_principals from unauthorized sessions.
- Use SQL Server Audit to track access to system views, alerting on patterns like filtering by type_desc.
- Network-level detection: Unusual sqlcmd traffic or query patterns in proxy logs.
- Behavioral: Correlate with login events from low-privilege accounts attempting system view access.

## Related

- [[procedures/Enumerate-MSSQL-Database-Users]]
- [[tools/sqlcmd]]
