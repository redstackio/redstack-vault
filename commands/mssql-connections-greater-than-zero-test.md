---
type: command
executor: sql
data: '@@CONNECTIONS>0'
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

# mssql-connections-greater-than-zero-test

## Command

```sql
@@CONNECTIONS>0
```

## Description

Checks if there are active connections in MS SQL using the @@CONNECTIONS variable. Inject to test for MS SQL (assumes connections >0).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND @@CONNECTIONS>0 --`

## Expected Output

True if MS SQL with connections; false or error otherwise.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/mssql-connections-equality-test]]
