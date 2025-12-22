---
id: 2a63a663-191b-4208-9ffc-cd4367c1d6be-part1
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.628523+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - sql-injection
  - blind
  - make-set
  - version-extraction
platforms:
  - MySQL
validated: true
---

# MySQL-Blind-MAKE_SET-Version-Length-Payload

## Code

```sql
AND MAKE_SET(YOLO<(SELECT(length(version()))),1)
```

## Description

This SQL snippet is part of a blind injection payload using MySQL's MAKE_SET function to infer the length of the database version string. It creates a boolean condition that alters the application's response based on whether the version length is less than a guessed value (YOLO), enabling iterative length discovery without direct query output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| YOLO | Integer guess for comparison (replace with 1, 2, etc., for binary search) | 10 |

## Usage

Inject this into a vulnerable login form's username field (e.g., via POST request). Observe application responses (success/error) while incrementing YOLO until a flip occurs, indicating the version length. Use in conjunction with character extraction payloads for full version reconstruction. Typically delivered manually via browser or proxy tools during web pentesting.

## Detection

- Monitor application logs for repeated failed logins with anomalous SQL patterns involving MAKE_SET or version() functions.
- WAF rules detecting conditional SQL functions or substring/ascii usage in user inputs.
- Database query logs showing subqueries on system functions like version().

## Related

- [[procedures/MySQL-Blind-Injection-with-MAKE_SET-for-Auth-Bypass]]
