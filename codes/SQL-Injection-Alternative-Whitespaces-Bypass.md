---
id: 884da371-8a13-4f5b-a325-b911ffedd7f1
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:36.673694+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - SQL Injection
  - WAF Bypass
  - Whitespace Alternatives
platforms:
  - Web
validated: true
---

# SQL-Injection-Alternative-Whitespaces-Bypass

## Code

```sql
?id=1%09and%091=1%09--
?id=1%0Dand%0D1=1%0D--
?id=1%0Cand%0C1=1%0C--
?id=1%0Band%0B1=1%0B--
?id=1%0Aand%0A1=1%0A--
?id=1%A0and%A01=1%A0--
```

## Description

This code snippet provides URL-encoded SQL injection payloads using alternative whitespace characters (tab, carriage return, form feed, vertical tab, line feed, non-breaking space) to bypass WAF filters that block standard spaces. Each payload tests a tautology (AND 1=1) to confirm injection without altering query logic.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| %09 | Tab character encoding | Used as whitespace separator |
| %0D | Carriage return | Alternative line break |
| %0C | Form feed | Page break character |
| %0B | Vertical tab | Line tabulation |
| %0A | Line feed | Newline character |
| %A0 | Non-breaking space | HTML entity space |

## Usage

Append these payloads directly to vulnerable URL parameters (e.g., http://target.com/vuln.php?id= followed by the payload). Use in reconnaissance to test for space-filtered SQLi. Ideal for initial validation before escalating to data extraction.

## Detection

- WAF logs showing URL-decoded payloads with non-standard whitespace.
- Database query logs revealing concatenated queries with unusual separators.
- Application errors or unexpected tautology results in response times.

## Related

- [[procedures/SQL-Injection-Bypassing-Space-Filter-and-Selecting-All-Users]]
