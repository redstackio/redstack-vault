---
type: code
language: html
verified: true
tags:
  - xss
  - payload
  - waf-bypass
  - javascript
platforms:
  - Web
validated: true
---

# HTML-Link-with-Encoded-JavaScript-XSS

## Code

```html
<a href="j&Tab;a&Tab;v&Tab;asc&NewLine;ri&Tab;pt&colon;&lpar;a&Tab;l&Tab;e&Tab;r&Tab;t&Tab;(document.domain)&rpar;">X</a>
```

## Description

This HTML code creates a clickable link that, when rendered in a browser, executes an obfuscated JavaScript payload to alert the current document's domain. The encoding uses HTML entities for tabs (&Tab;), newlines (&NewLine;), and other characters to bypass WAF filters like Cloudflare's, which may not normalize these during inspection. It exploits differences in how the WAF and browser parse the input, allowing XSS execution for potential data theft or further exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload; customize the JavaScript inside (e.g., replace alert(document.domain) with exfiltration code) | N/A |

## Usage

Inject this payload into a reflected XSS vulnerability, such as a URL parameter, search field, or HTML context in user input. For example, append it to a query string: https://target.com/search?q=<payload>. When a victim visits the link or the reflected page loads, clicking 'X' triggers the alert. In attacks, modify to send document.cookie to an attacker-controlled server via XMLHttpRequest.

## Detection

- WAF logs showing blocked but normalized payloads (e.g., 'javascript:alert').
- Browser developer tools revealing unusual script execution or domain access.
- Client-side monitoring for obfuscated href attributes in links.
- Network traffic to unexpected domains from JavaScript.

## Related

- [[procedures/Bypass-Cloudflare-WAF-with-Encoded-XSS-Payload]]
- [[tools/Burp-Suite]]
