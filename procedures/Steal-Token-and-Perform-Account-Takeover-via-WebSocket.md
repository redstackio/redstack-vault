---
id: proc-steal-token-websocket-takeover
tags:
  - token-theft
  - account-takeover
  - websocket
  - meteor
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
  - '[[Lateral Movement]]'
commands: []
verified: false
platforms:
  - Web
  - Desktop (Electron)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:52:38.750Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Valid Accounts]]'
---
---

# Steal-Token-and-Perform-Account-Takeover-via-WebSocket

## Summary

This procedure uses the executed XSS script to steal the victim's Meteor login token from localStorage, then authenticates via WebSocket to impersonate the user and perform actions like role assignment or password changes, achieving full account takeover.

## Description

Rocket.Chat uses Meteor for real-time features, storing login tokens in localStorage. The XSS payload extracts this token and establishes a WebSocket connection using SockJS, resuming the session with the stolen token. Once authenticated, the attacker can invoke Meteor methods to manipulate user data, such as elevating privileges or altering credentials. In the Desktop client, this may extend to file reads or RCE.

## Requirements

1. Executed XSS with access to localStorage
2. Knowledge of the target's WebSocket endpoint (wss://host/sockjs/)
3. Attacker's user ID for role assignment

## Defense

Defensive measures and detection strategies:

- Use HttpOnly cookies for session tokens instead of localStorage
- Implement token binding to user-agent or IP
- Log WebSocket connections and method calls for anomalies

## Objectives

1. Exfiltrate session token
2. Establish authenticated WebSocket session
3. Execute privileged actions on victim's behalf

## Instructions

### Step 1: Extract Token

**Context**: In the XSS context, access browser storage.

The script runs: localStorage.getItem('Meteor.loginToken')

> Expected: Token string retrieved.

### Step 2: Connect via WebSocket

**Context**: Use the token to resume session over WebSocket.

Script connects to wss://host/sockjs/111/evilwss/websocket and sends authentication with the resume token.

> Explanation: SockJS handles fallback transports; connection succeeds if token is valid.

### Step 3: Invoke Methods for Takeover

**Context**: Call Meteor methods to alter account.

Execute: Meteor.call('insertOrUpdateUser', { userId: victimId, roles: ['admin'] }) or change password.

**Expected Output**: Account modified; confirm via UI or logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]
- [[Lateral Movement]]

### Techniques

- [[Steal Web Session Cookie]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-theft]]
- [[websocket]]

