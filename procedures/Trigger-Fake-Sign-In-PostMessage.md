---
tags:
  - web
  - postmessage
  - injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/postmessage-send-fake-signin]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 00711a56-6c3e-4949-a2be-016e61bee9d4
created_at: '2025-12-11T06:10:28.568Z'
updated_at: '2025-12-11T06:10:28.568Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Trigger Fake Sign-In PostMessage

## Summary

This procedure triggers a postMessage event from the malicious page to send fake sign-in data, exploiting the origin bypass.

## Description

The malicious page sends a postMessage with type 'digits_sdk_sign_in' containing the attacker's tokens, which the target site accepts due to the validation flaw.

## Requirements

1. Malicious page loaded in victim's browser
2. JavaScript enabled
3. Attacker's sign-in tokens prepared

## Defense

Defensive measures and detection strategies:

- Validate postMessage origins with exact matching
- Log and alert on unexpected messages

## Objectives

1. Inject fake sign-in data
2. Exploit regex wildcard in search()
3. Prepare for phone association

## Instructions

### Step 1: Interact with Button

**Context**: Click a button on the malicious page to trigger the event.

The page includes a button that executes the postMessage.

> Button click initiates the script.

### Step 2: Send PostMessage

**Context**: Execute the JavaScript to send the message.

**Command** ([[commands/postmessage-send-fake-signin]]):
```javascript
window.opener.postMessage({ type: 'digits_sdk_sign_in', data: { phone: 'attacker-phone', token: 'fake-token' } }, '*');
```

> Explanation: Sends fake data to the opener window, bypassing validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/postmessage-send-fake-signin]]

## Tools Used



## Tags

- web
- postmessage
- injection
