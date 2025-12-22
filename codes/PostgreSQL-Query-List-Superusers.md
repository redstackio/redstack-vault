---
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:35.544600+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - postgresql
  - sql-injection
  - database-discovery
validated: true
---

# PostgreSQL-Query-List-Superusers

## Code

```sql
SELECT usename FROM pg_user WHERE usesuper IS TRUE
```

## Description

This SQL code snippet queries the PostgreSQL `pg_user` system table to list all superuser account names. Superusers have unrestricted access to the database, making this query useful for identifying administrative targets in penetration testing or after gaining initial SQL injection access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The query contains no variables; it is a static SELECT statement targeting the `usesuper` flag. | N/A |

## Usage

Inject this query into a vulnerable SQLi parameter in a web application, such as via union-based injection: `' UNION SELECT usename FROM pg_user WHERE usesuper IS TRUE --`. Alternatively, execute directly in a PostgreSQL client (e.g., psql) if database access is obtained. Use during discovery phases to map database privileges before attempting escalation or data collection.

## Detection

- Monitor PostgreSQL logs for SELECT queries on `pg_user` from non-administrative connections.
- Web application logs showing anomalous UNION or subquery patterns in input parameters.
- Intrusion detection signatures for SQLi payloads targeting system catalogs.

## Related

- [[procedures/List-PostgreSQL-Superusers-via-SQL-Injection]]
