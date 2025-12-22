---
id: 79824cef-56d1-4d00-b230-466ef694bcf7
name: CSRF-JSON-GET-Request-Payload
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:55:56.209777+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - csrf
  - payload
  - javascript
validated: true
---

# CSRF-JSON-GET-Request-Payload

## Code

```html
<script>
var xhr = new XMLHttpRequest();
xhr.open("GET", "http://www.example.com/api/currentuser");
xhr.send();
</script>
```

## Description

This HTML code snippet contains a JavaScript payload that performs a CSRF attack by sending an unauthorized GET request to a JSON API endpoint using XMLHttpRequest. When loaded in a victim's browser while they are authenticated to the target site, it leverages the session cookies to fetch sensitive data without user interaction. The response can be captured or exfiltrated for further use in attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Target URL in xhr.open | The vulnerable JSON API endpoint | http://target.com/api/currentuser |

## Usage

Embed this script in an HTML file (e.g., malicious.html) and host it on an attacker-controlled server using a tool like Python's http.server. Lure the victim to visit the page via phishing or social engineering while they are logged into the target application. The script executes on page load, sending the request. To exfiltrate the response, extend the script with xhr.onreadystatechange to send xhr.responseText to an attacker endpoint.

## Detection

- Browser developer tools or network logs showing unexpected cross-origin GET requests to API endpoints.
- Web Application Firewall (WAF) rules detecting requests without CSRF tokens or from untrusted referers.
- Server-side logging of API calls with mismatched Origin or Referer headers.
- Endpoint protection monitoring for anomalous JavaScript execution in user sessions.

## Related

- [[procedures/Perform-CSRF-Attack-via-JSON-GET-Request]]
