---
type: command
executor: sql
data: pg_client_encoding()=pg_client_encoding()
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

# postgresql-client-encoding-test

## Command

```sql
pg_client_encoding()=pg_client_encoding()
```

## Description

Uses PostgreSQL's pg_client_encoding() to get client encoding for tautology test.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND pg_client_encoding()=pg_client_encoding() --`

## Expected Output

True if PostgreSQL.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/postgresql-integer-cast-test]]
