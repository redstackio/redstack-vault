---
id: proc-inject-url-rocket
tags:
  - os-command-injection
  - electron
  - url-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Desktop
  - Electron
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:20.314Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Inject-Malicious-URL-into-openInternalVideoChatWindow

## Summary

This procedure involves crafting and injecting a malicious URL parameter into the openInternalVideoChatWindow function, exploiting the lack of validation to prepare for OS command execution via Electron's shell.openExternal.

## Description

The openInternalVideoChatWindow function in internalVideoChatWindow.ts accepts a user-controlled 'url' parameter at line 17, passing it directly to shell.openExternal without sanitization. When internal video chat is disabled (line 14 check bypassed) or in Mac App Store builds, schemes like file:// can be used to trigger local file execution or command interpretation, leading to RCE.

## Requirements

1. Successful XSS execution from prior procedure
2. Knowledge of target OS for scheme crafting (e.g., file:// for Windows/macOS)
3. Rocket.Chat-Desktop with internal video chat disabled
4. Debugging access to verify parameter acceptance

## Defense

Defensive measures and detection strategies:

- Validate and whitelist URL schemes in desktop API functions
- Enable internal video chat to enforce safer handling
- Log all shell.openExternal calls for anomaly detection
- Use app sandboxing to restrict file/system access

## Objectives

1. Bypass parameter validation in the API function
2. Set up a URL that shell.openExternal interprets as executable
3. Position for immediate RCE on invocation

## Instructions

### Step 1: Craft Malicious URL Payload

**Context**: Design a URL using a scheme that leads to command execution, tailored to the victim's OS.

For Windows, use:

```javascript
var maliciousUrl = 'file:///C:/Windows/System32/calc.exe';
```

For macOS:

```javascript
var maliciousUrl = 'file:///System/Applications/Calculator.app';
```

> Test in a safe environment; ensure the path points to an executable.

### Step 2: Inject URL via API Call

**Context**: Pass the crafted URL in the XSS-extended API invocation.

Inject:

```javascript
window.rocketChatDesktop.openInternalVideoChatWindow(maliciousUrl);
```

> Expected output: Function executes without throwing validation errors; URL is queued for shell handling.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[os-command-injection]]
- [[electron]]
- [[url-injection]]
