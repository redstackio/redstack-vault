---
type: code
language: html
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - xss
  - payload
  - waf-bypass
platforms:
  - Web
validated: true
---

# XSS-JavaScript-URI-with-Encoded-Script

## Code

```html
<a href=javas&#99;ript:alert(1)>
```

## Description

This HTML snippet is an XSS payload designed to bypass WAF filters by using HTML entity encoding on the 'javascript' URI scheme. The '&#99;' encodes the letter 'c', evading pattern-matching rules while allowing browsers to decode and execute the javascript:alert(1) when the link is clicked or rendered. It targets reflected or stored XSS in unescaped data fields.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload; customize the alert(1) for specific actions like data exfiltration. | N/A |

## Usage

Inject this payload into a vulnerable input field on a Wordfence-protected site (e.g., via a form submission). Upon rendering, it appears as a harmless link but executes JS on interaction. Used in procedures like [[procedures/Wordfence-WAF-Bypass-via-XSS-Vulnerability]] for proof-of-concept bypass. Extend by replacing alert(1) with malicious code, such as sending document.cookie to an attacker server.

## Detection

- WAF logs showing entity-encoded URIs or javascript: patterns after decoding.
- Browser developer tools revealing unexpected alert() calls or network requests from JS.
- CSP violations if policy blocks inline JS or unsafe-inline.
- Client-side monitoring for DOM manipulations inserting encoded href attributes.

## Related

- [[procedures/Wordfence-WAF-Bypass-via-XSS-Vulnerability]]
