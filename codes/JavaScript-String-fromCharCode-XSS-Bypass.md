---
id: 23e4c600-2772-4f5a-9908-474b70639f8e
type: code
name: JavaScript-String-fromCharCode-XSS-Bypass
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.421127+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xss
  - filter-bypass
  - ascii-conversion
platforms:
  - Web
validated: true
---

# JavaScript-String-fromCharCode-XSS-Bypass

## Code

```javascript
String.fromCharCode(88,83,83)
```

## Description

This JavaScript code snippet uses the String.fromCharCode() method to convert comma-separated Unicode values (88 for 'X', 83 for 'S', 83 for 'S') into the string 'XSS'. It is designed for bypassing XSS filters that block literal strings by reconstructing the payload numerically at runtime, allowing injection into script contexts to execute further malicious code like alerts or data theft.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 88,83,83 | Hardcoded Unicode values for characters (no substitution needed for basic 'XSS') | N/A |

## Usage

Inject this snippet into a vulnerable input that reflects into a <script> tag or event handler, e.g., `<script>if(String.fromCharCode(88,83,83)=="XSS"){alert(1);}</script>`. It executes in the browser to form the string and trigger actions. Extend by chaining to full payloads, such as encoding an entire alert or beacon for credential exfiltration in reflected/stored XSS scenarios.

## Detection

- Scan for String.fromCharCode() invocations in dynamic JS code via static analysis tools like ESLint or browser dev tools.
- Monitor for unusual string constructions in user inputs using WAF rules targeting numeric sequences followed by fromCharCode.
- Enable JS error logging or CSP reporting to detect eval-like behaviors from encoded payloads.

## Related

- [[procedures/ASCII-Conversion-XSS-Filter-Bypass]]
