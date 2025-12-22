---
id: 95d8598b-fa51-4665-bf7a-5303991155bd
name: select-usesuper-from-pg-user-current-user
type: command
executor: sql
data: SELECT usesuper FROM pg_user WHERE usename = CURRENT_USER;
output: null
created_at: '2023-04-06T03:56:35.596511+00:00'
updated_at: '2023-04-10T20:23:22.132689+00:00'
platforms:
  - Linux
  - Database
tags:
  - postgresql
  - discovery
verified: true
validated: true
---

# select-usesuper-from-pg-user-current-user

## Command

```sql
SELECT usesuper FROM pg_user WHERE usename = CURRENT_USER;
```

## Description

This SQL command queries the pg_user system catalog to check the 'usesuper' attribute for the current user in PostgreSQL. It provides a boolean flag indicating superuser role membership, ideal for detailed permission auditing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses CURRENT_USER pseudofunction; no explicit parameters | N/A |

## Examples

### Basic Usage

```sql
SELECT usesuper FROM pg_user WHERE usename = CURRENT_USER;
```

### With psql for Remote Check

```bash
psql -h target_host -U current_user -d database_name -c "SELECT usesuper FROM pg_user WHERE usename = CURRENT_USER;"
```

## Expected Output

If superuser:

```
 usesuper 
----------
 t
(1 row)
```

If not:

```
 usesuper 
----------
 f
(1 row)
```

## Related

- [[procedures/Check-PostgreSQL-Current-User-Superuser-Privileges]]
