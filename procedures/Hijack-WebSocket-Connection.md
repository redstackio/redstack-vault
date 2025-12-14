---
id: 123e4567-e89b-12d3-a456-426614174002
name: Hijack-WebSocket-Connection
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.964Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - cswsh
  - hijacking
  - websocket
platforms:
  - Web
commands:
  - '[[commands/websocket-hijack-js]]'
tools:
  - '[[tools/PortSwigger-WebSocket-Lab]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Hijack-WebSocket-Connection

## Summary

This procedure hijacks an authenticated WebSocket connection by initiating it from a malicious cross-origin webpage, leveraging the lack of CSRF protections to impersonate the victim's session.

## Description

Once the vulnerability is confirmed, the attacker embeds JavaScript in their controlled site to create a WebSocket instance targeting the vulnerable endpoint. The browser attaches session cookies to the upgrade request, allowing the hijack. In the Stripo Inc case, this enabled interception of all WebSocket traffic without user interaction beyond visiting the malicious page.

## Requirements

1. Malicious webpage hosted on attacker's domain
2. Victim visits the page while authenticated to target
3. Target WebSocket URL known and unprotected
4. JavaScript execution enabled in victim's browser

## Defense

Defensive measures and detection strategies:

- Require custom headers or tokens in WebSocket requests
- Use SameSite=Strict cookies to prevent cross-site inclusion
- Log and alert on WebSocket connections from untrusted origins

## Objectives

1. Establish control over the victim's WebSocket session
2. Relay real-time data through the hijacked channel
3. Prepare for data extraction

## Instructions

### Step 1: Embed Hijacking Script

**Context**: Add JavaScript to the malicious HTML page to initiate the connection automatically on load.

**Command** ([[commands/websocket-hijack-js]]):
```javascript
document.addEventListener('DOMContentLoaded', function() {
  const ws = new WebSocket('ws://target.com/ws');
  ws.onopen = function() { console.log('Hijacked connection open'); };
});
```

> This script runs on page load, creating the WebSocket. Expected output: Console log confirming open connection if successful.

### Step 2: Monitor Connection

**Context**: Set up event listeners to capture all traffic on the hijacked socket.

**Command** ([[commands/websocket-hijack-js]]):
```javascript
ws.onmessage = function(event) { console.log('Hijacked message:', event.data); };
ws.onerror = function(error) { console.error('Hijack error:', error); };
```

> Listens for messages. Incoming data indicates successful hijack; errors suggest protections in place.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/websocket-hijack-js]]

## Tools Used

- [[tools/PortSwigger-WebSocket-Lab]]

## Tags

- [[cswsh]]
- [[hijacking]]
- [[websocket]]
