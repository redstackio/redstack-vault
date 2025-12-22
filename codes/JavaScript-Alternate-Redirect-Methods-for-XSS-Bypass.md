---
type: code
language: JavaScript
verified: true
tags:
  - xss
  - redirect
  - bypass
  - payload
platforms:
  - Web
validated: true
---

# JavaScript-Alternate-Redirect-Methods-for-XSS-Bypass

## Code

```javascript
location="http://google.com"
document.location = "http://google.com"
document.location.href="http://google.com"
window.location.assign("http://google.com")
window['location']['href']="http://google.com"
```

## Description

This code snippet provides multiple equivalent JavaScript techniques to redirect the current page to a specified URL, designed for use in XSS payloads to bypass filters that block common redirect patterns. Each line represents a different method leveraging the browser's location object, allowing attackers to evade string-based detection while achieving client-side navigation to a malicious site for phishing, drive-by attacks, or exfiltration.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| URL (e.g., "http://google.com") | The target URL for redirection; replace with attacker-controlled domain | "http://attacker.com/phish" |

## Usage

Embed any line of this code within a <script> tag in an XSS payload, injected via vulnerable web inputs (e.g., reflected in search results or stored in user profiles). Test variants sequentially against the target's filter: start with simple assignment ('location=...'), escalate to bracket notation if needed. Use in scenarios like reflected XSS to redirect victims immediately upon page load, or chained with other payloads for delayed execution. Ensure the URL is properly escaped if the injection point requires it.

## Detection

- Browser developer tools or proxy interception showing unexpected client-side redirects from legitimate domains.
- WAF logs indicating blocked 'location' or 'href' keywords, but successful navigation via aliases.
- Content Security Policy (CSP) violations if 'unsafe-inline' is disallowed.
- Endpoint detection for anomalous outbound requests to unknown domains from scripted contexts.
- JavaScript anomaly detection tools scanning for location object manipulations.

## Related

- [[procedures/XSS-Filter-Bypass-via-Alternate-Redirect-Methods]]
