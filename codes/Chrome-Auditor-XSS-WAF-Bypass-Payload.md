---
id: 657a607b-2ab1-4d98-b2fa-cd9a7483d9de
name: Chrome-Auditor-XSS-WAF-Bypass-Payload
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.455608+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - waf-bypass
  - chrome-auditor
validated: true
---

# Chrome-Auditor-XSS-WAF-Bypass-Payload

## Code

```javascript
</script><svg><script>alert(1)-%26apos%3B
```

## Description

This JavaScript snippet is an obfuscated XSS payload from the Chrome Auditor project (dated August 9, 2018), designed to bypass signature-based WAF detection. It closes a potentially open `<script>` tag, injects an SVG element containing a new script tag, and uses URL encoding (`%26apos%3B` for `&'`) to evade filters. The `alert(1)` serves as a proof-of-concept execution; in real attacks, replace with code to exfiltrate data like cookies.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(1) | Placeholder for JavaScript execution (replace with malicious code, e.g., fetch to send document.cookie) | alert(document.cookie) |

No other variables; the payload is self-contained but can be URL-encoded further for injection.

## Usage

Inject this payload into vulnerable web parameters (e.g., search fields, URL queries) during XSS testing. Deliver via phishing links or direct interaction to execute in the victim's browser. Commonly used in red team engagements to test WAF efficacy against advanced XSS vectors. Reference in procedures like [[procedures/WAF-Bypass-Using-Chrome-Auditor-XSS-Attack-Vector]] for injection steps.

## Detection

- WAF logs showing unblocked SVG or script tag injections.
- Browser developer tools revealing unexpected script execution or DOM modifications.
- Client-side logging of alert() calls or network requests to external domains.
- Endpoint protection platforms (EPP) monitoring for anomalous JavaScript patterns like encoded apostrophes or SVG onload events.

## Related

- [[procedures/WAF-Bypass-Using-Chrome-Auditor-XSS-Attack-Vector]]
- [[Burp-Suite]] (for intercepting and modifying requests)
