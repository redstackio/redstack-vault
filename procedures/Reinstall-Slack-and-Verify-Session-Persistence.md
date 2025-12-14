---
tags:
  - slack
  - persistence
  - credentials
  - windows
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Windows
techniques:
  - '[[Credentials In Files]]'
skill_level: low
impact_level: high
detection_risk: medium
sub_techniques: []
id: f4d29860-b0be-4455-9bb8-ffab28915b77
created_at: '2025-12-14T17:31:19.728Z'
updated_at: '2025-12-14T17:31:19.728Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Reinstall-Slack-and-Verify-Session-Persistence

## Summary

This procedure reinstalls the Slack desktop app on Windows and confirms automatic re-authentication using persisted session data, exploiting the uninstallation flaw for unauthorized access.

## Description

After uninstallation, residual session files (e.g., in %APPDATA%\Slack) allow the app to restore the previous login upon reinstallation. Launching the fresh install bypasses credential entry, granting immediate access to the account. This enables attackers on shared devices to view messages, files, and admin controls without authentication, posing risks for data theft or privilege abuse. Source: HackerOne Report #238260.

## Requirements

1. 64-bit Windows with prior Slack session data intact
2. Internet access to download fresh installer
3. Physical access to the machine

## Defense

Defensive measures and detection strategies:

- Clear browser and app caches regularly on shared systems
- Enable Slack's 'Sign out on all devices' feature periodically
- Deploy EDR tools to detect anomalous app reinstalls and session restores

## Objectives

1. Restore access via persisted credentials without re-authentication
2. Validate full account compromise including admin features
3. Demonstrate impact in shared computer scenarios

## Instructions

### Step 1: Download Fresh Installer

**Context**: Obtain a new copy to simulate a legitimate reinstall.

Visit https://slack.com/downloads/windows and download the 64-bit .exe.

### Step 2: Install and Launch

**Context**: Run the installer and observe session restoration.

Execute the .exe, complete installation, then launch Slack. The app should auto-login using stored data.

> Expected: Direct access to workspaces without prompts; verify by checking messages or admin panels.

### Step 3: Validate Access

**Context**: Confirm unauthorized entry to sensitive areas.

Navigate to channels, direct messages, or admin settings to ensure full functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[slack]]
- [[session-persistence]]
- [[credentials-in-files]]
