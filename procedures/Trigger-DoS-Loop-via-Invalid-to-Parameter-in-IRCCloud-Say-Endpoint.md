---
tags:
  - dos
  - input-validation
  - websocket
  - api
  - resource-exhaustion
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:32:01.800Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: edd98b58-1c5a-4a40-aff1-bdf608413f8f
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-DoS-Loop-via-Invalid-to-Parameter-in-IRCCloud-Say-Endpoint

## Summary

This procedure exploits inadequate input validation in IRCCloud's 'say' websocket API endpoint by sending a JSON payload with an empty string in the 'to' array, causing a repeated error handling loop that results in self-denial of service for the attacker's account and potential increased load on the system affecting other users.

## Description

The IRCCloud web application uses websockets for real-time messaging. The 'say' endpoint expects a 'to' parameter as a valid channel or user identifier. By providing {"to": [""]}, an empty string array, the server-side error handling enters an infinite loop while attempting to process the invalid recipient, exhausting client resources and blocking account access. This self-DoS can cascade to server load if multiple instances occur. The attack requires an authenticated session and targets the web platform exclusively.

## Requirements

1. Authenticated IRCCloud user session via web browser
2. Access to browser developer tools or a websocket client for payload injection
3. Knowledge of IRCCloud's websocket API structure (method: 'say', params including 'to' and 'message')

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for API parameters, rejecting arrays with empty strings
- Rate-limit websocket messages per user to prevent abuse
- Monitor for looping error patterns in logs and anomalous CPU spikes
- Use circuit breakers in error handling to avoid infinite loops

## Objectives

1. Trigger resource exhaustion on the client-side to deny self-service
2. Increase server load through unchecked error processing
3. Demonstrate impact of poor input validation in real-time APIs

## Instructions

### Step 1: Establish Websocket Connection

**Context**: Authenticate and connect to IRCCloud's websocket to prepare for payload transmission.

Log into IRCCloud web at https://www.irccloud.com. Open developer tools (F12) and navigate to the Console or Network tab to inspect the websocket connection (typically wss://irccloud.com).

**Expected Output**: Active websocket session with authentication confirmed.

### Step 2: Craft and Send Malicious Payload

**Context**: Construct the invalid JSON payload targeting the 'say' method and inject it via the websocket.

In the browser console, identify the websocket object (often accessible as a global or via inspection). Send the payload:

```javascript
const payload = {
  "method": "say",
  "params": {
    "to": [""],
    "message": "test"
  }
};
ws.send(JSON.stringify(payload));
```

Replace 'ws' with the actual websocket instance from the page (e.g., inspect window object for connections). If using an external client like wscat, first connect and authenticate, then send the JSON.

**Expected Output**: Client freezes due to looping errors; account becomes inaccessible until logout/relogin or session expiry.

### Step 3: Verify Impact

**Context**: Confirm the DoS effect and observe any system load indicators.

Attempt to perform normal actions like sending messages or refreshing channels. Monitor browser task manager for high CPU usage.

**Expected Output**: Unresponsiveness in the interface; potential error logs in console showing repeated failures.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- dos
- input-validation
- websocket
- api
- resource-exhaustion
