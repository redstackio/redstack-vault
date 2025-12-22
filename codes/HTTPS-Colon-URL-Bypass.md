---
id: 0e15c26f-0445-4eca-aaa6-9d4bc95e0cf2
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798370+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - https-bypass
  - protocol
validated: true
---

# HTTPS-Colon-URL-Bypass

## Code

```url-payload
https:google.com
```

## Description

Omits // after https: to evade syntax checks, still triggering HTTPS redirect.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| google.com | Target domain | evil.com |

## Usage

http://target.com/redirect?url=https:evil.com. Useful against // -specific blocks.

## Detection

- Validate full protocol syntax in input sanitization.
- Alert on malformed HTTPS URIs.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
