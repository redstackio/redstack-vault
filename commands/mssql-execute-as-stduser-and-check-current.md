---
id: d9dc2174-a84f-4e76-b1d5-9eb6f70bb1cb
name: mssql-execute-as-stduser-and-check-current
type: command
executor: sql
data: |-
  EXECUTE AS LOGIN = 'stduser';
  SELECT SYSTEM_USER;
output: null
created_at: '2023-04-06T03:56:21.083460+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - SQL Server
tags:
  - mssql
  - impersonation
verified: true
validated: true
---

# mssql-execute-as-stduser-and-check-current

## Command

```sql
EXECUTE AS LOGIN = 'stduser';
SELECT SYSTEM_USER;
```

## Description

This SQL command impersonates a standard user ('stduser') and queries the current login context. Use it to test impersonation in preparation for nested escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'stduser' | Target low-privilege login to impersonate | Yes |

## Examples

### Basic Usage

```sql
EXECUTE AS LOGIN = 'stduser';
SELECT SYSTEM_USER;
```

### Nested Example

```sql
EXECUTE AS LOGIN = 'stduser';
SELECT SYSTEM_USER;
EXECUTE AS LOGIN = 'sa';
SELECT SYSTEM_USER;
```

## Expected Output

Impersonation success, then:

stduser

## Related

- [[procedures/Nested-Impersonation-Privilege-Escalation-in-SQL-Server]]
