---
id: fe721c3d-7048-420a-8433-f46b4a647582
name: mssql-select-is-srvrolemember-sysadmin
type: command
executor: sql
data: SELECT IS_SRVROLEMEMBER('sysadmin');
output: null
created_at: '2023-04-06T03:56:21.034359+00:00'
updated_at: '2023-04-10T20:36:37.208885+00:00'
platforms:
  - Windows
tags:
  - discovery
  - mssql
  - privileges
verified: true
validated: true
---

# mssql-select-is-srvrolemember-sysadmin

## Command

```sql
SELECT IS_SRVROLEMEMBER('sysadmin');
```

## Description

This command checks if the current or impersonated user is a member of the 'sysadmin' server role, which provides full administrative access to the SQL Server instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'sysadmin' | Fixed role name to check | Yes |

## Examples

### Basic Usage

```sql
SELECT IS_SRVROLEMEMBER('sysadmin');
```

### Check Other Roles

Adapt for other roles like 'db_owner':

```sql
SELECT IS_SRVROLEMEMBER('db_owner');
```

## Expected Output

A single value: 1 (member), 0 (not member), or NULL (unknown).

------
1

## Related

- [[procedures/mssql-impersonation-credential-check]]
- [[commands/mssql-execute-as-login]]
