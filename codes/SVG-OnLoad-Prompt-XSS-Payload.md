---
type: code
language: html
verified: true
tags:
  - xss
  - payload
  - svg
platforms:
  - Web
validated: true
---

# SVG-OnLoad-Prompt-XSS-Payload

## Code

```html
<svg/OnLoad="`${prompt()}`">
```

## Description

This HTML snippet creates a malicious SVG element that executes a JavaScript prompt via the onload event when rendered in a browser. It bypasses WAF filters by using SVG's native support for event handlers, avoiding blocked script tags. The template literal with backticks allows potential for dynamic code insertion, but here it simply triggers a basic alert.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This payload has no variables; it is static and self-executing. | N/A |

## Usage

Inject this payload into a reflected XSS vulnerability on a Cloudflare-protected site, such as a search query parameter (e.g., ?q=<svg/OnLoad=...>). When the page loads and renders the input, the SVG triggers the prompt. Use in red team exercises to test WAF efficacy or in pentests to demonstrate client-side execution.

## Detection

- WAF logs showing unfiltered SVG onload attributes in requests.
- Browser CSP violations or JavaScript execution traces in dev tools.
- Client-side monitoring for unexpected prompts or SVG resource loads.

## Related

- [[procedures/Cloudflare-XSS-Bypass-Using-SVG-OnLoad-Prompt]]
