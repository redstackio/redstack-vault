---
id: f81b55c4-5d6d-45f1-b291-f5fba971dba6
name: mssql-select-user
type: command
executor: sql
data: SELECT user
output: null
created_at: '2023-04-06T03:56:33.515437+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Database
  - MSSQL
tags:
  - sql-injection
  - discovery
verified: true
validated: true
---

# mssql-select-user

## Command

```sql
SELECT user
```

## Description

This SQL command queries the 'user' variable in MSSQL, equivalent to CURRENT_USER, to confirm the database user in injection scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; variable reference | Yes |

## Examples

### Basic Usage

```sql
SELECT user
```

### Batched Injection

`'; SELECT user; --`

## Expected Output

The current database user, e.g.:

```
dbo
```

## Related

- [[procedures/Retrieve-MSSQL-User-Information-via-SQL-Injection]]
- [[commands/mssql-select-current-user]]
