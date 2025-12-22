---
id: 0df1733b-2ed8-4022-8844-5f72c52724be
name: mssql-get-original-login
type: command
executor: sql
data: SELECT ORIGINAL_LOGIN();
output: null
created_at: '2023-04-06T03:56:21.083547+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - SQL Server
tags:
  - mssql
  - discovery
verified: true
validated: true
---

# mssql-get-original-login

## Command

```sql
SELECT ORIGINAL_LOGIN();
```

## Description

This SQL command returns the original login that initiated the connection, ignoring any impersonations. Use it to track true session origins for persistence or evasion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```sql
SELECT ORIGINAL_LOGIN();
```

### After Nested Impersonation

```sql
EXECUTE AS LOGIN = 'stduser';
EXECUTE AS LOGIN = 'sa';
SELECT ORIGINAL_LOGIN();
```

## Expected Output

A single string value, e.g.:

original_compromised_user

## Related

- [[procedures/Nested-Impersonation-Privilege-Escalation-in-SQL-Server]]
