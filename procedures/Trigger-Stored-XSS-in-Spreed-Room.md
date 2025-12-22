---
id: proc-190870-trigger
tags:
  - xss
  - execution
  - trigger
  - nextcloud
  - spreed
  - hover
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
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.155Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS in Spreed Room

## Summary

This procedure triggers the stored XSS payload by having victims interact with the tainted call room, executing arbitrary JavaScript in their browsers for potential session theft or other attacks.

## Description

Victims joining the room or hovering over the injected name cause the payload to render and fire events like onerror. In IE, lack of CSP allows direct execution on load; in Chrome, hover triggers it. Targets web browsers via Nextcloud's UI; requires prior room setup. Outcomes include JS alerts or exfiltration, high impact on admins.

## Requirements

1. Victim access to the shared room or link.
2. Vulnerable browser (tested in IE and Chrome).
3. Payload injected and room created.

## Defense

Defensive measures and detection strategies:

- Deploy CSP headers to restrict script execution.
- Escape HTML in all UI renders of user names.
- Monitor browser console errors or unexpected JS events in client logs.

## Objectives

1. Execute the stored payload in victim context.
2. Demonstrate impact like alerts or data theft.
3. Escalate to broader client-side compromise.

## Instructions

### Step 1: Direct Victim to Room

**Context**: Ensure the victim opens the invitation or link.

Provide the room link or wait for invite acceptance to load the Spreed room.

### Step 2: Interact to Trigger

**Context**: Perform actions that render the name, firing the payload.

In the room view, have the victim load the page (IE auto-triggers) or hover over the participant name list (Chrome).

> Expected output: JS execution, e.g., alert(1) pops up, confirming vulnerability.

### Step 3: Validate Impact

**Context**: Check for successful exploitation effects.

Observe if custom payloads (e.g., for cookie theft) send data to attacker-controlled servers.

> Success if arbitrary code runs, enabling attacks like session hijacking.

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
- trigger
- javascript
- execution
