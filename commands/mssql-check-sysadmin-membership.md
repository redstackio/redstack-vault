---
id: 3421101e-9bad-4592-ba5b-983ce6c69f51
name: mssql-check-sysadmin-membership
type: command
executor: sql
data: SELECT is_srvrolemember('sysadmin')
output: null
created_at: '2023-04-06T03:56:20.649944+00:00'
updated_at: '2023-04-10T20:36:41.379800+00:00'
platforms:
  - Windows
tags:
  - mssql
  - privilege-check
verified: true
validated: true
---

# mssql-check-sysadmin-membership

## Command

```sql
SELECT is_srvrolemember('sysadmin')
```

## Description

This SQL command verifies if the current session user (potentially post-impersonation) is a member of the sysadmin server role, granting full administrative control over the SQL instance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'sysadmin' | The fixed server role name to check | Yes |

## Examples

### Basic Usage

```sql
SELECT is_srvrolemember('sysadmin')
```

### In Context (via sqlcmd)

```bash
sqlcmd -S server -d database -Q "SELECT is_srvrolemember('sysadmin')"
```

## Expected Output

If member:

1

If not:

0

## Related

- [[procedures/Exploit-MSSQL-Impersonation-for-Privilege-Escalation]]
