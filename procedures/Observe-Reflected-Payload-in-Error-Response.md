---
tags:
  - xss
  - reflection
  - self-xss
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Browsershots-org]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: d673e5c8-8d38-4cac-a9b1-e06833751eda
created_at: '2025-12-14T03:15:41.421Z'
updated_at: '2025-12-14T03:15:41.421Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-Reflected-Payload-in-Error-Response

## Summary

This procedure captures and verifies the execution of the reflected XSS payload in the server's error response, confirming the vulnerability in a proxied browser setup.

## Description

After injecting the payload, the server responds with an unescaped error message including the invalid method, allowing the HTML/JS to render and execute in the browser viewing the response. Due to browser security, this only works in proxies like Burp Suite; standard contexts rewrite methods. Use tools like Browsershots.org to test legacy browser behavior if needed.

## Requirements

1. Proxied browser environment (e.g., Burp Suite with Firefox)
2. Prior successful injection from the injection procedure
3. Optional: Access to browser testing services for validation

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict inline scripts and unsafe-inline
- Log and alert on XSS payload patterns in HTTP methods
- Use web application firewalls (WAF) to block malformed requests
- Regularly scan for reflected XSS with tools like OWASP ZAP

## Objectives

1. Capture the error response with reflected payload
2. Execute and observe the self-XSS in proxy
3. Evaluate exploitation limitations

## Instructions

### Step 1: Intercept and View Response

**Context**: In the proxy tool, inspect the server's 400 error response to see the unescaped payload.

No command; in Burp Suite, drop the response in the Inspector or forward to browser.

> The response body will contain: "Invalid HTTP method: <img src=\"3\" onerror=\"alert(3)\"/>". In the proxied browser, the img tag loads, fails src, and triggers onerror alert.

### Step 2: Test Execution in Browser Contexts

**Context**: Load the error page in a browser via proxy to trigger JS execution; use Browsershots.org for cross-browser checks.

Submit a URL to http://browsershots.org/ with the payload-crafted request simulated.

> Expected: Alert executes only in proxy; standard browsers prevent custom methods, resulting in GET fallback and no XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Browsershots-org]]

## Tags

- [[xss]]
- [[self-xss]]
