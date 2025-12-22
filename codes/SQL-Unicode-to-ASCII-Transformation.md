---
id: fa491d26-c01f-4071-9fd5-df10d6914794
name: SQL-Unicode-to-ASCII-Transformation
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:36.110477+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - sqli
  - unicode
  - bypass
validated: true
---

# SQL-Unicode-to-ASCII-Transformation

## Code

```sql
Unicode character U+02BA MODIFIER LETTER DOUBLE PRIME (encoded as %CA%BA) was transformed into U+0022 QUOTATION MARK (" )
Unicode character U+02B9 MODIFIER LETTER PRIME (encoded as %CA%B9) was transformed into U+0027 APOSTROPHE (' )
```

## Description

Describes Unicode characters that normalize to SQL operators like quotes and apostrophes, allowing bypass of strict character filters via encoding.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Static transformation examples; use encodings in payloads | %CA%BA for " |

## Usage

Inject encoded Unicode (e.g., %CA%B9) into inputs; if the database converts it to ', it enables injection similar to direct apostrophe use.

## Detection

- Logs of non-ASCII characters in inputs.
- Normalization events in database audits.
- WAF rules for Unicode ranges like U+02xx.

## Related

- [[procedures/SQL-Injection-Entry-Point-Detection]]
