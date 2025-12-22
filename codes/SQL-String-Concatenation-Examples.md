---
id: 9c1a26d1-b3a6-4c33-9e1c-8c53fb0e0d5e
name: SQL-String-Concatenation-Examples
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:36.110352+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - sqli
  - concatenation
  - bypass
validated: true
---

# SQL-String-Concatenation-Examples

## Code

```sql
`+HERP
'||'DERP
'+'herp
' 'DERP
'%20'HERP
'%2B'HERP
```

## Description

Examples of SQL string concatenation using operators like +, ||, and spaces, including encoded variants. These allow splitting payloads across inputs to evade detection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static examples; adapt HERP/DERP to target strings | `+HERP |

## Usage

Use in fields where inputs are concatenated, e.g., username: ' || 'admin' to force SQL merging and alter queries.

## Detection

- Query logs with unexpected concatenation operators.
- Response anomalies from merged strings.
- Filter rules for + or || in inputs.

## Related

- [[procedures/SQL-Injection-Entry-Point-Detection]]
