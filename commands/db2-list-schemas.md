---
id: 4caf0b81-1e1d-48f0-93a0-58e46a98d405
name: db2-list-schemas
type: command
executor: sql
data: SELECT schemaname FROM syscat.schemata;
output: null
created_at: '2023-04-06T03:56:32.748248+00:00'
updated_at: '2023-04-10T20:21:59.786968+00:00'
platforms:
  - Database
  - DB2
tags:
  - enumeration
  - discovery
verified: true
validated: true
---

# db2-list-schemas

## Command

```sql
SELECT schemaname FROM syscat.schemata;
```

## Description

This SQL command retrieves all schema names from the DB2 system catalog, helping identify namespaces for database objects during discovery phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The query has no parameters; it operates on the connected database's schemata. | N/A |

## Examples

### Basic Usage

Run in a connected DB2 session:

```sql
SELECT schemaname FROM syscat.schemata;
```

### With Export

To output to file:

```sql
SELECT schemaname FROM syscat.schemata; export to schemas.csv OF DEL;
```

## Expected Output

```
SCHEMANAME
----------
SYSIBM
SYSPUBLIC
DB2INST1
USERAPP

4 record(s) selected.
```

A table listing schema names with a record count.

## Related

- [[procedures/Enumerate-DB2-Databases-and-Schemas]]
- [[commands/db2-list-databases]]
