---
id: 1831c435-fd52-423d-8157-f0d6bf3134ed
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.278796+00:00'
updated_at: '2023-04-10T20:21:32.603023+00:00'
platforms:
  - Web
tags:
  - xss
  - csp-bypass
  - payload
validated: true
---

# CSP-Bypass-XSS-Data-URI-Payload

## Code

```javascript
<script src="data:,alert(1)">/</script>
```

## Description

This JavaScript payload exploits XSS vulnerabilities to bypass CSP by using a data URI as the script source. It injects and executes arbitrary code inline, evading policies that block external scripts but allow data: schemes. Primarily used in reflected or stored XSS to demonstrate or perform client-side attacks like alerts, cookie theft, or keylogging.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(1) | Placeholder for JavaScript to execute; replace with malicious code | alert(document.cookie) |

## Usage

Inject this payload into vulnerable inputs (e.g., URL parameters, form fields) on a target website with an XSS flaw. For testing: Append to a reflected endpoint like http://target.com/search?q=<script src="data:,alert(1)">/</script>. In production attacks, modify to exfiltrate data via fetch() or location redirect. Deliver via phishing links or social engineering to lure victims.

## Detection

- Browser CSP violation reports (monitor report-uri directives).
- WAF rules detecting <script> tags or data: URIs in inputs.
- Client-side monitoring for unexpected JavaScript execution or network requests to attacker domains.
- Input sanitization logs showing blocked script injections.

## Related

- [[procedures/CSP-Bypass-via-XSS-Injection]]
