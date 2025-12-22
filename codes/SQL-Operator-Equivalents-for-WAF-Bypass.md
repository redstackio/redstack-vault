---
id: 5e59011f-b6db-4d50-8b93-20aff8e846aa
name: SQL-Operator-Equivalents-for-WAF-Bypass
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:36.767607+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - sqli
  - waf-bypass
  - operator-substitution
validated: true
---

# SQL-Operator-Equivalents-for-WAF-Bypass

## Code

```sql
AND   -> &&
OR    -> ||
=     -> LIKE,REGEXP, BETWEEN, not < and not >
> X   -> not between 0 and X
WHERE -> HAVING
```

## Description

This reference maps common SQL operators to equivalent alternatives that can substitute in injection payloads to evade WAF keyword filters. For example, '&&' functions like 'AND' in many databases, avoiding direct blocks.

## Parameters

None - static reference mappings.

## Usage

Incorporate into SQLi payloads during testing, e.g., replace 'AND' with '&&' in a tautology: ?id=1 && 1=1#. Combine with case variations for layered obfuscation. Applicable in tools like sqlmap or manual Burp requests.

## Detection

- Query logs showing non-standard operators like '&&' or 'HAVING' in WHERE contexts.
- WAF anomalies from unmatched but equivalent patterns.
- Increased error rates from malformed but evasive queries.

## Related

- [[procedures/SQL-Injection-WAF-Bypass-using-Case-Modification]]
