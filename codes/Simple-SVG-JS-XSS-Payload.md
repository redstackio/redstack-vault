---
type: code
language: JavaScript
verified: true
tags:
  - xss
  - svg-payload
  - javascript-uri
platforms:
  - Web
validated: true
---

# Simple-SVG-JS-XSS-Payload

## Code

```javascript
javascript:'<svg onload=alert(1)>'
```

## Description

This code snippet is a basic JavaScript URI payload using an SVG element to execute an alert on load. It demonstrates a simple XSS vector via SVG, which can be encoded (e.g., in octal) to bypass filters. The payload creates an inline SVG that triggers JavaScript when rendered, useful for proof-of-concept XSS testing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(1) | The JavaScript to execute; replace with custom code like document.cookie exfiltration | alert(document.cookie) |

## Usage

Inject this as a data URI into vulnerable inputs (e.g., URL parameters, form fields) where user input is reflected without sanitization. For filter bypass, octal-encode the SVG string before use, as shown in related procedures like [[procedures/Octal-Encoded-JavaScript-SVG-XSS-Filter-Bypass]]. Start a listener on your server if exfiltrating data.

## Detection

- Scan inputs for 'javascript:' URIs and SVG tags with onload attributes.
- Monitor browser console for unexpected alerts or network requests to external domains.
- Use CSP headers to block inline SVG execution; log JS events in SVG contexts.
- WAF rules for encoded variants (e.g., \074svg patterns after decoding).

## Related

- [[procedures/Octal-Encoded-JavaScript-SVG-XSS-Filter-Bypass]]
