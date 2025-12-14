---
tags:
  - rce
  - electron
  - rocket-chat
  - desktop-client
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Desktop
  - Electron
  - Windows
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 91222d09-65e9-487c-b768-ed4d82f70006
created_at: '2025-12-14T17:23:42.493Z'
updated_at: '2025-12-14T17:23:42.493Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-RCE-via-Rocket-Chat-Desktop-Connection

## Summary

This procedure describes connecting the Rocket.Chat-Desktop client to a compromised server, triggering the execution of the injected custom script to achieve remote code execution via an insecure Electron BrowserWindow.

## Description

Once the malicious custom script is configured on the server, any desktop client connecting and logging in will execute the script in its Electron renderer process. The script opens a new window with nodeIntegration enabled, loading a preload script from the attacker's server, which can run Node.js code like spawning CMD.exe. This exploits the lack of sanitization in the desktop app's handling of server-injected JS, leading to full RCE on the victim's machine. The target environment is the Electron-based desktop client on platforms like Windows.

## Requirements

1. Compromised Rocket.Chat server with malicious custom script active
2. Rocket.Chat-Desktop client installed on the victim's machine
3. Victim's network access to the server
4. Preload script (e.g., cmd.js) hosted on attacker's accessible server

## Defense

Defensive measures and detection strategies:

- Update Rocket.Chat-Desktop to patched versions that sanitize custom scripts
- Enable Electron security flags like contextIsolation and webSecurity in the app
- Monitor client-side for unexpected BrowserWindow creations or external script loads
- Use application whitelisting to restrict Electron apps from spawning processes
- Educate users on connecting only to trusted servers and monitor for anomalous pop-ups

## Objectives

1. Trigger script execution upon client connection
2. Load and run arbitrary code from external preload
3. Confirm RCE, such as command shell spawn

## Instructions

### Step 1: Launch and Connect Client

**Context**: Initiate the connection to activate the custom script.

No command required; use the desktop app:

- Open Rocket.Chat-Desktop
- Enter server URL and login credentials

> Upon login, the script executes automatically. Expected output: Client interface loads, but malicious window may open subtly.

### Step 2: Observe Code Execution

**Context**: Verify the preload script runs and executes payload.

Monitor the victim's machine for effects from cmd.js, such as:

- CMD.exe process spawning
- Network requests to attacker's preload server

> Expected output: Visible command prompt or logged execution traces in Electron dev tools.

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
- [[electron]]
- [[rocket-chat]]
- [[desktop-client]]
