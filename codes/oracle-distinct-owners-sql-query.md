---
id: 423661c2-31e3-46e8-8e8f-d0e52d9917f4
name: oracle-distinct-owners-sql-query
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.171321+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
tags:
  - database-enumeration
  - sql-injection
  - oracle
validated: true
---

# oracle-distinct-owners-sql-query

## Code

```sql
SELECT DISTINCT owner FROM all_tables;
```

## Description

This SQL code snippet queries the Oracle 'all_tables' view to extract unique table owners, providing a mapping of schemas and users in the database. It is designed for use in SQL injection attacks to perform blind or union-based enumeration of database metadata without requiring elevated privileges.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The query is static and does not use variables; adapt by wrapping in UNION for injection contexts. | N/A |

## Usage

Inject this query into a vulnerable SQL endpoint using UNION to match the original query's structure, e.g., `' UNION SELECT owner FROM all_tables --`. Execute via tools like SQLMap (`sqlmap -u "http://target/search?q=1" --dbms=oracle --technique=U`) or manual interception with Burp Suite. Useful in red team engagements for initial database reconnaissance after confirming SQLi.

## Detection

- Database logs showing SELECT from 'all_tables' by non-admin users.
- WAF alerts on UNION keywords or anomalous query lengths.
- Application errors (ORA-01789) from mismatched UNION columns.
- Monitor for repeated metadata queries indicating enumeration attempts.

## Related

- [[procedures/Oracle-SQL-Database-Enumeration-via-SQL-Injection]]
- [[tools/sqlmap]]
