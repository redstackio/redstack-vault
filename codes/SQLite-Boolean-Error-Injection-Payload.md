---
id: 97dbaa3b-a426-45c0-a27d-f28381af53c7
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:37.114115+00:00'
updated_at: '2023-04-10T20:24:29.239622+00:00'
tags:
  - sql-injection
  - boolean-based
  - payload
platforms:
  - Linux
  - Web
validated: true
---

# SQLite-Boolean-Error-Injection-Payload

## Code

```sql
AND CASE WHEN [BOOLEAN_QUERY] THEN 1 ELSE load_extension(1) END
```

## Description

This SQL code snippet is a payload for boolean-error based injection in SQLite databases. It uses a CASE WHEN statement to evaluate a boolean condition: if true, it returns 1 (normal response); if false, it attempts to load an extension (triggering an error). This difference allows attackers to infer data by observing application responses (normal vs. error pages).

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| [BOOLEAN_QUERY] | The conditional SQL expression to test (e.g., (1=1) or ASCII(SUBSTR(username,1,1))>64) | (SELECT COUNT(*) FROM users > 0) |

## Usage

Inject this payload into a vulnerable SQLite query parameter in a web application or API. Start with simple true/false tests to confirm, then use it for data extraction by crafting boolean queries that probe database contents character-by-character or field-by-field. Typically delivered via HTTP requests (e.g., using curl or Burp Suite) to endpoints like search forms or logins.

## Detection

- Monitor application logs for SQLite errors related to load_extension calls or unusual CASE WHEN patterns in queries.
- Enable SQL query logging to detect concatenated user inputs with boolean logic.
- Web application firewalls can flag payloads containing 'CASE WHEN', 'load_extension', or repetitive error-triggering requests.
- Anomalous response patterns: Frequent 500 errors alternating with normal responses indicate probing.

## Related

- [[procedures/Perform-SQLite-Boolean-Error-Based-Injection]]
