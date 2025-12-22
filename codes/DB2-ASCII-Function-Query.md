---
id: 5e4d999e-0cc3-468d-aa5a-6ce3f965aa5c
name: DB2-ASCII-Function-Query
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:32.965432+00:00'
updated_at: '2023-04-10T20:22:04.479759+00:00'
platforms:
  - Database
  - DB2
tags:
  - SQL Injection
  - ASCII
  - DB2
validated: true
---

# DB2-ASCII-Function-Query

## Code

```sql
select ascii('A') from sysibm.sysdummy1 -- returns 65
```

## Description

This SQL code snippet uses the DB2 ASCII() function to convert a specified character to its numeric ASCII equivalent, querying from the sysibm.sysdummy1 dummy table. It serves as a building block for SQL injection payloads where direct character input is filtered, allowing attackers to reconstruct strings numerically (e.g., chaining multiple ASCII calls to extract passwords character-by-character).

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'A' | The character to convert (hardcoded; replace with dynamic expression like substr(table.column, position, 1) in injections) | 'A' (ASCII 65) |

## Usage

Embed this snippet into a vulnerable SQL injection point, such as a web form parameter: `search=1' UNION SELECT ascii('A') from sysibm.sysdummy1 --`. Use in blind SQLi to infer data by testing ASCII values (e.g., if ASCII > 64, delay response). Commonly delivered via tools like sqlmap or manual Burp Suite requests in red team engagements targeting legacy DB2 applications.

## Detection

- Monitor DB2 logs for queries invoking ASCII() on non-standard inputs or sysibm.sysdummy1.
- WAF rules flagging numeric string constructions or union selects with conversion functions.
- Anomaly detection in query patterns showing repeated single-character extractions.

## Related

- [[procedures/DB2-SQL-Injection-Using-ASCII-Function]]
