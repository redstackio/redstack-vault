---
id: 1815b773-1921-444b-b632-64c7d2ba50e7
name: SQL-Injection-Payloads-Case-Variation
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:36.767510+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - sqli
  - waf-bypass
  - case-modification
validated: true
---

# SQL-Injection-Payloads-Case-Variation

## Code

```sql
?id=1 AND 1=1#
?id=1 AnD 1=1#
?id=1 aNd 1=1#
```

## Description

These SQL injection payloads use case variations of the 'AND' keyword to bypass WAFs that filter only specific capitalizations. The tautology '1=1' tests for vulnerability by forcing a true condition, with '#' commenting out the rest of the query.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| id | Name of the vulnerable URL parameter | id |

## Usage

Append to vulnerable GET parameters in web requests (e.g., via curl or Burp Suite). Test each variation; use in blind SQLi to confirm bypass before escalating to data extraction.

## Detection

- WAF logs showing partial keyword matches or allowed mixed-case queries.
- Database logs with anomalous tautology conditions.
- Application responses leaking error messages or full datasets.

## Related

- [[procedures/SQL-Injection-WAF-Bypass-using-Case-Modification]]
