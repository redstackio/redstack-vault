---
id: 2a2e05a9-6fc8-43d8-b0f1-f35e50c431ca
name: db2-select-table-privilege-grantees
type: command
executor: sql
data: select distinct(grantee) from sysibm.systabauth
output: null
created_at: '2023-04-06T03:56:32.616080+00:00'
updated_at: '2023-04-10T20:22:05.508378+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - enumeration
  - privileges
  - table
verified: true
validated: true
---

# db2-select-table-privilege-grantees

## Command

```sql
select distinct(grantee) from sysibm.systabauth
```

## Description

This SQL command queries the DB2 table authorization view to list unique grantees of table-level privileges (e.g., SELECT, INSERT). It provides detailed insights into object-specific access, more accurate than broader queries for pinpointing data access rights.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| grantee | The grantee column for table privileges | Built-in |
| sysibm.systabauth | The system view for table authorizations | Built-in |

## Examples

### Basic Usage

```sql
select distinct(grantee) from sysibm.systabauth;
```

### Usage with Privilege Details

```sql
select grantee, control, selectauth from sysibm.systabauth;
```

## Expected Output

A distinct list of grantees, for example:

GRANTEE
--------
USER1
APPUSER
DB2ADMIN

No results may mean no explicit table grants or access denial.

## Related

- [[procedures/DB2-User-Enumeration]]
- [[commands/db2-select-database-privilege-grantees]]
