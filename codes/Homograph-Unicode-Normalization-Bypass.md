---
id: 1e963d8c-1853-4e37-b5da-9125f11318e6
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798736+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - homograph
  - unicode
validated: true
---

# Homograph-Unicode-Normalization-Bypass

## Code

```url-payload
https://evil.c℀.example.com . ---> https://evil.ca/c.example.com
http://a.com／X.b.com
```

## Description

Uses homoglyphs and zero-width chars to mimic legit domains, evading visual checks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| evil.c℀.example.com | Homoglyph domain | paypa1.com (with l=1) |

## Usage

/redirect?url=https://evil.c℀om. Resolves maliciously.

## Detection

- Punycode conversion and blacklist homoglyphs.
- User education on visual inspection.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
