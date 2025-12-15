---
id: proc-scan-port-clickjack
tags:
  - port-scanning
  - xss
  - clickjacking
type: procedure
tools:
  - '[[tools/Chrome-Browser]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:12.940Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Scan-for-Debugging-Port-and-Clickjack

## Summary

This procedure uses JavaScript in the browser to scan local ports for Burp's Chrome debugging websocket and renders a clickjacking payload to compromise the interface.

## Description

Once the exploit page loads, JS sniffs local ports (e.g., via WebSocket connections or timing attacks) to identify the randomized debugging port. It then exploits known XSS in Chrome's debugging protocol (e.g., Chromium bugs since 2016) to compromise the WebSocket GUID. A clickjacking iframe overlays a 'CLICK ME!!!' button, tricking the user into clicking while targeting the debugging UI. This occurs in a web context on macOS.

## Requirements

1. Burp scan running with debugging exposed
2. Exploit page loaded in Chrome
3. JavaScript execution enabled

## Defense

Defensive measures and detection strategies:

- Use --remote-debugging-pipe instead of port for local-only secure transport
- Patch Chrome to latest version to mitigate XSS bugs
- Detect anomalous local port scans via browser security features

## Objectives

1. Identify and connect to debugging websocket
2. Exploit XSS for GUID compromise
3. Display clickjacking UI for user interaction

## Instructions

### Step 1: Execute Port Scan and Render Payload

**Context**: Allow JS to run and observe port detection, followed by clickjacking setup.

**Command** (JavaScript in page; no CLI):
The burp.html JS handles this: loops over ports, attempts ws://127.0.0.1:<port>/json, exploits on success.

> Expected output: Browser console: "Found port 9225"; iframe with button appears. Verify by inspecting DOM for hidden iframe.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Browser]]

## Tags

- port-scanning
- xss
- clickjacking
