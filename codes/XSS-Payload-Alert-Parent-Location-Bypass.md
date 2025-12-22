---
id: 342c539e-529b-4e19-a296-20476e8fccfe
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.658218+00:00'
updated_at: '2023-04-10T20:21:38.506528+00:00'
tags:
  - xss
  - payload
  - filter-bypass
  - javascript
platforms:
  - Web
  - Browser
validated: true
---

# XSS-Payload-Alert-Parent-Location-Bypass

## Code

```javascript
<div id = "x"></div><script>alert(x.parentNode.parentNode.parentNode.location)</script>
window["doc"+"ument"]
```

## Description

This JavaScript payload is designed for XSS attacks to bypass document blacklists and filters that block direct access to window or document objects. It creates a div element with id 'x' and uses DOM traversal via parentNode to reach the top-level window's location property, displaying it in an alert. The final line uses string concatenation in bracket notation to reference the 'document' object without triggering keyword-based filters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This payload has no substitutable variables; it is self-contained for injection. Adjust the number of parentNode calls based on the specific DOM depth if needed. | N/A |

## Usage

Inject this payload into a vulnerable input field (e.g., URL parameter, form input) on a web page susceptible to reflected or stored XSS. For example, append it to a search query: `https://vulnerable-site.com/search?q=<div id = "x"></div><script>alert(x.parentNode.parentNode.parentNode.location)</script>window["doc"+"ument"]`. When the page loads in the victim's browser, the script executes, alerting the parent location. Use this in red team exercises to demonstrate filter evasion and URL disclosure.

## Detection

- Monitor for unusual alert() calls or DOM manipulations in web logs and client-side scripts.
- Implement client-side scanning with tools like DOMPurify to sanitize inputs and block script tags.
- Use Web Application Firewalls (WAFs) to detect patterns like parentNode traversal or obfuscated object access (e.g., ["doc"+"ument"]).
- Enable browser developer tools or proxy interception (e.g., Burp Suite) to inspect injected payloads during testing.

## Related

- [[procedures/Cross-Site-Scripting-Alert-Parent-Location-Filter-Bypass]]
