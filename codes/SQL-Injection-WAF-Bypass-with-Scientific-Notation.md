---
type: code
language: sql
verified: true
tags:
  - SQL Injection
  - WAF Bypass
  - Scientific Notation
platforms:
  - Web
  - MySQL
validated: true
---

# SQL-Injection-WAF-Bypass-with-Scientific-Notation

## Code

```sql
' or 1.e('')='
```

## Description

This payload modifies the basic SQL injection tautology by incorporating scientific notation (1.e('') which evaluates to 1=1 in MySQL) to obfuscate the condition. It evades WAFs that block direct ' OR 1=1 patterns while achieving the same authentication bypass effect.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static payload; no substitutions required. | N/A |

## Usage

Use in login forms or input fields after basic payloads are blocked. Test in a proxy tool to modify requests. Ideal for MySQL backends where numeric exponent notation is parsed leniently.

## Detection

- Advanced WAFs analyzing normalized queries for hidden numeric functions.
- Database logs revealing exponent notation in injected strings.
- Anomalous successful logins with malformed input.

## Related

- [[procedures/SQL-Injection-Attack-with-WAF-Bypass-using-Scientific-Notation]]
