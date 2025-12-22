---
type: code
language: sql
verified: true
tags:
  - postgresql
  - sql-injection
  - user-enumeration
platforms:
  - Database
  - PostgreSQL
validated: true
---

# PostgreSQL-User-Enumeration-Queries

## Code

```sql
SELECT user;
SELECT current_user;
SELECT session_user;
SELECT usename FROM pg_user;
SELECT getpgusername();
```

## Description

This SQL code snippet contains a series of queries to enumerate user information in a PostgreSQL database. It retrieves the current user, session user, all cluster users, and alternative username functions. Designed for use in SQL injection scenarios to quickly gather database user details without multiple separate injections.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; direct SQL statements | N/A |

## Usage

Stack these queries in a single injection payload for efficiency, e.g., via sqlmap with `--dbs` or manual Burp Intruder: `' ; [paste queries] ; --`. Ideal for initial database reconnaissance after confirming SQLi vulnerability. Execute in a PostgreSQL client like psql for testing, or inject into web app parameters.

## Detection

- Monitor application logs for stacked SELECT queries or accesses to pg_user table.
- WAF rules matching UNION/ stacked injections with user-related keywords (current_user, session_user).
- Database audit logs showing anomalous SELECTs from application IPs on system catalogs.

## Related

- [[procedures/PostgreSQL-Current-User-Information-Gathering]]
