---
type: command
executor: sql
data: '@@CPU_BUSY=@@CPU_BUSY'
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

# mssql-cpu-busy-test

## Command

```sql
@@CPU_BUSY=@@CPU_BUSY
```

## Description

Uses MS SQL's @@CPU_BUSY variable for tautology to detect MS SQL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND @@CPU_BUSY=@@CPU_BUSY --`

## Expected Output

True if MS SQL.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/mssql-connections-equality-test]]
