---
id: d5f165e8-5762-45f7-92d9-f76422dd86e7
name: html-script-console-log-test
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:41.759363+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - stealth
  - testing
validated: true
---

# html-script-console-log-test

## Code

```html
<script>console.log("Test XSS from the search bar of page XYZ\n".concat(document.domain).concat("\n").concat(window.origin))</script>
```

## Description

HTML payload using console.log to output a test message with domain and origin, simulating stealthy data collection from a specific input like a search bar.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| document.domain | Target domain | 'xyz.com' |
| window.origin | Origin details | 'https://xyz.com' |

## Usage

Target specific inputs like search bars on page XYZ. Check console for output to confirm injection without alerts. Modify log to send data externally for real exploitation.

## Detection

- Console logs with concatenated domain/origin.
- Input sanitization missing for script tags.
- Behavioral monitoring for unusual console activity.

## Related

- [[procedures/Identify-and-Exploit-XSS-Vulnerabilities]]
