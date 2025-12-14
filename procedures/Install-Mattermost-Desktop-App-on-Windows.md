---
tags:
  - installation
  - mattermost
  - windows
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:30.600Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
id: bf42332e-bc14-4935-a276-69562a0d21bd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Install-Mattermost-Desktop-App-on-Windows

## Summary

This procedure installs the official Mattermost Desktop App for Windows 64-bit, setting the stage for session establishment in vulnerability demonstrations.

## Description

The Mattermost Desktop App, likely built on Electron, is downloaded and installed from official sources. This step requires internet access and administrative privileges on the target Windows machine. It prepares the environment for authentication, where session data will later persist due to uninstall flaws.

## Requirements

1. Windows 64-bit operating system
2. Internet connection for downloading the installer
3. Administrative privileges for installation

## Defense

Defensive measures and detection strategies:

- Monitor installer downloads from official Mattermost site
- Use endpoint detection to log app installations
- Enforce app whitelisting in enterprise environments

## Objectives

1. Deploy the app to enable session creation
2. Ensure compatibility with Windows architecture
3. Prepare for subsequent authentication steps

## Instructions

### Step 1: Download Installer

**Context**: Obtain the official executable to avoid tampered versions.

Navigate to the Mattermost downloads page and select the Windows 64-bit desktop app installer (e.g., Mattermost-Setup-x64.exe).

### Step 2: Run Installation

**Context**: Execute the setup to integrate the app into the system.

Double-click the downloaded .exe file, follow the wizard prompts, and complete the installation. Accept defaults unless customization is needed.

**Expected Output**: App shortcut created in Start menu; installation log in temp directories.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[installation]]
- [[mattermost]]
- [[windows]]
