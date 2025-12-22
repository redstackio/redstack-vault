---
id: 3c98c47e-dfb6-4362-ae52-591d32a338a4
name: mssql-check-sysadmin-role-membership
type: command
executor: sql
data: >-
  -- possible roles: sysadmin, serveradmin, dbcreator, setupadmin, bulkadmin,
  securityadmin, diskadmin, public, processadmin

  SELECT is_srvrolemember('sysadmin');
output: null
created_at: '2023-04-06T03:56:34.157965+00:00'
updated_at: '2023-04-10T20:22:47.331484+00:00'
platforms:
  - MSSQL
tags:
  - discovery
  - privileges
verified: true
validated: true
---

# mssql-check-sysadmin-role-membership

## Command

```sql
-- possible roles: sysadmin, serveradmin, dbcreator, setupadmin, bulkadmin, securityadmin, diskadmin, public, processadmin
SELECT is_srvrolemember('sysadmin');
```

## Description

This SQL command uses the is_srvrolemember function to check if the current user is a member of the sysadmin server role in MSSQL, returning 1 for membership or 0 otherwise. It is essential for privilege escalation assessment after SQL injection access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'sysadmin' | Server role name to check (e.g., 'sysadmin', 'securityadmin') | Yes |

## Examples

### Basic Usage

```sql
SELECT is_srvrolemember('sysadmin');
```

### Advanced Usage

Check multiple roles:

```sql
SELECT is_srvrolemember('securityadmin') AS SecurityAdmin, is_srvrolemember('dbcreator') AS DbCreator;
```

## Expected Output

A single integer value: 1 (member, full privileges) or 0 (not a member). Example:

| (No column name) |
|------------------|
| 1 |

A result of 1 indicates sysadmin access for further exploitation.

## Related

- [[procedures/mssql-injection-list-permissions]]
- [[commands/mssql-check-server-permissions]]
