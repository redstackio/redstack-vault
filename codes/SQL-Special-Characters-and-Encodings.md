---
id: ab65bd76-1dfa-4af7-822a-6a23256d865a
name: SQL-Special-Characters-and-Encodings
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:36.110165+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - sqli
  - bypass
  - special-characters
validated: true
---

# SQL-Special-Characters-and-Encodings

## Code

```sql
'
%27
"
%22
#
%23
;
%3B
)
Wildcard (*)
&apos;  # required for XML content
```

## Description

This code snippet lists common special characters used in SQL queries along with their URL-encoded equivalents. These are injected into web application inputs to test for SQL injection vulnerabilities by attempting to close or alter SQL statements.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | These are static payloads; substitute directly into HTTP parameters | ' or %27 |

## Usage

Copy individual lines (e.g., ') into URL parameters or form fields during manual testing with tools like Burp Suite or curl. Use in reconnaissance to identify if inputs are concatenated into SQL without escaping.

## Detection

- Web application logs showing unescaped special characters in queries.
- Error pages exposing SQL syntax issues.
- WAF alerts for encoded delimiters like %27.

## Related

- [[procedures/SQL-Injection-Entry-Point-Detection]]
- [[tools/Burp-Suite]]
