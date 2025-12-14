---
tags:
  - server
  - express
  - undici
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-server-start]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:28.233Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 927a7dd7-ba4d-4d96-a357-5b88ec37e6ba
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Start-Node.js-Webhook-Server

## Summary

Launches the vulnerable Express server that handles webhook triggers and submits multipart/form-data requests to the backend using undici's fetch, generating predictable boundaries with Math.random().

## Description

The server.js script sets up an Express app on port 8000 with a /trigger-webhook endpoint. When triggered, it uses undici to send POST requests with multipart boundaries generated via Math.random(), which relies on V8's LCG. This exposes boundaries for collection in the exploit. The procedure assumes dependencies are installed and focuses on starting the server to simulate the client-side vulnerability in a Node.js application forwarding requests to a backend API.

## Requirements

1. Installed dependencies (express, undici)
2. Port 8000 available
3. server.js in current directory

## Defense

Defensive measures and detection strategies:

- Replace Math.random() with cryptographically secure alternatives like crypto.randomBytes in libraries
- Monitor for unusual Node.js process spawns on non-standard ports
- Use WAF to inspect multipart boundaries for patterns indicating predictability

## Objectives

1. Activate the webhook endpoint for boundary observation
2. Enable multipart request generation with vulnerable randomness
3. Prepare for exploit data collection

## Instructions

### Step 1: Launch Server

**Context**: Start the Express server to listen for webhook triggers.

**Command** ([[commands/node-server-start]]):
```bash
node ./server.js
```

> Runs the server. Expected output: "Server listening on port 8000". The server now handles requests exposing undici's boundary generation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/node-server-start]]

## Tools Used

- [[tools/node]]

## Tags

- express
- webhook
- multipart
