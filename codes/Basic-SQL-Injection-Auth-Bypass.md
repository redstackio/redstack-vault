---
type: code
language: sql
verified: true
tags:
  - SQL Injection
  - Authentication Bypass
platforms:
  - Web
  - MySQL
validated: true
---

# Basic-SQL-Injection-Auth-Bypass

## Code

```sql
' or ''='
```

## Description

This SQL snippet is a classic tautology-based injection payload used to bypass authentication in vulnerable login forms. It closes the string with a single quote and appends a condition that always evaluates to true (''=''), effectively making the query return all records and granting access without valid credentials.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload with no variables; inject directly into input fields. | N/A |

## Usage

Inject into username/password fields in a web form (e.g., via Burp Suite repeater). Suitable for initial vulnerability testing in SQLi assessments. Combine with URL encoding if needed for GET requests.

## Detection

- WAF signatures for common SQLi patterns like trailing OR conditions.
- Application logs showing queries with unbalanced quotes or tautologies.
- Failed login attempts followed by successful access without credentials.

## Related

- [[procedures/SQL-Injection-Attack-with-WAF-Bypass-using-Scientific-Notation]]
