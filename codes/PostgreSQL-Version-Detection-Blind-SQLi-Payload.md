---
id: 04b32789-fa6e-4025-9fd6-020c455acc49
name: PostgreSQL-Version-Detection-Blind-SQLi-Payload
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.810794+00:00'
updated_at: '2023-04-10T20:23:18.726439+00:00'
platforms:
  - PostgreSQL
tags:
  - sqli
  - blind-injection
  - detection
validated: true
---

# PostgreSQL-Version-Detection-Blind-SQLi-Payload

## Code

```sql
' and substr(version(),1,10) = 'PostgreSQL' and '1  -> OK
' and substr(version(),1,10) = 'PostgreXXX' and '1  -> KO
```

## Description

This SQL snippet provides two boolean-based payloads for blind SQL injection to detect if the target database is PostgreSQL. The first payload checks if the first 10 characters of the version() function match 'PostgreSQL', returning a true condition (OK) if it does. The second uses a mismatched string ('PostgreXXX') for false (KO) to compare responses.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| version() | Built-in PostgreSQL function returning the server version string | 'PostgreSQL 13.5' |
| substr(version(),1,10) | Extracts first 10 characters for comparison | 'PostgreSQL' |

## Usage

Inject these payloads into vulnerable web application parameters (e.g., via POST data in login forms). Observe application responses: normal behavior for true (OK), altered (error/delay) for false (KO). Used in procedures like [[procedures/PostgreSQL-Blind-SQL-Injection-Exploitation]] to confirm DBMS before data extraction.

## Detection

- Web logs showing anomalous SQL patterns with substr() or version() functions.
- WAF alerts on injection keywords like 'and', substr, or version.
- Database query logs capturing conditional substr comparisons.

## Related

- [[procedures/PostgreSQL-Blind-SQL-Injection-Exploitation]]
- [[tools/sqlmap]]
