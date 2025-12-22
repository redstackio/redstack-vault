---
id: 2ac649c1-134f-4c90-a017-f8c24695bb0d
name: mssql-get-current-user
type: command
executor: sql
data: SELECT SYSTEM_USER;
output: null
created_at: '2023-04-06T03:56:33.515238+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - SQL Server
tags:
  - mssql
  - discovery
verified: true
validated: true
---

# mssql-get-current-user

## Command

```sql
SELECT SYSTEM_USER;
```

## Description

This SQL command returns the name of the current SQL Server login (system user). Use it to verify context during sessions or after impersonation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | N/A | No |

## Examples

### Basic Usage

```sql
SELECT SYSTEM_USER;
```

### After Impersonation

```sql
EXECUTE AS LOGIN = 'sa';
SELECT SYSTEM_USER;
```

## Expected Output

A single string value, e.g.:

compromised_user

## Related

- [[procedures/Nested-Impersonation-Privilege-Escalation-in-SQL-Server]]
