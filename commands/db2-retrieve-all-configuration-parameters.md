---
id: b2add254-46b3-48ce-8414-b2141c140c85
name: db2-retrieve-all-configuration-parameters
type: command
executor: sql
data: 'select name, deferred_value, dbpartitionnum from sysibmadm.dbcfg;'
output: null
created_at: '2023-04-06T03:56:33.205039+00:00'
updated_at: '2023-04-10T20:22:01.198376+00:00'
platforms:
  - Linux
tags:
  - database
  - db2
  - configuration
verified: true
validated: true
---

# db2-retrieve-all-configuration-parameters

## Command

```sql
select name, deferred_value, dbpartitionnum from sysibmadm.dbcfg;
```

## Description

This SQL command retrieves all database configuration parameters stored on disk, including deferred values and partition details, from a DB2 server. It is used to extract sensitive config data like credentials during post-exploitation or discovery phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The query selects all rows from sysibmadm.dbcfg; no parameters needed. | N/A |

## Examples

### Basic Usage

```sql
select name, deferred_value, dbpartitionnum from sysibmadm.dbcfg;
```

### Advanced Usage

Filter for sensitive params like authentication:

```sql
select name, deferred_value, dbpartitionnum from sysibmadm.dbcfg where name like '%auth%';
```

## Expected Output

A comprehensive table of parameter names (e.g., SVCENAME, AUTHENTICATION), their deferred values (e.g., paths, usernames, or 'SYSADM'), and partition numbers. Example:

NAME          | DEFERRED_VALUE | DBPARTITIONNUM
SVCENAME      | db2svc         | 0
AUTHENTICATION| SERVER         | 0

Look for values containing credentials or system paths; errors indicate insufficient privileges.

## Related

- [[procedures/DB2-Configuration-Parameters-Retrieval]]
