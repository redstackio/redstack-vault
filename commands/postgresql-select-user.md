---
type: command
executor: sql
data: SELECT user;
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

# postgresql-select-user

## Command

```sql
SELECT user;
```

## Description

This SQL command is an alias for SELECT current_user; in PostgreSQL, returning the name of the current database user for quick verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Simple alias query | Yes |

## Examples

### Basic Usage

```sql
SELECT user;
```

### In Injection Payload

```sql
' OR 1=1; SELECT user; --
```

## Expected Output

A single value, e.g.:

```
  user  
--------
 postgres
(1 row)
```

## Related

- [[procedures/PostgreSQL-Current-User-Information-Gathering]]
- [[commands/postgresql-select-current-user]]
