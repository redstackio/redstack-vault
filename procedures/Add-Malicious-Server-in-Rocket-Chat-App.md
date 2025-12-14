---
id: proc-add-malicious-server-rocket-chat
tags:
  - rce
  - electron
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
  - Linux
  - macOS
  - Electron
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:32.815Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
---
# Add-Malicious-Server-in-Rocket-Chat-App

## Summary

This procedure guides the addition of a malicious server URL in the Rocket.Chat Electron desktop app, triggering the load of a prepared malicious webpage that bypasses links.js validation to execute arbitrary code via shell.openExternal.

## Description

Exploiting the vulnerability in Rocket.Chat's Electron app (bypass of fix #276031), this procedure involves entering the attacker's server URL in the app's 'Add new server' UI. The app fetches /api/info, loads index.html, executes the hooked JS, bypasses regex checks, and opens local files (e.g., executables or SMB shares). Affects Windows (calc.exe), Linux/macOS (with path adaptations). Prerequisites: Malicious server running, victim app version vulnerable. Expected: RCE without further interaction, e.g., app launches calc.exe or accesses network shares for credential theft.

## Requirements

1. Vulnerable Rocket.Chat Electron app installed on target OS.
2. Attacker's server URL accessible (http://attacker-ip).
3. Victim tricked into adding the server (e.g., via phishing email).

## Defense

Defensive measures and detection strategies:

- Patch to latest Rocket.Chat version (>2.17.9 with proper fix).
- Disable or sandbox shell.openExternal calls.
- User training to avoid adding untrusted servers.
- Monitor app logs for suspicious URL loads or external opens.

## Objectives

1. Load malicious content into the Electron renderer.
2. Trigger RCE through bypassed validation.
3. Achieve code execution on the host OS.

## Instructions

### Step 1: Open Add Server UI

**Context**: Launch the app and navigate to server addition to input the malicious URL.

No command; app UI steps:
1. Open Rocket.Chat Electron app.
2. Click the server selector (top-left).
3. Select 'Add new server'.

> Expected: Dialog opens for URL entry.

### Step 2: Enter and Confirm URL

**Context**: Input the attacker's URL, which triggers API check and page load.

Enter: http://attacker-ip (or domain).

Click 'Add server' or 'Connect'.

> The app queries /api/info, loads index.html if valid, executes JS, bypasses '^([a-z]+:)?\/\/' check, dispatches click, calls shell.openExternal('c:\\windows\\system32\\calc.exe'). Expected: calc.exe launches (Windows); adapt href for other OS (e.g., '/usr/bin/gnome-calculator' on Linux).

### Step 3: Verify Execution

**Context**: Check for RCE indicators on the victim machine.

Observe: Executable launches or SMB connection attempted.

> Success: calc.exe window opens; failure: App errors on URL validation (indicates patch applied).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[electron]]
- [[shell-openexternal]]
