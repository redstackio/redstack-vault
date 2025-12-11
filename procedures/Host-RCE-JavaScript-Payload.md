---
tags:
  - rce
  - javascript
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
  - Desktop
  - Electron
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
id: bf3fa767-9f92-4715-8831-ea25615f45e0
created_at: '2025-12-11T06:10:22.523Z'
updated_at: '2025-12-11T06:10:22.523Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Host RCE JavaScript Payload

## Summary

This procedure hosts a JavaScript payload on an attacker-controlled server to exploit Electron in Slack.

## Description

The JS overwrites window.desktop functions, leaks BrowserWindow, and creates a new window with nodeIntegration for RCE.

## Requirements

1. HTTPS server setup.
2. JavaScript payload code.
3. Alternative: Use files.slack.com XSS.

## Defense

Defensive measures and detection strategies:

- Disable nodeIntegration in Electron.
- Monitor for suspicious redirects.

## Objectives

1. Deliver RCE payload.
2. Enable command execution.
3. Achieve data access.

## Instructions

### Step 1: Set Up Server and Host Payload

**Context**: Host HTML with JS payload.

Use [[tools/HTTPS-Enabled-Server]] to serve the file.

```bash
# Example: python -m http.server 443 with HTTPS
```

> Expected: Payload accessible, overwrites functions upon load.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used



## Tools Used

- [[tools/HTTPS-Enabled-Server]]

## Tags

- [[rce]]
- [[JavaScript]]
