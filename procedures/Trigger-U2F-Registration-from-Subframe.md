---
tags:
  - u2f
  - postmessage
  - xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - iOS
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f3302c19-d52c-4def-8c7e-979174d635ac
created_at: '2025-12-14T03:47:12.889Z'
updated_at: '2025-12-14T03:47:12.889Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-U2F-Registration-from-Subframe

## Summary

This procedure exploits the lack of origin validation in Brave iOS by invoking u2f.register() from a cross-origin subframe via direct U2F.postMessage, triggering a misleading FIDO modal that displays the top frame's origin.

## Description

Brave's iOS implementation allows subframes to directly call U2F.postMessage to execute u2f.register(), without validating the caller's origin. This initiates a fake U2F registration process, showing a 'Ready to Scan' modal with the top frame's origin (e.g., alice.csrf.jp) instead of the subframe's (evil.csrf.jp), deceiving the user. The attack scenario involves embedding this in a victim page, leading to JS injection upon completion. Prerequisites include the loaded iframe setup; outcomes enable phishing and code execution.

## Requirements

1. Cross-origin iframe loaded in Brave iOS
2. JavaScript access in subframe to craft postMessage payload
3. FIDO U2F API availability in browser

## Defense

Defensive measures and detection strategies:

- Enforce strict origin checks in U2F implementations
- Audit modals to display actual caller origins
- Use browser extensions to block unauthorized postMessage

## Objectives

1. Initiate unauthorized U2F process from subframe
2. Deceive user with false origin in modal
3. Prepare for payload injection in response handling

## Instructions

### Step 1: Craft postMessage Payload

**Context**: Prepare the message to invoke u2f.register() with fake parameters.

In subframe JS: window.parent.postMessage({type: 'u2f.register', appId: '...', ...}, '*');

> This bypasses checks; include a malicious 'version' parameter for later injection.

### Step 2: Invoke from Subframe

**Context**: Execute the call to trigger the modal.

Run the postMessage script in the iframe context.

> Expected: FIDO modal appears showing top frame origin.

### Step 3: Observe Misrepresentation

**Context**: Confirm the UI deception.

Note the modal displays alice.csrf.jp, not evil.csrf.jp.

> Success: User is prompted without suspicion.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[u2f]]
- [[postmessage]]
- [[xss]]
