---
id: 986288c5-d99e-4b8c-8aa4-5f4dcce9510f
name: UTF-8-Encoded-CRLF-XSS-Payload
type: code
language: http
verified: true
created_at: '2023-04-06T03:55:55.344884+00:00'
updated_at: '2023-04-06T03:55:55.348211+00:00'
platforms:
  - Web
tags:
  - payload
  - xss
  - crlf
  - injection
validated: true
---

# UTF-8-Encoded-CRLF-XSS-Payload

## Code

```http
%E5%98%8A%E5%98%8Dcontent-type:text/html%E5%98%8A%E5%98%8Dlocation:%E5%98%8A%E5%98%8D%E5%98%BCsvg/onload=alert%28innerHTML%28%29%E5%98%BE
```

## Description

This HTTP payload uses UTF-8 encoding to bypass CRLF filters, injecting a Content-Type header to force HTML rendering, a Location header for splitting, and an SVG element with an onload JavaScript alert that displays the page's inner HTML. It exploits response splitting vulnerabilities to execute XSS in the victim's browser.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload; customize the alert or SVG content if needed for specific targets. | N/A |

## Usage

Embed this encoded string as the value for a reflected input parameter in a POST or GET request to a vulnerable endpoint (e.g., via curl or Burp Suite). When reflected, it splits the response headers and injects the SVG, triggering the alert on page load. Ideal for proof-of-concept in web pentests targeting unfiltered input fields.

## Detection

- WAF rules scanning for encoded control characters (%E5%98%8A, %C0%0D) or anomalous headers in responses.
- Browser developer tools showing unexpected SVG elements or onload events.
- Server logs with malformed HTTP responses containing multiple Content-Type headers.
- Content-Security-Policy (CSP) violations if the injected script attempts execution.

## Related

- [[procedures/CRLF-Filter-Bypass-with-UTF-8-Encoding]]
- [[tools/Burp-Suite]]
