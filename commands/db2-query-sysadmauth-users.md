---
id: a63d2ca4-ab5f-4690-9133-f3ab66ccd754
name: db2-query-sysadmauth-users
type: command
executor: sql
data: select name from SYSIBM.SYSUSERAUTH where SYSADMAUTH = 'Y' or SYSADMAUTH = 'G'
output: null
created_at: '2023-04-06T03:56:32.690174+00:00'
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

# db2-query-sysadmauth-users

## Command

```sql
select name from SYSIBM.SYSUSERAUTH where SYSADMAUTH = 'Y' or SYSADMAUTH = 'G'
```

## Description

This SQL command retrieves DB2 users with SYSADM authority, the highest privilege level allowing instance-wide administration. 'Y' indicates direct grant, 'G' indicates grantable authority. Ideal for pinpointing sysadmins in injection-based discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Direct query; no variables, adapt for injection context. | N/A |

## Examples

### Basic Usage

Direct execution in db2 command line:

```sql
select name from SYSIBM.SYSUSERAUTH where SYSADMAUTH = 'Y' or SYSADMAUTH = 'G';
```

### Injected Usage

In SQLi payload: ... UNION [above query] --

## Expected Output

Usernames with SYSADM, e.g.:

NAME
----
DB2INST1
ADMINUSR

Empty result if no SYSADM users or insufficient privileges.

## Related

- [[procedures/DB2-List-DBA-Accounts-via-SQL-Injection]]
- [[commands/db2-query-controlauth-users]]
