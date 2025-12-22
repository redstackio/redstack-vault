---
type: command
executor: sql
data: SELECT usename FROM pg_user WHERE usesuper IS TRUE
output: null
created_at: '2023-04-06T03:56:35.544665+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - postgresql
  - sql-injection
verified: true
validated: true
---

# postgresql-select-superusers-from-pg-user

## Command

```sql
SELECT usename FROM pg_user WHERE usesuper IS TRUE;
```

## Description

This SQL command queries the PostgreSQL system catalog `pg_user` to retrieve usernames of all superusers (database administrators with full privileges). It is typically injected via SQL injection vulnerabilities to enumerate high-privilege accounts during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The query has no parameters; it directly filters the `pg_user` table using the `usesuper` boolean flag. | N/A |

## Examples

### Basic Usage

```sql
SELECT usename FROM pg_user WHERE usesuper IS TRUE;
```

Run this in a PostgreSQL client like psql or via injection in a vulnerable application.

### Advanced Usage

To limit output or combine with other queries:

```sql
SELECT usename, usesysid FROM pg_user WHERE usesuper IS TRUE LIMIT 10;
```

## Expected Output

A result set listing superuser names:

```
 usename 
---------
 postgres
 admin   
(2 rows)
```

If no superusers beyond defaults are found, only standard accounts like `postgres` appear. Errors occur if the executing user lacks permission to query `pg_user`.

## Related

- [[procedures/List-PostgreSQL-Superusers-via-SQL-Injection]]
