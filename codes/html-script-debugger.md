---
id: 90f1a674-6e83-444c-9a58-7a4b1292da86
name: html-script-debugger
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:41.758429+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - debugging
validated: true
---

# html-script-debugger

## Code

```html
<script>debugger;</script>
```

## Description

This HTML-wrapped JavaScript code injects a debugger statement to pause script execution when the page loads, allowing interactive inspection of variables and the environment in browser dev tools during XSS analysis.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; standalone payload | N/A |

## Usage

Inject into vulnerable input fields or parameters in web applications to trigger a breakpoint on page load or interaction. Open dev tools beforehand to step through execution. Useful for understanding the injection context without altering functionality.

## Detection

- Browser dev tools show unexpected breakpoints.
- Script analysis tools flag 'debugger;' statements as potential malicious code.
- CSP violations if inline scripts are restricted.

## Related

- [[procedures/Identify-and-Exploit-XSS-Vulnerabilities]]
