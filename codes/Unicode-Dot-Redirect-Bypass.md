---
id: c795dbbe-8a41-4d0b-8b47-1c84760fcf80
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798431+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - unicode
  - encoding-bypass
validated: true
---

# Unicode-Dot-Redirect-Bypass

## Code

```url-payload
/?redir=google。com
//google%E3%80%82com
```

## Description

Substitutes . with fullwidth Unicode dot to bypass dot blacklists or incomplete normalization.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| google。com | Encoded domain | evil。com |

## Usage

/redirect?url=//google%E3%80%82com. App may pass without normalizing.

## Detection

- Implement Unicode normalization (NFC/NFD) before validation.
- Block non-ASCII in domains.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
