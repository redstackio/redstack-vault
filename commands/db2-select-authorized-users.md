---
id: 1edbfc09-6f55-485f-b0da-cb906684770c
name: db2-select-authorized-users
type: command
executor: sql
data: select distinct(authid) from sysibmadm.privileges
output: null
created_at: '2023-04-06T03:56:32.615891+00:00'
updated_at: '2023-04-10T20:22:05.508378+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - enumeration
  - users
verified: true
validated: true
---

# db2-select-authorized-users

## Command

```sql
select distinct(authid) from sysibmadm.privileges
```

## Description

This SQL command queries the DB2 system administrative privileges view to retrieve a distinct list of authorization IDs (users or groups) that have been granted any privileges within the database instance. Use this during discovery phases to map out all potentially authorized entities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| authid | The authorization ID column from the privileges table | Built-in |
| sysibmadm.privileges | The system view containing privilege grants | Built-in |

## Examples

### Basic Usage

```sql
select distinct(authid) from sysibmadm.privileges;
```

### Usage with Ordering

```sql
select distinct(authid) from sysibmadm.privileges order by authid;
```

## Expected Output

A list of unique authorization IDs, for example:

AUTHID
------
DB2ADMIN
USER1
PUBLIC
GROUP1

If no rows are returned, either no privileges are assigned or the executing user lacks access to the view.

## Related

- [[procedures/DB2-User-Enumeration]]
- [[commands/db2-select-schema-owners]]
