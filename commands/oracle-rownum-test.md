---
type: command
executor: sql
data: ROWNUM=ROWNUM
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

# oracle-rownum-test

## Command

```sql
ROWNUM=ROWNUM
```

## Description

Tests Oracle using the ROWNUM pseudocolumn.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND ROWNUM=ROWNUM --`

## Expected Output

True if Oracle.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/oracle-rawtohex-test]]
