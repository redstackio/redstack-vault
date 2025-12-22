---
id: a375a42b-a2a1-45d2-8d6b-1f14661d127f
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.741394+00:00'
updated_at: '2023-04-10T20:24:17.381901+00:00'
platforms:
  - Web
tags:
  - sql-injection
  - waf-bypass
  - version-probe
validated: true
---

# SQL-Version-Bypass-Payloads

## Code

```sql
?id=1 and substring(version(),1,1)like(5)
?id=1 and substring(version(),1,1)not in(4,3)
?id=1 and substring(version(),1,1)in(4,3)
?id=1 and substring(version(),1,1) between 3 and 4
```

## Description

These SQL payloads are designed to bypass WAF filters that block equality-based injections by using alternative conditional operators (LIKE, NOT IN, IN, BETWEEN) on the substring of the database version() function. They probe the first digit of the DB version to confirm bypass without triggering rules tuned for '=' or simple comparisons, enabling further injection for data extraction.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| version() | Built-in DB function returning the database version string | MySQL 5.7.32 |
| substring(version(),1,1) | Extracts the first character (version major digit) | '5' |
| 5,4,3 | Numeric values to match against the version digit for conditional testing | 5 (for MySQL 5.x) |

## Usage

Inject these payloads into vulnerable URL parameters (e.g., ?id=) using tools like curl or Burp Suite during web pentesting. Test each to identify which operator evades the WAF, then chain with UNION SELECT for data exfiltration. Used in procedures like [[procedures/SQL-Injection-WAF-Bypass-Using-Version-Checks]] for initial probing.

## Detection

- WAF logs showing blocked requests followed by allowed ones with these operators.
- Database query logs revealing substring(version()) calls from web app IPs.
- Application response anomalies, like conditional content changes based on version probes.
- Network traffic analysis for repeated requests to the same endpoint with varying SQL fragments.

## Related

- [[procedures/SQL-Injection-WAF-Bypass-Using-Version-Checks]]
