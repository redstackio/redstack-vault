---
id: d20c75a8-1b2d-4dc8-86bd-25c7714ec7aa
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.623204+00:00'
updated_at: '2023-04-10T20:21:36.748220+00:00'
tags:
  - xss
  - waf-bypass
  - unicode-encoding
platforms:
  - Web
validated: true
---

# Unicode-Encoded-XSS-Alert-Payload

## Code

```javascript
><h1 onclick=alert('1')>
```

## Description

This JavaScript payload is an obfuscated version of an HTML element (<h1 onclick=alert('1')>) using Unicode escape sequences to evade WAF detection. When injected into a vulnerable web input and decoded by the browser, it creates an h1 element that triggers an alert box displaying '1' upon click, confirming XSS execution. It's useful for testing WAF bypass in cross-site scripting scenarios, particularly against rules that don't normalize Unicode.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| '1' | Message displayed in the alert box; replace with custom text like document.cookie for data exfiltration | 'XSS Success' |

## Usage

Inject this encoded payload into reflected or stored XSS vectors, such as URL parameters, form fields, or HTTP headers in web applications. Use a proxy like Burp Suite to URL-encode the Unicode if needed for transmission (e.g., %u003e for \u003e). Once reflected, click the resulting element to trigger. Commonly used in procedures like [[procedures/JavaScript-Alert-WAF-Bypass]] for initial confirmation before escalating to credential theft or keylogging.

## Detection

- WAF logs showing Unicode sequences in requests without normalization enabled.
- Browser CSP violations or script execution logs detecting onclick handlers.
- JavaScript console errors or network beacons if extended for exfiltration.
- Anomaly detection in web traffic for alert() function calls or unusual HTML attribute patterns.
