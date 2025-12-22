---
id: 47735b9e-e235-49e9-a25b-f8a970ae5abb
name: Incomplete-HTML-Tag-XSS-Payload
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.399667+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xss
  - payload
  - filter-bypass
  - incomplete-tag
platforms:
  - Web
validated: true
---

# Incomplete-HTML-Tag-XSS-Payload

## Code

```javascript
<img src='1' onerror='alert(0)' <
```

## Description

This code snippet is a malformed HTML tag used as an XSS payload to bypass input filters that only validate complete HTML structures. The <img> tag with a invalid src='1' triggers the onerror event, executing the JavaScript alert(0) when the image fails to load. The trailing < prevents the filter from recognizing it as a complete tag, allowing injection into reflected or stored contexts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(0) | JavaScript code to execute on error; replace with custom payload like document.cookie exfiltration | alert(document.domain) |

## Usage

Inject this payload into vulnerable input fields (e.g., search parameters, comments) on web applications. Use in reflected XSS by appending to URLs or in stored XSS by submitting forms. Test in a browser console or via proxy tools like Burp Suite to confirm execution without triggering filters. Escalate by replacing alert(0) with fetches to attacker servers for data theft.

This payload is used in the [[procedures/Bypass-XSS-Filter-with-Incomplete-HTML-Tag]] procedure during step 2 for proof-of-concept testing.

## Detection

- Monitor for incomplete or malformed HTML tags in logs using regex patterns like <[^>]*\s+on\w+\s*=.
- Implement client-side CSP to block inline event handlers (e.g., script-src 'self').
- WAF rules detecting onerror or onload attributes in user input.
- Browser dev tools showing unexpected JavaScript execution or network requests from onload/onerror events.

## Related

- [[procedures/Bypass-XSS-Filter-with-Incomplete-HTML-Tag]]
