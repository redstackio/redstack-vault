---
id: 86b26ce0-6b5a-48f7-90e1-ec708c9d2468
name: mssql-select-user-name
type: command
executor: sql
data: SELECT user_name()
output: null
created_at: '2023-04-06T03:56:33.515295+00:00'
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

# mssql-select-user-name

## Command

```sql
SELECT user_name()
```

## Description

This SQL command uses the user_name() function to return the current database username in MSSQL, ideal for verifying session context in injection attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; function call | Yes |

## Examples

### Basic Usage

```sql
SELECT user_name()
```

### Union-Based Injection

`UNION SELECT user_name(), NULL --`

## Expected Output

A single value representing the username, e.g.:

```
public
```

## Related

- [[procedures/Retrieve-MSSQL-User-Information-via-SQL-Injection]]
- [[commands/mssql-select-current-user]]
