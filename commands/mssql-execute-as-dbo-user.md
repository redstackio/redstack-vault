---
id: db90828a-986e-403a-92ff-e96fa284cf5a
name: mssql-execute-as-dbo-user
type: command
executor: sql
data: execute as user = 'dbo';
output: null
created_at: '2023-04-06T03:56:20.649896+00:00'
updated_at: '2023-04-10T20:36:41.379800+00:00'
platforms:
  - Windows
tags:
  - mssql
  - impersonation
verified: true
validated: true
---

# mssql-execute-as-dbo-user

## Command

```sql
execute as user = 'dbo';
```

## Description

This SQL command impersonates the dbo (database owner) user in the current session, elevating privileges to perform any database operation if the executing user has db_owner membership.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'dbo' | The fixed username to impersonate | Yes |

## Examples

### Basic Usage

```sql
execute as user = 'dbo';
```

### Revert After Use

```sql
revert;
```

## Expected Output

No output on success; error if insufficient permissions (e.g., "The impersonate permission was denied").

## Related

- [[procedures/Exploit-MSSQL-Impersonation-for-Privilege-Escalation]]
