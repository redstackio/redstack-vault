---
id: e9d6d1d2-2452-499b-8568-d578fc53e491
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.474249+00:00'
updated_at: '2023-04-10T20:21:38.150054+00:00'
tags:
  - xss
  - payload
  - bypass
  - mousedown
platforms:
  - Web
validated: true
---

# XSS-Single-Quote-Bypass-MouseDown-Payload

## Code

```javascript
<a href="" onmousedown="var name = '&#39;;alert(1)//'; alert('smthg')">Link</a>
```

## Description

This JavaScript payload exploits a single quote bypass in an onmousedown event handler by using the HTML entity &#39; to close an existing string in the attribute value. It injects an alert(1) execution upon mouse down interaction, demonstrating arbitrary code execution. The trailing alert('smthg') simulates original code continuation, but the // comment prevents interference. This is a reflected XSS vector suitable for testing filter evasion in web applications that decode HTML entities but block literal quotes.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This payload has no runtime variables; customize the alert(1) to exfiltrate data like document.cookie or location.href. | N/A |

## Usage

Inject this payload into a vulnerable input field that gets reflected into an onmousedown attribute, such as a search box or form parameter in a link. For instance, if the app constructs <a onmousedown="validate('INPUT')">, the payload closes the string with &#39;, executes alert(1), and comments out the rest. Trigger by pressing the mouse button on the link. Use in red team engagements to simulate session theft by replacing alert(1) with a data exfiltration fetch to an attacker server.

## Detection

- Browser developer tools showing unexpected alert dialogs or network requests from event handlers.
- Web Application Firewall (WAF) logs flagging HTML entities like &#39; in attribute contexts or unbalanced quotes.
- Content Security Policy (CSP) violations if inline scripts are restricted, or client-side monitoring for dynamic attribute modifications.

## Related

- [[procedures/Cross-Site-Scripting-Single-Quote-Bypass-on-MouseDown-Event-Handler]]
