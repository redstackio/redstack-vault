---
id: 123e4567-e89b-12d3-a456-426614174002
name: Uninstall-Rockstar-Games-Launcher
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:31.055Z'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - uninstallation
  - data-retention
  - windows
commands: []
platforms:
  - Windows
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---

# Uninstall-Rockstar-Games-Launcher

## Summary

This procedure removes the Rockstar Games Launcher using standard Windows methods, but due to the vulnerability, it fails to clear stored profile data and auto sign-in flags from local storage.

## Description

The uninstall process via Control Panel or the installer does not target residual files in user directories like %AppData%, leading to persistence of sensitive data. This is the root cause of the vulnerability, allowing unauthorized access on reinstall. Tested on Windows 64-bit systems.

## Requirements

1. Installed Rockstar Games Launcher
2. Administrative privileges
3. Access to Windows Control Panel

## Defense

Defensive measures and detection strategies:

- Implement custom uninstall scripts to wipe AppData
- Use forensic tools to scan for residual app data post-uninstall
- Educate users on manual data cleanup

## Objectives

1. Trigger incomplete uninstallation
2. Retain local profile data
3. Set up for reinstallation test

## Instructions

### Step 1: Initiate Uninstallation

**Context**: Use built-in Windows tools to remove the application.

- Open Control Panel > Programs and Features.
- Locate "Rockstar Games Launcher".
- Right-click and select Uninstall, or use the installer's uninstaller if available.
- Follow prompts without selecting data removal options.

> Expected output: Confirmation of uninstall completion; application removed from Programs list.

### Step 2: Verify Incomplete Cleanup

**Context**: Check for remaining files to confirm data retention.

- Open File Explorer and navigate to %AppData%\Rockstar Games.
- Observe if profile files (e.g., login tokens) persist.

> Expected output: Residual files present, indicating vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools (partial, as uninstall evades full cleanup)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[uninstallation]]
- [[data-retention]]
- [[windows]]
