---
type: code
language: JavaScript
verified: true
tags:
  - xss
  - payload
  - html-encoding
  - bypass
platforms:
  - Web
validated: true
---

# HTML-Encoded-JavaScript-Alert-Payloads

## Code

```javascript
%26%2397;lert(1)
&#97;&#108;&#101;&#114;&#116;
></script><svg onload=%26%2397%3B%26%23108%3B%26%23101%3B%26%23114%3B%26%23116%3B(document.domain)>
```

## Description

These code snippets are HTML-encoded variants of JavaScript alert payloads designed to bypass web application filters that block direct XSS attempts. The first uses URL encoding combined with decimal entities for 'a' in 'alert', the second employs full decimal entities for 'alert', and the third breaks out of a script tag using entities and SVG onload to execute a domain-revealing alert. They target filters that fail to decode entities before checking for malicious patterns, allowing browser execution upon rendering.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| (None) | These are static payloads; customize by replacing '1' or 'document.domain' with dynamic values like document.cookie for exfiltration. | N/A |

## Usage

Inject these payloads into vulnerable web inputs such as search fields, form parameters, or URL queries during XSS testing. For reflected XSS, append to URLs (e.g., ?q=<encoded_payload>); for stored XSS, submit in comments or profiles. Use in red team engagements to simulate attacks on weak sanitization, or in pentests to demonstrate bypasses. Always test in a controlled environment and obtain authorization.

## Detection

- Application logs showing unusual entity sequences (e.g., multiple &# followed by numbers) in user inputs.
- Browser console errors or JavaScript execution traces indicating decoded scripts.
- WAF alerts for encoded <script> or onload attributes in traffic.
- CSP violations if policy blocks inline SVG or script execution.
- Monitor for alert() calls or unexpected network requests to attacker domains from victim browsers.

## Related

- [[procedures/Bypass-HTML-Encoding-Filters-for-XSS-Injection]]
