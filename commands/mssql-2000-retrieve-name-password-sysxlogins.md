---
type: command
executor: sql
data: 'SELECT name, password FROM master..sysxlogins'
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

# mssql-2000-retrieve-name-password-sysxlogins

## Command

```sql
SELECT name, password FROM master..sysxlogins
```

## Description

Retrieves usernames and binary password data from the sysxlogins table in MSSQL 2000. Use this to dump raw credentials before hex conversion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Queries master database system table | No |

## Examples

### Basic Usage

```sql
SELECT name, password FROM master..sysxlogins
```

## Expected Output

name    password
sa      0x010100A29B6D5C0D7F5F5D5C0D7F5F5D...

## Related

- [[procedures/MSSQL-Server-Password-Hash-Extraction-and-Cracking]]
