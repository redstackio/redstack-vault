---
id: 64d2b6ce-9f64-4203-9d26-7c9217e63beb
name: SQL-Comment-Payload-For-Injection
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.923176+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - sql-injection
  - payload
  - comments
validated: true
---

# SQL-Comment-Payload-For-Injection

## Code

```sql
--
/**
```

## Description

This SQL code snippet consists of comment delimiters used in injection payloads to truncate queries or bypass filters in SQLite databases. The single-line comment '--' ignores everything after it on the line, while the multi-line '/* */' can span lines, allowing attackers to neutralize validation checks or hide additional SQL code.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; these are static comment tokens to append to payloads | -- for single-line bypass |

## Usage

Embed in user inputs for web forms, e.g., username field: ' OR 1=1 -- to always true the query. Use in tools like curl or Burp Suite to test SQLite apps. Common in login bypass or data extraction scenarios.

## Detection

- Monitor application logs for queries containing '--' or '/*' in user inputs.
- WAF rules to block inputs with comment patterns.
- Database error logs showing truncated or malformed queries.

## Related

- [[procedures/SQLite-Injection-Using-Comments]]
- [[curl-sqlite-injection-test]]
