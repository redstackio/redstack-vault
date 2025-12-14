---
tags:
  - websocket
  - poc-execution
  - browser
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.227Z'
sub_techniques: []
id: 540dc1d9-b124-4a0d-ad70-71ff9f7d0298
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Open-WebSocket-PoC-HTML-in-Browser

## Summary

This procedure involves loading a locally hosted PoC HTML file in a web browser to establish an unauthenticated WebSocket connection to the target's GraphQL endpoint, setting the stage for sending the introspection query.

## Description

The PoC HTML file contains JavaScript to create a WebSocket object connected to the target endpoint (e.g., ws://target.com/graphql). Upon loading, it prepares to send messages without requiring login, exploiting the misconfiguration where WebSocket 'start' type messages bypass auth checks. This step assumes the local server from the previous procedure is running.

## Requirements

1. Local HTTP server running on port 8000
2. Modern web browser (Chrome, Firefox, etc.)
3. Target WebSocket URL configured in the PoC HTML

## Defense

Defensive measures and detection strategies:

- Require authentication on all WebSocket endpoints
- Implement origin checks for WebSocket connections
- Monitor browser developer tools for suspicious connections

## Objectives

1. Initiate WebSocket handshake without credentials
2. Verify connection to the unauthenticated endpoint
3. Prepare for query transmission

## Instructions

### Step 1: Navigate to PoC

**Context**: Access the hosted PoC to trigger the WebSocket setup.

Open your browser and go to http://localhost:8000/ws.html.

> The page loads the JavaScript, which attempts to connect to the target WebSocket. Check the browser console for connection status.

### Step 2: Verify Connection

**Context**: Confirm the WebSocket is open and ready.

Monitor the browser console for messages like "WebSocket connected" or errors.

> Successful connection indicates the endpoint is reachable and unauthenticated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- websocket
- poc-execution
- browser
