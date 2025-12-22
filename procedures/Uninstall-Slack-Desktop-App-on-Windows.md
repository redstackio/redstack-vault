---
tags:
  - slack
  - uninstallation
  - windows
type: procedure
tools: []
tactics: []
commands: []
platforms:
  - Windows
techniques: []
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: f6d2f849-781e-4946-9aa5-501bf053f868
created_at: '2025-12-14T17:31:19.730Z'
updated_at: '2025-12-14T17:31:19.730Z'
verified: false
validated: true
submitted: true
---
# Uninstall-Slack-Desktop-App-on-Windows

## Summary

This procedure covers the standard uninstallation of the Slack desktop app on Windows, which fails to remove local session data, enabling the core vulnerability.

## Description

Windows uninstallation for Slack is handled through the system's Apps & features interface or executable, but it does not delete residual files in user directories like %APPDATA% or %LOCALAPPDATA%. This leaves session tokens and credentials intact, allowing persistence. The process is automatic with no warnings about data retention, making it a subtle flaw exploitable in shared setups.

## Requirements

1. Installed Slack desktop app on 64-bit Windows
2. User permissions to uninstall software
3. No admin rights required for standard user installs

## Defense

Defensive measures and detection strategies:

- Manually delete %APPDATA%\Slack and %LOCALAPPDATA%\Slack after uninstallation
- Use enterprise tools like Microsoft Intune to enforce full app data wipes
- Monitor file system changes in app data directories post-uninstallation

## Objectives

1. Remove the Slack executable while preserving session files
2. Simulate a clean removal that exposes the persistence issue
3. Ensure no uninstall prompts alert to residual data

## Instructions

### Step 1: Access Uninstall Interface

**Context**: Locate the app in Windows settings for removal.

Open Settings > Apps > Apps & features, search for 'Slack', and select it.

### Step 2: Execute Uninstall

**Context**: Trigger the removal process without additional cleanup.

Click 'Uninstall' and confirm. The process completes automatically without prompts for data deletion.

> Post-uninstall, verify the app is gone but check directories like %APPDATA%\Slack for remaining files containing session data.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[slack]]
- [[uninstallation]]
- [[windows]]
