---
id: 0904e875-6ef0-4637-a3cc-a814e86beeef
name: postgresql-list-users-and-privileges
type: command
executor: sql
data: 'SELECT usename, usecreatedb, usesuper, usecatupd FROM pg_user'
output: null
created_at: '2023-04-06T03:56:35.569010+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Database
tags:
  - postgresql
  - enumeration
  - privileges
verified: true
validated: true
---

# postgresql-list-users-and-privileges

## Command

```sql
SELECT usename, usecreatedb, usesuper, usecatupd FROM pg_user;
```

## Description

This SQL command queries the PostgreSQL pg_user system catalog to retrieve a list of all database users along with key privilege indicators. It is used during reconnaissance to identify superusers or privileged accounts that can be targeted for escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| usename | Username of the database user | Built-in (queried) |
| usecreatedb | Boolean: Can user create databases? (t=true, f=false) | Built-in (queried) |
| usesuper | Boolean: Is user a superuser? (t=true, f=false) | Built-in (queried) |
| usecatupd | Boolean: Can user update system catalogs? (t=true, f=false) | Built-in (queried) |

## Examples

### Basic Usage

Execute directly in psql:

```sql
SELECT usename, usecreatedb, usesuper, usecatupd FROM pg_user;
```

### Via Injection

In a vulnerable query: `SELECT * FROM users WHERE id=1; SELECT usename, usesuper FROM pg_user; --`

## Expected Output

```
 usename  | usecreatedb | usesuper | usecatupd 
----------+-------------+----------+-----------
 postgres | t           | t        | t
 appuser  | f           | f        | f
(2 rows)
```

This shows 'postgres' as a superuser. Look for 't' values to identify escalation targets.

## Related

- [[procedures/PostgreSQL-Privilege-Escalation-via-User-Enumeration]]
- [[commands/postgresql-connect]]
