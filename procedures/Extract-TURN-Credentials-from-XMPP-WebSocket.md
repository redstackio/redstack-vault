---
tags:
  - xmpp
  - websocket
  - credential-extraction
type: procedure
tools:
  - '[[tools/Chrome-DevTools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:29:44.170Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b3487fa1-4631-4298-9817-2e5456923d82
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
---

# Extract-TURN-Credentials-from-XMPP-WebSocket

## Summary

This procedure involves intercepting XMPP WebSocket traffic in a browser to extract temporary TURN server credentials, enabling authentication for subsequent relay exploitation in real-time communication applications.

## Description

In scenarios where web apps use XMPP over WebSocket for signaling in WebRTC setups, TURN credentials are often sent in plaintext within messages. By inspecting network traffic with browser dev tools, attackers can capture the hostname, username, and password for the TURN server. This is a prerequisite for abusing misconfigured TURN relays to pivot internally. The target environment includes web applications with XMPP integration, typically on ports like 443 for WebSocket.

## Requirements

1. Access to the target web application via browser
2. Chrome or similar browser with DevTools enabled
3. Network connectivity to initiate XMPP sessions

## Defense

Defensive measures and detection strategies:

- Encrypt TURN credentials in XMPP messages or use short-lived tokens with validation
- Monitor WebSocket traffic for anomalous credential extractions via WAF rules
- Implement client-side obfuscation or secure signaling protocols

## Objectives

1. Obtain valid TURN credentials for relay authentication
2. Identify TURN server endpoints for reconnaissance
3. Enable proxy setup for internal access

## Instructions

### Step 1: Initiate XMPP Connection

**Context**: Start a session in the target web app to trigger XMPP WebSocket messages containing TURN details.

No command needed; perform in-browser actions like starting a call.

> Load the application and perform an action that establishes a peer connection, generating WS traffic.

### Step 2: Inspect Network Traffic

**Context**: Use DevTools to filter and extract credentials from WS frames.

**Command** (Browser DevTools):
Open Network tab, filter WS, inspect xmpp-websocket frames for type='turn'.

```javascript
// Pseudo-code for filtering in console
frames.filter(frame => frame.data.includes("type='turn'"))
```

> Extract fields: TURN URI (tls://hostname:443), username, password. Credentials are temporary, valid for session duration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Network Service Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-DevTools]]

## Tags

- [[xmpp]]
- [[websocket]]
- [[credential-extraction]]

---
