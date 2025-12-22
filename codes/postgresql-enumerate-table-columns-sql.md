---
id: dd2079a2-c188-4ecc-b70d-369a63719004
name: postgresql-enumerate-table-columns-sql
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.720017+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - sql-injection
  - postgresql
  - database-enumeration
validated: true
---

# postgresql-enumerate-table-columns-sql

## Code

```sql
SELECT column_name FROM information_schema.columns WHERE table_name='data_table'
```

## Description

This SQL code snippet queries the PostgreSQL information_schema.columns view to list all column names for a given table. It is a core payload for SQL injection-based schema enumeration, allowing attackers to map database structure without direct access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| data_table | The name of the target table | users |

## Usage

Inject this query into a vulnerable input field (e.g., search parameter) in a web application connected to PostgreSQL. For blind injections, wrap in conditional logic like SUBSTRING to extract results incrementally. Use tools like sqlmap with --dbms=postgresql --technique=B for automation.

## Detection

- Database query logs showing access to information_schema.columns from untrusted sources.
- Web application logs with anomalous SELECT patterns or UNION attempts.
- Increased error rates from invalid table names or permission checks on metadata views.

## Related

- [[procedures/PostgreSQL-Column-Enumeration-via-SQL-Injection]]
