---
id: proc-uuid-3
tags:
  - csrf
  - social-engineering
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
updated_at: '2025-12-14T17:27:03.176Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trick-Victim-into-Executing-Malicious-Request

## Summary

This procedure delivers the crafted CSRF request to a victim on the same shared workstation, tricking them into triggering it after login, which uses the persistent token to authorize unauthorized actions transparently.

## Description

The attacker sends the malicious link or form via common channels, relying on the victim's login on the shared device to bind the request to their session. The static token ensures server acceptance, completing the CSRF attack without alerting the user. This is effective in multi-user scenarios where browser state persists.

## Requirements

1. Crafted request from prior procedure
2. Victim's contact info (email, chat) for delivery
3. Shared workstation access pattern

## Defense

Defensive measures and detection strategies:

- Educate users on shared device risks and token hygiene
- Implement user-agent or IP binding for tokens
- Detect rapid successive logins on shared devices

## Objectives

1. Induce victim interaction post-login
2. Execute the forged request in victim's context
3. Achieve unauthorized action (e.g., data alteration)

## Instructions

### Step 1: Prepare Delivery Mechanism

**Context**: Choose a phishing vector to send the malicious payload.

Embed the form in an email or create a clickable link disguised as legitimate (e.g., "Click to confirm your account").

**Expected Output**: Deliverable message with embedded request.

### Step 2: Send to Victim

**Context**: Target the next likely user of the shared workstation.

Transmit via email or chat, timing it for when the victim accesses the device.

**Expected Output**: Victim receives and potentially opens the message.

### Step 3: Monitor Execution

**Context**: Confirm the request fires upon victim interaction after login.

Watch for application changes or use a callback to verify (e.g., if action logs to attacker's controlled endpoint).

**Expected Output**: Successful unauthorized action logged on server.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[social-engineering]]
