---
id: 1cbd17a1-6bd3-40a2-b6fe-7d3b85a8292b
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.673867+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - SQL Injection
  - WAF Bypass
  - Parentheses
platforms:
  - Web
validated: true
---

# SQL-Injection-Parentheses-Bypass

## Code

```sql
?id=(1)and(1)=(1)--
```

## Description

This payload leverages parentheses to balance and restructure the SQL expression, creating a tautology without spaces. It modifies the query to always return true, bypassing filters and potentially dumping results.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (1) | Parenthesized literal | Balances the expression |
| and(1)=(1) | Tautology condition | Ensures query returns all matching rows |
| -- | Comment terminator | Ignores remainder of original query |

## Usage

Use in numeric or string parameters vulnerable to injection. Combine with UNION for data exfil. Test by observing if more records than expected are returned.

## Detection

- Logs showing unbalanced or nested parentheses in queries.
- Response anomalies like full table dumps.
- Input validation failures on special characters.

## Related

- [[procedures/SQL-Injection-Bypassing-Space-Filter-and-Selecting-All-Users]]
