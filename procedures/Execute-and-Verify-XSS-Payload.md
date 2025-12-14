---
tags:
  - xss-execution
  - verification
  - alert
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:41.739Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b1aac98d-182c-430d-9f21-124a2757c4a3
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Execute-and-Verify-XSS-Payload

## Summary

This procedure forwards the modified response to execute the injected SVG XSS payload and verifies success through the appearance of a JavaScript alert, confirming the vulnerability's exploitability for further attacks like session theft.

## Description

After payload injection and redirect removal, forwarding the response renders the page in the browser, where the reflected SVG executes its onload handler. The alert('jarvis7') serves as proof-of-concept, but in real scenarios, this could be replaced with code to steal cookies (e.g., document.cookie) or access geolocation/webcam APIs.

## Requirements

1. Modified response ready in Burp Suite from prior steps
2. Browser session active with auth bypass
3. No additional tools beyond Burp

## Defense

Defensive measures and detection strategies:

- Deploy browser sandboxing and XSS filters (e.g., X-XSS-Protection header)
- Audit for SVG uploads or reflections in PHP apps
- Detect alerts or anomalous JS execution via client-side monitoring

## Objectives

1. Trigger JavaScript execution in victim context
2. Validate vulnerability without page disruption
3. Assess impact for escalation (e.g., impersonation)

## Instructions

### Step 1: Forward Modified Response

**Context**: Release the tampered response to the browser for rendering.

In Burp Suite, click 'Forward' on the response tab.

> The browser loads the page; watch for immediate execution without redirect.

### Step 2: Observe Execution

**Context**: Confirm the payload fires by checking for the alert dialog.

Monitor the browser for a popup alert displaying 'jarvis7'.

> Expected: Alert box appears, proving XSS; dismiss to continue. If no alert, recheck payload encoding or redirect removal.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss-execution]]
- [[verification]]
