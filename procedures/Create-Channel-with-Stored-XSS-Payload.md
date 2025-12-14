---
id: proc-create-xss-channel
tags:
  - xss
  - stored-xss
  - validation-bypass
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/meteor-call-create-channel-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:31:18.946Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
---

# Create-Channel-with-Stored-XSS-Payload

## Summary

This procedure exploits a validation bypass in the createChannel Meteor method to store an XSS payload in the room's name property via the extraData parameter, persisting it in the database for later execution.

## Description

The createRoom function in app/lib/server/functions/createRoom.js merges extraData without validation, allowing override of the name. When an admin later edits the room, an error in getValidRoomName triggers handleError, which reflects the unescaped payload via toastr. This requires authenticated access and browser console execution.

## Requirements

1. Logged-in attacker account
2. Browser with developer tools (e.g., Chrome DevTools)
3. Vulnerable Rocket.Chat 3.12.1 instance

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all extraData inputs in room creation
- Escape error messages before passing to toastr
- Log suspicious Meteor calls and monitor database for script tags

## Objectives

1. Store arbitrary JavaScript in room metadata
2. Bypass frontend validation
3. Set up payload for admin interaction

## Instructions

### Step 1: Log In as Attacker

**Context**: Ensure authenticated session.

**Instructions**: Use the login form with 'attacker'/'attacker'.

### Step 2: Open Developer Tools

**Context**: Access the JavaScript console.

**Instructions**: Press F12 or right-click > Inspect > Console tab.

### Step 3: Execute Meteor Call

**Context**: Invoke createChannel with payload override.

**Command** ([[commands/meteor-call-create-channel-xss]]):
```javascript
Meteor.call('createChannel', 'valid-name', [], false, {}, { name: 'edit me <img src onerror=alert(origin)>' })
```

> Calls the server method: 'valid-name' as base name, empty members, public channel, empty extraData, and XSS in name override. Expected output: Channel ID returned, channel visible in UI.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/meteor-call-create-channel-xss]]

## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- xss
- stored-xss
- validation-bypass

