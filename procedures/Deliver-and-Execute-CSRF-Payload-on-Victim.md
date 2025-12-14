---
id: proc-uuid-3
tags:
  - csrf
  - social-engineering
  - web
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
updated_at: '2025-12-14T17:27:22.954Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver and Execute CSRF Payload on Victim

## Summary

This procedure delivers the crafted CSRF payload to a victim on a shared workstation, leveraging the persistent token to execute unauthorized actions seamlessly without the victim's awareness.

## Description

Delivery occurs via social engineering tactics like phishing emails or chat messages containing the malicious link or embedded form. When the victim interacts on the same workstation, the browser submits the request using the valid, unchanged token from the prior session. This compromises the victim's account (e.g., changing credentials) while appearing as a legitimate action. The attack relies on physical proximity for shared access but amplifies impact through account takeover.

## Requirements

1. Crafted CSRF payload with stolen token
2. Victim access to the shared workstation
3. Social engineering channel (email, chat) to deliver payload

## Defense

Defensive measures and detection strategies:

- Educate users on shared workstation risks and token hygiene
- Implement multi-factor authentication for sensitive actions
- Deploy browser extensions to block auto-submitting forms
- Monitor for rapid successive actions from shared IPs

## Objectives

1. Induce victim interaction with the payload
2. Achieve unauthorized action execution via token
3. Confirm compromise without user detection

## Instructions

### Step 1: Prepare Delivery Mechanism

**Context**: Package the payload for easy victim consumption.

Encode the HTML form as a clickable link (e.g., data:text/html,<form...>) or host on a disposable site and send URL via email: "Click to update your profile: http://evil.com/malicious.html".

**Expected Output**: Deliverable link or attachment.

### Step 2: Social Engineering Delivery

**Context**: Trick the victim into opening the payload on the shared machine.

Send the message to the victim, impersonating a trusted source (e.g., "IT update required"). Ensure timing aligns with workstation access.

**Expected Output**: Victim receives and opens the link.

### Step 3: Monitor Execution

**Context**: Verify the request processes successfully.

Observe application logs or follow up by checking if the action (e.g., email change) occurred. No direct command; rely on victim interaction confirmation.

**Expected Output**: Account modified, e.g., new email set.

**Success Indicators**:
- No CSRF rejection
- Action completes silently

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[social-engineering]]
- [[web]]
