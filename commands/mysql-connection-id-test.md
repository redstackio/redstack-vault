---
type: command
executor: sql
data: connection_id()=connection_id()
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

# mysql-connection-id-test

## Command

```sql
connection_id()=connection_id()
```

## Description

Tests for MySQL using the connection_id() function, which returns the current connection ID. Use in SQLi to confirm MySQL presence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`id=1' AND connection_id()=connection_id() --`

## Expected Output

Normal response if MySQL; error if not.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/mysql-crc32-test]]
