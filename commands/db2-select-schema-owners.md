---
id: a15f7b42-250a-469f-9985-7f66404c2cf7
name: db2-select-schema-owners
type: command
executor: sql
data: select distinct(definer) from syscat.schemata
output: null
created_at: '2023-04-06T03:56:32.616023+00:00'
updated_at: '2023-04-10T20:22:05.508378+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - enumeration
  - schemas
verified: true
validated: true
---

# db2-select-schema-owners

## Command

```sql
select distinct(definer) from syscat.schemata
```

## Description

This SQL command extracts unique definer (owner) values from the DB2 schema catalog, listing all schema owners in the database. Schema owners often have elevated control over contained objects, making this useful for identifying administrative users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| definer | The definer/owner column in the schemata table | Built-in |
| syscat.schemata | The catalog view for schema metadata | Built-in |

## Examples

### Basic Usage

```sql
select distinct(definer) from syscat.schemata;
```

### Usage with Additional Details

```sql
select schemaname, definer from syscat.schemata;
```

## Expected Output

A list of unique schema owners, for example:

DEFINER
-------
DB2ADMIN
USER1
APPUSER

Empty results may indicate no custom schemas or access restrictions.

## Related

- [[procedures/DB2-User-Enumeration]]
- [[commands/db2-select-authorized-users]]
