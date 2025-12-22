---
id: 43e191c3-e247-4840-b003-b896b0ad2621
type: code
language: SQL
verified: true
created_at: '2023-04-06T03:56:35.372039+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - sql-injection
  - comments
validated: true
---

# PostgreSQL-Comment-Injection-Snippet

## Code

```sql
--
/**/  
```

## Description

This SQL snippet uses PostgreSQL's single-line comment (--) followed by a multi-line comment (/* */) to bypass input filters in injection scenarios. It can be appended to user input to comment out the remainder of the original query, allowing arbitrary SQL execution without triggering keyword-based detections.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static comment snippet; customize by prepending payload like ' OR 1=1 | ' OR 1=1 -- |

## Usage

Embed in vulnerable parameters, e.g., username=admin' -- to bypass login checks. Use in tools like SQLMap or manual requests via Burp Suite. Ideal for WAF bypass where direct injections are blocked but comments are overlooked.

## Detection

- Monitor query logs for unusual comment usage or syntax errors from incomplete queries.
- WAF rules detecting -- or /* */ in inputs.
- Database audit logs showing altered query structures.

## Related

- [[procedures/PostgreSQL-Injection-Using-Comments]]
- [[tools/sqlmap]]
