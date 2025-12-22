---
id: fcf04ad7-8d46-48f3-b8ec-1143c3b3dc3b
name: db2-list-databases
type: command
executor: sql
data: select distinct(table_catalog) from sysibm.tables;
output: null
created_at: '2023-04-06T03:56:32.748200+00:00'
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

# db2-list-databases

## Command

```sql
select distinct(table_catalog) from sysibm.tables;
```

## Description

This SQL command queries the DB2 system catalog to list all unique database names (table catalogs) in the current instance. Use it during database reconnaissance to map available databases for further exploration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The query has no parameters; it runs against the connected instance's metadata. | N/A |

## Examples

### Basic Usage

Execute after connecting to the DB2 instance:

```sql
select distinct(table_catalog) from sysibm.tables;
```

### With Export

To save results:

```sql
select distinct(table_catalog) from sysibm.tables; export to dbs.csv OF DEL;
```

## Expected Output

```
TABLE_CATALOG
-------------
SAMPLE
PRODDB
TESTDB

3 record(s) selected.
```

A table showing distinct database names, followed by a record count.

## Related

- [[procedures/Enumerate-DB2-Databases-and-Schemas]]
- [[commands/db2-list-schemas]]
