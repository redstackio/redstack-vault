---
id: aa04c2ca-dd40-4b11-8c16-8a1824ab2a75
name: db2-select-database-privilege-grantees
type: command
executor: sql
data: select grantee from syscat.dbauth
output: null
created_at: '2023-04-06T03:56:32.616002+00:00'
updated_at: '2023-04-10T20:22:05.508378+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - enumeration
  - privileges
  - database
verified: true
validated: true
---

# db2-select-database-privilege-grantees

## Command

```sql
select grantee from syscat.dbauth
```

## Description

This SQL command retrieves grantees of database-level authorities from the DB2 authorization catalog, such as users with CONNECT or CREATETAB privileges. It helps identify accounts with broad database access, though results may include duplicates.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| grantee | The grantee column listing authorized entities | Built-in |
| syscat.dbauth | The catalog view for database authorities | Built-in |

## Examples

### Basic Usage

```sql
select grantee from syscat.dbauth;
```

### Usage with Distinct and Ordering

```sql
select distinct grantee from syscat.dbauth order by grantee;
```

## Expected Output

A list of grantees, potentially with duplicates, for example:

GRANTEE
--------
DB2ADMIN
USER1
USER1
PUBLIC

Cross-reference for uniqueness; errors suggest privilege limitations.

## Related

- [[procedures/DB2-User-Enumeration]]
- [[commands/db2-select-table-privilege-grantees]]
