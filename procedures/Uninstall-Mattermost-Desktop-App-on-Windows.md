---
tags:
  - uninstallation
  - mattermost
  - persistence
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:30.593Z'
skill_level: novice
impact_level: low
detection_risk: low
sub_techniques: []
id: aff6c64e-0cc3-408c-93ec-d62a480f1275
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Uninstall-Mattermost-Desktop-App-on-Windows

## Summary

This procedure removes the Mattermost Desktop App via Windows uninstaller, exploiting the lack of session data cleanup to leave authentication artifacts intact.

## Description

Using the standard Windows uninstall process (Settings > Apps or Control Panel), the app is removed without prompts for data deletion. Session files in user profiles (e.g., %APPDATA%/Mattermost) persist, rooted in platform limitations and UX design, enabling later bypass.

## Requirements

1. Installed Mattermost Desktop App
2. User privileges to uninstall programs

## Defense

Defensive measures and detection strategies:

- Customize uninstallers to include data wipe options
- Use group policies to enforce full app data removal
- Audit residual files post-uninstallation

## Objectives

1. Remove app binaries while preserving session data
2. Demonstrate vulnerability in cleanup process
3. Set up for reinstallation test

## Instructions

### Step 1: Access Uninstaller

**Context**: Initiate removal without affecting data.

Go to Windows Settings > Apps & features, search for Mattermost, and select Uninstall.

### Step 2: Complete Uninstallation

**Context**: Confirm removal occurs sans data prompts.

Follow prompts to uninstall; observe no questions about stored data.

**Expected Output**: App entry removed from list; files in program directories gone, but %APPDATA% intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[uninstallation]]
- [[mattermost]]
- [[Persistence]]
