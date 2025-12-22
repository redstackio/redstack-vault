---
id: d41cc9d5-c3fc-4ee6-a92d-46fd84df9314
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.803571+00:00'
updated_at: '2023-04-10T20:21:44.292405+00:00'
tags:
  - xss
  - payload
  - svg
platforms:
  - Web
validated: true
---

# SVG-Onload-JavaScript-Alert-Payload

## Code

```javascript
<svg onload=alert(1)//
```

## Description

This code snippet is an SVG-based XSS payload that executes JavaScript via the onload event handler when the SVG element is rendered by the browser. It bypasses filters blocking the '>' character by using an unclosed tag and commenting out the rest with '//'. The alert(1) serves as a proof-of-concept to confirm execution; in attacks, it can be replaced with data exfiltration or other malicious code.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(1) | JavaScript code to execute on load | alert(document.cookie) for cookie theft |

## Usage

Inject this payload into vulnerable web application inputs like search fields or forms where output is reflected without proper sanitization. It works in contexts where HTML/SVG is parsed, such as user profiles or error messages. Test in a controlled environment to avoid unintended execution.

## Detection

- Look for SVG elements with onload attributes in user inputs via web application firewall (WAF) rules.
- Enable CSP to block inline event handlers.
- Monitor for unexpected JavaScript execution in browser developer tools or server logs showing anomalous SVG rendering.

## Related

- [[procedures/Bypass-Greater-Than-Filter-with-SVG-Onload-Alert]]
