---
tags:
  - auth-bypass
  - web
  - execution
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.541Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 4f228f29-8ded-420b-9d3d-ebce8055d956
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Submit-HTML-Form-and-Return-to-Admin

## Summary

This procedure executes the crafted HTML form in a browser to send the POST request that sets the admin flag, then returns to the admin page to prepare for access.

## Description

Once the HTML file is ready, opening it in a browser and submitting the form sends the POST to the endpoint, exploiting the lack of validation. The browser then navigates back to the admin URL (https://███████/█████), where the session manipulation takes effect upon refresh.

## Requirements

1. Web browser
2. Local HTML file from previous step
3. Target admin URL

## Defense

Defensive measures and detection strategies:

- Block or sanitize unexpected POST origins
- Implement session fixation prevention
- Monitor browser user-agent and referer headers for anomalies

## Objectives

1. Deliver the malicious POST payload
2. Apply session changes without detection
3. Transition to admin access verification

## Instructions

### Step 1: Open and Submit Form

**Context**: Load the HTML file in the browser to trigger the POST submission, then manually navigate back to the admin page.

No specific command; browser actions:

1. Open bypass.html in browser.
2. Click the submit button.
3. Navigate to https://███████/█████.

> The form submission should occur silently. Check browser developer tools (F12 > Network tab) for the POST request with the hidden parameters. Ensure no errors like 403 or CSRF blocks appear.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[web]]
- [[Execution]]
