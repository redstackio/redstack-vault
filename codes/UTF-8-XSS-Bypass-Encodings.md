---
id: 9043124d-06e0-4824-b33f-60b78ae9aa9b
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.055392+00:00'
updated_at: '2023-04-10T20:21:30.582987+00:00'
tags:
  - xss
  - bypass
  - utf-8
platforms:
  - Web
validated: true
---

# UTF-8-XSS-Bypass-Encodings

## Code

```javascript
< = %C0%BC = %E0%80%BC = %F0%80%80%BC
> = %C0%BE = %E0%80%BE = %F0%80%80%BE
' = %C0%A7 = %E0%80%A7 = %F0%80%80%A7
" = %C0%A2 = %E0%80%A2 = %F0%80%80%A2
" = %CA%BA
' = %CA%B9
```

## Description

This code snippet provides a reference mapping of special characters commonly used in XSS payloads to their overlong UTF-8 encoded forms. These encodings can be used to construct payloads that bypass filters expecting standard single-byte URL encodings, allowing injection of tags like <script> or attributes like onclick="..." in web applications.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static reference; no variables to substitute. Use the encodings directly in URL or form payloads. | N/A |

## Usage

Incorporate these encodings into XSS payloads during testing or attacks. For instance, replace '<' with %C0%BC in a script tag to evade basic WAF rules. Deliver via reflected inputs, stored comments, or DOM manipulations. Reference this in procedures like [[procedures/UTF-8-Bypass-for-Cross-Site-Scripting]] when crafting obfuscated JavaScript injections.

## Detection

- Monitor for overlong UTF-8 sequences in logs (e.g., %C0%BC instead of %3C) using regex patterns like /%[C0-E0]%[80-BF]/.
- Enable strict UTF-8 validation in web servers (e.g., Apache mod_security rules) to reject invalid byte sequences.
- Browser behavior: Look for unexpected script execution from encoded inputs; use CSP to block inline JS.

## Related

- [[procedures/UTF-8-Bypass-for-Cross-Site-Scripting]]
