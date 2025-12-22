---
id: f96432b0-09b2-41e4-99a0-8cb3121f7bad
name: simple-xss-alert-script
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:42.957301+00:00'
updated_at: '2023-04-10T20:21:36.399872+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - javascript
validated: true
---

# simple-xss-alert-script

## Code

```html
<script>alert('1');</script>
```

## Description

This HTML code snippet injects a simple JavaScript alert to test for XSS vulnerabilities. It displays an alert box with the message '1' when executed in a browser context, serving as a proof-of-concept payload for filter bypass testing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| '1' | The message displayed in the alert box | 'XSS Test Successful' |

## Usage

Embed this snippet into an input field, URL parameter, or third-party content that the target site loads. For ES6 bypass, wrap in template literals (e.g., ``<script>`alert(1)`</script>``) and submit via form POST. Use in red team exercises to verify execution after filter evasion.

## Detection

- Browser developer console shows unescaped script tags.
- CSP violations logged if policy blocks inline scripts.
- WAF alerts on <script> tags or alert() function calls.
- Monitor for anomalous popups or JavaScript errors in user sessions.

## Related

- [[procedures/ecmascript6-filter-bypass-script-injection]]
