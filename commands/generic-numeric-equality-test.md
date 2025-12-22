---
type: command
executor: sql
data: 1337=1337
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

# generic-numeric-equality-test

## Command

```sql
1337=1337
```

## Description

Generic numeric tautology to confirm SQLi vulnerability; works on most DBMS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND 1337=1337 --`

## Expected Output

True response on injectable points.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/generic-string-equality-test]]
