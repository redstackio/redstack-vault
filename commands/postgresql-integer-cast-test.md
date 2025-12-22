---
type: command
executor: sql
data: '5::integer=5'
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

# postgresql-integer-cast-test

## Command

```sql
5::integer=5
```

## Description

Tests PostgreSQL's type cast syntax (::integer).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND 5::integer=5 --`

## Expected Output

True if PostgreSQL.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/postgresql-client-encoding-test]]
