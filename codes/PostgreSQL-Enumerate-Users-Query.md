---
type: code
language: SQL
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Web
tags:
  - postgresql
  - sql-injection
  - discovery
validated: true
---

# PostgreSQL-Enumerate-Users-Query

## Code

```sql
SELECT usename FROM pg_user
```

## Description

This SQL code snippet queries the pg_user system table in PostgreSQL to list all database usernames. It serves as the core payload for user enumeration attacks, particularly when injected into vulnerable web applications to discover valid accounts without authentication.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The query contains no variables; it is a static SELECT statement targeting the system catalog. | N/A |

## Usage

Inject this query into a SQL injection vulnerability, such as in a UNION SELECT statement: `1' UNION SELECT usename FROM pg_user--`. Execute via tools like sqlmap or manual HTTP requests. Use the output to identify targets for password attacks or privilege escalation. Ensure the injection point allows read access to pg_catalog.

## Detection

- Database logs showing SELECT queries on pg_user from unexpected sources or IPs.
- Web application logs with anomalous SQL patterns in parameters.
- Intrusion detection systems (IDS) alerting on SQL injection signatures involving system table queries.
- Increased error rates from failed injections attempting to access restricted tables.

## Related

- [[procedures/PostgreSQL-User-Enumeration-via-SQL-Injection]]
- [[commands/postgresql-select-users-from-pg-user]]
