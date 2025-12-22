---
id: proc-uuid-3
tags:
  - xss
  - execution
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-04T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:37.800Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-via-Profile-Edit

## Summary

This procedure triggers the stored XSS payload by inducing the victim to edit their FetLife profile, where the unsanitized fetish name is rendered, executing arbitrary JavaScript in the victim's browser context.

## Description

After the malicious fetish is added to the victim's profile, editing the profile settings causes the platform to load and display the fetish list without proper output escaping. This renders the injected script, leading to execution. The attack scenario targets the profile edit interface on FetLife. Expected outcomes: JavaScript runs, potentially exfiltrating session data or performing other client-side actions.

## Requirements

1. Victim has added the malicious fetish to their profile
2. Ability to influence victim to edit profile (e.g., via follow-up social engineering)
3. Attacker server for receiving exfiltrated data

## Defense

Defensive measures and detection strategies:

- Apply output escaping when rendering user-controlled data in edit interfaces
- Implement strict CSP headers to block unauthorized script execution
- Log and alert on JavaScript errors or unexpected network requests from client-side

## Objectives

1. Render the stored payload in the victim's browser
2. Execute JavaScript for session hijacking or data theft
3. Achieve arbitrary code execution in victim context

## Instructions

### Step 1: Induce Profile Edit

**Context**: Prompt the victim to access profile settings to trigger rendering.

Send a follow-up message: "Hey, edit your profile to update your fetishes – I just added one!"

### Step 2: Observe Execution

**Context**: Victim loads the edit page, executing the payload.

As the victim navigates to profile edit, the fetish name is inserted into the DOM without escaping, running the script.

> Expected output: Payload executes (e.g., network request to attacker server with cookies); verify by checking server logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
