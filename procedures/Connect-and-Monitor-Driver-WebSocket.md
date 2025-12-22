---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - websocket
  - monitoring
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:17.319Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Connect-and-Monitor-Driver-WebSocket

## Summary

This procedure establishes a WebSocket connection as a Bykea driver to monitor incoming messages for leaked sensitive data, such as trip identifiers, before any authorization like bid acceptance occurs.

## Description

In Bykea's system, WebSocket responses to drivers include trip_no details prematurely, violating access controls. This procedure uses browser tools or a client to connect, authenticate, and log messages, revealing the vulnerability in real-time communication channels. It targets web-based ride-hailing platforms with similar WebSocket implementations, leading to potential information disclosure.

## Requirements

1. Valid Bykea driver account credentials
2. Browser with developer tools (Chrome/Firefox) or WebSocket client like wscat
3. Network access to Bykea's WebSocket endpoint (e.g., wss://api.bykea.com/ws/driver)

## Defense

Defensive measures and detection strategies:

- Implement message-level authorization checks in WebSocket handlers to mask sensitive IDs until bid acceptance
- Monitor WebSocket traffic for anomalous connections or message patterns using WAF or SIEM tools
- Use hashing or tokenization for identifiers in tracking URLs to prevent direct access

## Objectives

1. Establish unauthorized monitoring of trip-related communications
2. Capture pre-authorization data leaks
3. Validate exposure of customer-linked identifiers

## Instructions

### Step 1: Authenticate and Connect

**Context**: Log in as a driver to initiate the WebSocket session.

Open the Bykea driver web interface, log in with credentials, and navigate to a section that triggers WebSocket (e.g., dashboard awaiting trips). In browser dev tools (F12 > Network > WS filter), locate the WebSocket connection URL.

### Step 2: Monitor Messages

**Context**: Observe incoming payloads for trip_no without interacting (no bid acceptance).

Keep the Network tab open or use console to log messages. Wait for a trip assignment message to arrive, which includes the leaked trip_no in JSON format like {"event": "trip_update", "trip_no": "TRIP123456", ...}.

**Expected Output**: JSON message with visible trip_no field.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[websocket]]
- [[monitoring]]
