---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss
  - execution
  - verification
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.463Z'
skill_level: novice
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-and-Verify-XSS-Execution-in-Viewer-Browsers

## Summary

This procedure triggers the stored XSS payload by accessing the vulnerable send push form in a victim context, verifying execution through observable effects like alerts or data exfiltration.

## Description

Once the payload is injected into the filters, any user loading the send push form will render the unsanitized input, executing the JavaScript in their browser session. This can lead to immediate effects (e.g., pop-ups) or stealthy actions (e.g., beaconing to an attacker server). In a real attack, this enables client-side compromise without further interaction, affecting all dashboard users.

## Requirements

1. Access to a second user account or incognito session to simulate a victim
2. The injected payload from the prior procedure
3. Browser console open for logging execution

## Defense

Defensive measures and detection strategies:

- Use web application firewalls (WAFs) to block script tags in inputs
- Implement client-side scanning for XSS payloads on form load
- Log and alert on unexpected JavaScript errors or external fetches from the dashboard

## Objectives

1. Execute the stored script in a non-attacker browser context
2. Confirm impact through visible indicators or network traffic
3. Highlight risks of session hijacking or phishing escalation

## Instructions

### Step 1: Simulate Victim Access

**Context**: Load the send push form as a different user to trigger rendering of the stored filters.

Log out of the attacker account, log in with a test/victim account, and navigate to the "Send Push" section.

### Step 2: Observe Execution

**Context**: The form loads the filters, parsing the injected script and running it automatically.

Upon loading, watch for the alert dialog or check the browser console (F12 > Console) for script output. For exfiltration payloads, monitor network tab for requests to attacker.com.

> Successful execution shows the alert or logs the domain/cookies, confirming browser context compromise.

### Step 3: Validate Impact

**Context**: Test for real-world effects like data theft to assess severity.

Modify the payload to include `document.cookie` and verify if session data is sent to a controlled endpoint using tools like ngrok for local capture.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
- verification
- client-side-attack
