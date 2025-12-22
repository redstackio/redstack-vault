---
id: proc-trigger-xss-removal-mobilevikings
tags:
  - xss
  - execution
  - exfiltration
type: procedure
tools: []
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
updated_at: '2025-12-14T03:15:35.687Z'
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
---
# Trigger-XSS-via-Authorization-Removal

## Summary

This procedure executes the stored XSS by having the victim interact with the 'Remove authorization' button, rendering the unsanitized `x:authorization-to-first-name` parameter in a modal window.

## Description

The vulnerability lies in the modal dialog for removing authorizations, where the attacker's user name (containing the payload) is output without HTML escaping, allowing JavaScript to run in the victim's authenticated session. This can lead to cookie theft or keylogging.

## Requirements

1. Victim has loaded the authorization overview with the malicious request
2. Payload stored in the user name field
3. Victim performs the removal action

## Defense

Defensive measures and detection strategies:

- Escape all outputs in modal windows
- Implement strict XSS filters and CSP
- Log and monitor JavaScript execution anomalies

## Objectives

1. Trigger payload execution in victim's browser
2. Steal session data or perform other client-side attacks
3. Maintain stealth to avoid detection

## Instructions

### Step 1: Guide Victim to Removal

**Context**: Use follow-up social engineering to prompt removal.

Send a message: "Please remove the pending authorization if not needed."

### Step 2: Victim Clicks Remove

**Context**: On the overview page, victim selects the request and clicks 'Remove authorization'.

This opens the modal, injecting the payload via the unsanitized parameter.

### Step 3: Payload Executes

**Context**: JavaScript runs, e.g., exfiltrating cookies to attacker's server.

Observe network traffic or alerts for successful theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
