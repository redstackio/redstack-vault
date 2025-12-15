---
tags:
  - setup
  - developer-mode
  - mozilla-vpn
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:26:29.918Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 140b4f33-0094-4c62-9f1e-0d1c926f2dd0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Enable-Developer-Mode-in-Mozilla-VPN

## Summary

This procedure activates developer mode and staging servers in the Mozilla VPN client, exposing the inspector WebSocket server on port 8765, which is necessary to trigger the path traversal vulnerability in the hotreloader feature.

## Description

The Mozilla VPN client includes hidden developer options that enable staging servers and an inspector interface for debugging. When activated, it starts a local WebSocket server vulnerable to path traversal during file reload operations. This procedure is a prerequisite for exploitation, requiring user interaction to enable the features. It targets Windows installations and does not affect macOS. The technical approach involves rapid menu interactions to unlock the menu, followed by configuration changes and client restart.

## Requirements

1. Mozilla VPN client installed on Windows
2. Administrative or user-level access to run the client
3. No network access required beyond local execution

## Defense

Defensive measures and detection strategies:

- Disable developer mode in production environments and educate users on risks
- Monitor for rapid menu interactions or unexpected WebSocket traffic on port 8765
- Use application whitelisting to prevent unauthorized client modifications

## Objectives

1. Unlock and enable developer options in the VPN client
2. Activate staging servers to expose the inspector
3. Prepare the client for WebSocket-based exploitation

## Instructions

### Step 1: Launch Mozilla VPN Client

**Context**: Start the application to access the settings menu.

No command required; simply run the Mozilla VPN executable from the start menu or installation directory.

> Expected output: Client window opens, showing connection status.

### Step 2: Access Developer Menu

**Context**: Unlock hidden developer options through a gesture-based trigger.

Open the help menu (typically via the menu bar or settings icon), then click the 'Help' title 6 times rapidly.

> Expected output: Developer options menu appears in settings.

### Step 3: Enable Staging Servers and Restart

**Context**: Configure the vulnerable mode and apply changes.

In the developer options, check the 'Use Staging Servers' box. Fully close the client (ensure no processes linger via Task Manager), then reopen it.

> Expected output: Client restarts with staging mode active; WebSocket server on localhost:8765.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- developer-mode
- mozilla-vpn
