---
id: 28835c28-e4d2-4fbc-89b7-c2a8a07e1d58
name: mssql-check-sysadmin-role
type: command
executor: sql
data: SELECT IS_SRVROLEMEMBER('sysadmin')
output: null
created_at: '2023-04-06T03:56:21.083381+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - SQL Server
tags:
  - mssql
  - privilege-check
verified: true
validated: true
---

# mssql-check-sysadmin-role

## Command

```sql
SELECT IS_SRVROLEMEMBER('sysadmin');
```

## Description

This SQL command checks if the current user is a member of the sysadmin server role in Microsoft SQL Server, returning 1 for yes or 0 for no. Use it during privilege assessment to determine escalation potential.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'sysadmin' | Fixed role name to check membership for | Yes |

## Examples

### Basic Usage

```sql
SELECT IS_SRVROLEMEMBER('sysadmin');
```

### Check Other Roles

```sql
SELECT IS_SRVROLEMEMBER('db_owner');
```

## Expected Output

A single integer value:

1  (if sysadmin)

or

0  (if not sysadmin)

## Related

- [[procedures/Nested-Impersonation-Privilege-Escalation-in-SQL-Server]]
