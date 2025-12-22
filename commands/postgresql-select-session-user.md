---
type: command
executor: sql
data: SELECT session_user;
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

# postgresql-select-session-user

## Command

```sql
SELECT session_user;
```

## Description

This SQL command returns the name of the user who owns the current session in PostgreSQL, which may differ from the current user if roles have been assumed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; session-based query | Yes |

## Examples

### Basic Usage

```sql
SELECT session_user;
```

### In Injection Payload

```sql
' OR 1=1; SELECT session_user; --
```

## Expected Output

A single row, e.g.:

```
 session_user 
--------------
 webapp
(1 row)
```

## Related

- [[procedures/PostgreSQL-Current-User-Information-Gathering]]
- [[commands/postgresql-select-current-user]]
