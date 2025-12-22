---
id: 3cd5b493-0bbd-42d0-99c1-01ba9445d372
name: XSS-Filter-Bypass-with-Null-Byte-and-Slash
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.575919+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xss
  - payload
  - bypass
platforms:
  - Web
validated: true
---

# XSS-Filter-Bypass-with-Null-Byte-and-Slash

## Code

```javascript
<object onafterscriptexecute=confirm(0)>
<object onbeforescriptexecute=confirm(0)>

// Bypass onxxx= filter with a null byte/vertical tab
<img src='1' onerror\x00=alert(0) />
<img src='1' onerror\x0b=alert(0) />

// Bypass onxxx= filter with a '/'
<img src='1' onerror/=alert(0) />
```

## Description

This JavaScript/HTML snippet contains multiple XSS payloads designed to bypass filters that block standard event handlers like 'onerror' or 'onafterscriptexecute'. It uses control characters (null byte \x00, vertical tab \x0b) and a slash (/) to obfuscate attribute names, tricking regex-based sanitizers into allowing execution. The payloads trigger a confirm(0) or alert(0) dialog upon rendering, confirming successful injection.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This snippet has no runtime variables; customize the alert/confirm payload as needed (e.g., replace alert(0) with document.cookie). | N/A |

## Usage

Inject these payloads into vulnerable web inputs such as search fields, URL parameters, or form posts in reflected/stored XSS scenarios. Use a proxy like Burp Suite to encode if transmitted over HTTP (e.g., %00 for null byte). Test in a browser to observe execution. This is typically used during web pentesting to validate XSS after identifying filter weaknesses, as part of procedures like [[procedures/Filter-Bypass-with-Exotic-Payloads-for-XSS]].

## Detection

- Web Application Firewalls (WAFs) logging unusual control characters or malformed HTML attributes.
- Client-side: Browser developer tools showing unexpected script execution or network requests from injected code.
- Server-side: Input logs revealing payloads with \x00, \x0b, or '/' in event handlers; enable CSP reporting for violations.

## Related

- [[procedures/Filter-Bypass-with-Exotic-Payloads-for-XSS]]
