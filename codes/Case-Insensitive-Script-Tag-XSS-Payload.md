---
id: 37bb0efe-71ce-478f-8ca8-4bd8be832216
name: Case-Insensitive-Script-Tag-XSS-Payload
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.319734+00:00'
updated_at: '2023-04-10T20:21:39.547530+00:00'
tags:
  - xss
  - payload
  - filter-bypass
platforms:
  - Web
validated: true
---

# Case-Insensitive-Script-Tag-XSS-Payload

## Code

```javascript
<sCrIpt>alert(1)</ScRipt>
```

## Description

This code snippet is an exotic XSS payload that uses mixed-case letters in the '<script>' and '</script>' tags to bypass case-sensitive filters. When injected into a vulnerable web application, it executes the JavaScript alert(1) function, confirming successful code injection and execution in the victim's browser.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(1) | The JavaScript action to execute; can be replaced with other code like document.cookie for data theft | alert(document.domain) |

## Usage

Inject this payload into user-controlled inputs such as search fields, URL parameters, or form fields in a web application vulnerable to reflected or stored XSS. Use it during penetration testing to demonstrate filter evasion. For example, append it to a URL like 'https://target.com/search?q=<sCrIpt>alert(1)</ScRipt>' and observe the alert on page load.

## Detection

- Monitor for mixed-case HTML tags in logs or WAF rules.
- Enable JavaScript execution logging via CSP reports or browser developer tools.
- Scan for anomalous alert() calls or unexpected pop-ups in client-side monitoring.
- Use input sanitization that normalizes case (e.g., toLowerCase()) before validation.

## Related

- [[procedures/Bypass-Case-Sensitive-XSS-Filter-with-Exotic-Payloads]]
