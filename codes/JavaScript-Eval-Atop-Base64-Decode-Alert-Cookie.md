---
type: code
language: javascript
verified: true
created_at: '2023-04-06T03:56:42Z'
updated_at: '2023-04-10T20:21:41Z'
platforms:
  - Web
tags:
  - xss
  - base64
  - data-encoding
validated: true
---

# JavaScript-Eval-Atop-Base64-Decode-Alert-Cookie

## Code

```javascript
<script>eval(atob("YWxlcnQoZG9jdW1lbnQuY29va2llKQ=="))<script>
```

## Description

This snippet decodes a base64-encoded JavaScript payload using atob() and executes it with eval(), targeting document.cookie to steal session data. The base64 obfuscates dots and keywords, evading plaintext filters. Note: The closing tag is malformed (<script> instead of </script>), which may cause parsing issues but is preserved for exact replication.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| "YWxlcnQoZG9jdW1lbnQuY29va2llKQ==" | Base64-encoded JS string (alert(document.cookie)); replace with custom encoded payload | YWxlcnQoMSk= for alert(1) |

## Usage

Encode your target JS first (e.g., using [[commands/base64-encode-xss-payload]]), then inject into XSS vectors. Use for data exfiltration in filtered apps; chain with decimal IPs for internal fetches.

## Detection

- JavaScript errors from atob() on invalid base64 or eval() execution.\n- Network logs showing base64 patterns in inputs.\n- Alert popups with cookie data or CSP blocks on eval/atob.\n
## Related

- [[procedures/XSS-Dot-Filter-Bypass-Using-Exotic-Payloads]]
