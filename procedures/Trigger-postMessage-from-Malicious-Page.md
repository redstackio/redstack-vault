---
tags:
  - xss
  - postmessage
  - payload-delivery
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:19.903Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6249541c-5438-430f-a4fb-b555ae78fe0c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-postMessage-from-Malicious-Page

## Summary

This procedure sends a postMessage event from the malicious page to the target login window, exploiting the insecure origin check to deliver an executable payload for DOM-based XSS.

## Description

The target's event listener validates origins loosely with ~e.origin.indexOf('https://hq.upserve.com'), allowing substring-based bypass. The malicious script targets the open window and sends a message with a 'exec' key containing JS code, which the target will eval.

## Requirements

1. Malicious page hosted and accessible.
2. Target login page open in a referenceable window (e.g., via window.open).
3. JavaScript console access for testing.

## Defense

Defensive measures and detection strategies:

- Use postMessage with structured data validation (e.g., typeof checks before eval).
- Avoid eval; use safer JSON.parse or function constructors.
- Log and alert on unexpected postMessage origins.

## Objectives

1. Deliver payload past origin validation.
2. Ensure message is received by the target handler.
3. Set up for immediate JS execution.

## Instructions

### Step 1: Prepare Target Reference

**Context**: Ensure the malicious page can access the target window object.

```javascript
// In malicious page
if (!targetWindow) {
    targetWindow = window.open('https://inventory.upserve.com/login/', 'target');
}
```

> Expected: Target window loaded and referenceable.

### Step 2: Craft and Send Payload

**Context**: Construct the message with executable code in e.data['exec'].

```javascript
function sendPayload() {
    var payload = {exec: "alert('XSS Triggered'); console.log('Payload delivered');"};
    targetWindow.postMessage(payload, '*');
}
// Call on click or auto
```

> Expected: Message sent; check browser console for transmission.

### Step 3: Verify Transmission

**Context**: Confirm no rejection due to origin.

Monitor network tab or add console.log before postMessage.

> Expected: No errors; message event fired on target.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- postmessage
- xss-trigger
