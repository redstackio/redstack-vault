---
type: command
executor: sql
data: get_current_ts_config()=get_current_ts_config()
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

# postgresql-ts-config-test

## Command

```sql
get_current_ts_config()=get_current_ts_config()
```

## Description

Tests PostgreSQL's text search configuration function.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND get_current_ts_config()=get_current_ts_config() --`

## Expected Output

True if PostgreSQL.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/postgresql-client-encoding-test]]
