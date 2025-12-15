---
tags:
  - csrf
  - drive-by
  - session-hijack
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:03.062Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 693ef20f-84d3-49db-a6ea-9878ece7619b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Execute-CSRF-Attack-on-Victim-Session

## Summary

This procedure executes the CSRF attack by delivering the forged request to a victim on the shared device, leveraging the static token to perform unauthorized actions transparently.

## Description

Once the victim logs into ownCloud on the shared workstation, the attacker sends the crafted link or embeds it in a phishing message. Interaction submits the request using the victim's session cookies and the reused static token, which validates successfully. This allows manipulation like file deletion or account changes without alerting the user, limited by the need for physical proximity.

## Requirements

1. Victim logged in on the shared device post-token theft
2. Delivery channel (email, chat) to the victim
3. Crafted request from previous procedure

## Defense

Defensive measures and detection strategies:

- Implement same-site cookies (Lax/Strict) to block cross-origin requests
- Require user confirmation for sensitive actions
- Audit logs for anomalous actions on shared accounts
- Limit session lifetimes on public devices

## Objectives

1. Induce victim interaction with the forged request
2. Achieve unauthorized action execution
3. Maintain stealth to avoid detection

## Instructions

### Step 1: Deliver Payload

**Context**: Send the malicious link or form to the victim via a trusted channel to encourage clicking on the shared device.

Use email or chat: "Check this update: [malicious-link-with-token]".

> Ensure delivery aligns with victim's login timing on the shared machine.

### Step 2: Trigger and Validate

**Context**: Monitor for execution as the victim interacts, confirming the action completes using the static token.

Observe ownCloud interface or logs for changes (e.g., file deleted).

> Expected output: Silent success with no errors, action reflected in victim's account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[drive-by]]
