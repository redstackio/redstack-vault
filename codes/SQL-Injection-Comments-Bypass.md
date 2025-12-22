---
id: 7780b739-b9df-4983-b2c0-fe9295ef1715
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.673794+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - SQL Injection
  - WAF Bypass
  - Comments
platforms:
  - Web
validated: true
---

# SQL-Injection-Comments-Bypass

## Code

```sql
?id=1/*comment*/and/**/1=1/**/--
```

## Description

This payload uses inline SQL comments (/*comment*/ and /**/) to separate keywords without relying on whitespace, bypassing WAFs that normalize or block spaces. The comments are parsed out by the database, allowing the AND 1=1 condition to execute seamlessly.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /*comment*/ | Single-line comment block | Ignored by parser, acts as separator |
| /**/ | Multi-line comment shorthand | Used between tokens like 'and' and '1=1' |
| -- | Line comment to terminate query | Prevents trailing syntax errors |

## Usage

Inject into URL parameters where whitespace is filtered. Test on login forms or ID fields. If the page behaves as authenticated (due to 1=1), proceed to UNION-based extraction.

## Detection

- Query logs with embedded /* */ patterns.
- WAF alerts on comment usage in inputs.
- Anomalous query execution without spaces.

## Related

- [[procedures/SQL-Injection-Bypassing-Space-Filter-and-Selecting-All-Users]]
