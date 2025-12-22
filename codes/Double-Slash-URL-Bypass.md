---
id: 44b7c5c0-b351-417d-ba51-f83851169ac2
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798375+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - protocol-bypass
  - relative-url
validated: true
---

# Double-Slash-URL-Bypass

## Code

```url-payload
//google.com
////google.com
```

## Description

Uses double or quadruple slashes to bypass protocol checks, treated as relative but resolving to absolute external sites.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| google.com | Target domain | evil.com |

## Usage

Redirect param: http://target.com/redirect?url=//evil.com. Bypasses http:// blacklists.

## Detection

- Regex for multiple // in URLs.
- Proxy logs showing unexpected absolute resolutions.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
