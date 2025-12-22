---
type: command
executor: sql
data: current_database()=current_database()
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Database
tags:
  - sql-injection
  - fingerprinting
verified: true
validated: true
---

# postgresql-current-database-test

## Command

```sql
current_database()=current_database()
```

## Description

Tests PostgreSQL's current_database() function.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND current_database()=current_database() --`

## Expected Output

True if PostgreSQL.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/postgresql-quote-literal-test]]
