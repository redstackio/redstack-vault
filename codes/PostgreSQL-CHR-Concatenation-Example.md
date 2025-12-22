---
id: 834f31bc-4323-443f-830c-be90a6023e88
name: PostgreSQL-CHR-Concatenation-Example
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.076721+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - sql-injection
  - bypass
  - concatenation
validated: true
---

# PostgreSQL-CHR-Concatenation-Example

## Code

```sql
SELECT CHR(65)||CHR(66)||CHR(67);
```

## Description

This SQL code snippet demonstrates using PostgreSQL's CHR function to convert ASCII codes to characters and concatenate them with the || operator. It is useful in SQL injection scenarios to bypass web application filters that block direct input of special characters like quotes or operators, allowing construction of malicious strings dynamically.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; hardcoded ASCII values (65=A, 66=B, 67=C) | N/A |

## Usage

Inject this into a vulnerable parameter to test string building, e.g., in a union select to return constructed strings. Extend by using CHR(39) for single quotes in payloads like CHR(39)||' OR '||CHR(39) to form ' OR '. Commonly used in blind injections where direct chars are filtered.

## Detection

- Database logs showing queries with multiple CHR calls or unusual ASCII concatenations.
- WAF rules matching patterns like CHR\(\d+\).*\|\|.
- Anomalous string outputs in application responses.

## Related

- [[procedures/PostgreSQL-Command-Execution-via-Injection]]
