---
id: 83f0b3b9-df7b-4b70-afc7-ba0de20f787d
name: mssql-check-db-owner-membership
type: command
executor: sql
data: select is_member('db_owner');
output: null
created_at: '2023-04-06T03:56:20.649845+00:00'
updated_at: '2023-04-10T20:36:41.379800+00:00'
platforms:
  - Windows
tags:
  - mssql
  - privilege-check
verified: true
validated: true
---

# mssql-check-db-owner-membership

## Command

```sql
select is_member('db_owner');
```

## Description

This SQL command checks if the current user is a member of the db_owner database role in MSSQL, which is essential for identifying impersonation opportunities during privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'db_owner' | The fixed role name to check membership for | Yes |

## Examples

### Basic Usage

```sql
select is_member('db_owner');
```

### In Context (via sqlcmd)

```bash
sqlcmd -S server -d database -Q "select is_member('db_owner');"
```

## Expected Output

If the user is a member:

1

If not:

0

Or NULL if the role is invalid.

## Related

- [[procedures/Exploit-MSSQL-Impersonation-for-Privilege-Escalation]]
