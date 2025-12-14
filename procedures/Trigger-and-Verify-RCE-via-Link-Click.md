---
id: proc-trigger-rce-click
tags:
  - rce
  - user-execution
  - electron
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/bash-rce-demo]]'
verified: false
platforms:
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Malicious File]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:28.540Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Malicious File]]'
  - '[[Unix Shell]]'
---
# Trigger-and-Verify-RCE-via-Link-Click

## Summary

This procedure simulates the victim clicking the malicious smb:// link in Rocket.Chat, bypassing filters to execute the .desktop file's bash command for remote code execution.

## Description

Clicking the link invokes shell.openExternal() in the Electron app, which processes smb:// without blocking, fetching and running the .desktop file. On Linux, this launches the Exec command; similar behavior on Windows/macOS via protocol handlers. Vulnerability root: links.js only strips file://. Outcome: Arbitrary code runs on victim system, demonstrated by app launches and messages.

## Requirements

1. Victim running Rocket.Chat with link visible
2. Samba share accessible from victim's network
3. User interaction (click and potential OS confirmation)

## Defense

Defensive measures and detection strategies:

- Patch Electron apps to whitelist only safe protocols (e.g., http/https)
- Enable UAC/prompts for external launches and monitor via EDR
- Detect anomalous process spawns (e.g., bash from Electron) post-click

## Objectives

1. Exploit protocol bypass for payload execution
2. Achieve RCE without direct file access
3. Verify impact through observable effects

## Instructions

### Step 1: Click the Link

**Context**: As victim, interact with the URL to trigger shell.openExternal().

In the chat, right-click or click the smb:// link; confirm any OS launcher prompt.

> Expected output: System attempts to open the remote .desktop file via SMB.

### Step 2: Observe Execution

**Context**: Validate RCE by checking for command effects using [[commands/bash-rce-demo]].

The embedded command executes automatically.

> Expected output: mate-calc launches in background; xmessage dialog shows "Hello from Electron."

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Malicious File]] User Execution: Malicious File
- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/bash-rce-demo]]

## Tools Used


## Tags

- rce
- user-execution
- electron
