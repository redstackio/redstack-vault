---
id: ffe57eb6-272b-4f53-8608-dcd435ebc559
name: db2-list-system-privileges
type: command
executor: sql
data: select * from SYSIBM.SYSUSERAUTH
output: null
created_at: '2023-04-06T03:56:32.653128+00:00'
updated_at: '2023-04-10T20:22:04.113006+00:00'
platforms:
  - Linux
  - Windows
tags:
  - db2
  - enumeration
verified: true
validated: true
---

# db2-list-system-privileges

## Command

```sql
select * from SYSIBM.SYSUSERAUTH;
```

## Description

This command enumerates system authorities for all DB2 users, including SYSADM and SECADM, to discover high-privilege accounts for potential abuse or targeting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Queries all system user authorities. | No |

## Examples

### Basic Usage

```sql
select * from SYSIBM.SYSUSERAUTH;
```

### Filtered for SYSADM

```sql
select * from SYSIBM.SYSUSERAUTH where sysadmauth = 'Y';
```

## Expected Output

Rows with GRANTEE, SYSADMAUTH, etc.:

GRANTEE | SYSADMAUTH | SECADMAUTH
--------|------------|------------
DB2ADMIN| Y          | Y
USER2   | N          | N

Reveals users with system-level control.

## Related

- [[procedures/Enumerate-DB2-User-Privileges]]
- [[commands/db2-show-current-user-database-privileges]]
