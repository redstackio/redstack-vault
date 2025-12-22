---
id: 60bd3a5e-5875-41f6-b78f-37eb5f40cf7e
name: mssql-select-system-user
type: command
executor: sql
data: SELECT SYSTEM_USER;
output: null
created_at: '2023-04-06T03:56:21.034262+00:00'
updated_at: '2023-04-10T20:36:37.208885+00:00'
platforms:
  - Windows
tags:
  - discovery
  - mssql
verified: true
validated: true
---

# mssql-select-system-user

## Command

```sql
SELECT SYSTEM_USER;
```

## Description

This SQL command queries the current system user (login) under which the SQL Server session is executing. It is used to identify the authentication context in discovery phases of an attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; executes in current context | Yes |

## Examples

### Basic Usage

```sql
SELECT SYSTEM_USER;
```

### In a Script

Use within a larger query to log context before privilege changes.

## Expected Output

A single row with the login name, e.g.:

SYSTEM_USER
-----------
domain\\lowprivuser

## Related

- [[procedures/mssql-impersonation-credential-check]]
- [[commands/mssql-select-original-login]]
