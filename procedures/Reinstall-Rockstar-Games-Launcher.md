---
id: 123e4567-e89b-12d3-a456-426614174003
name: Reinstall-Rockstar-Games-Launcher
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T12:00:00Z'
updated_at: '2025-12-14T17:31:31.053Z'
tactics:
  - '[[Persistence]]'
techniques:
  - '[[Registry Run Keys - Startup Folder]]'
sub_techniques: []
tags:
  - reinstallation
  - persistence
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
  - '[[Persistence]]'
mitre_techniques:
  - '[[Registry Run Keys - Startup Folder]]'
---

# Reinstall-Rockstar-Games-Launcher

## Summary

This procedure reinstalls the Rockstar Games Launcher on Windows, leveraging retained local data from prior installation to prepare for automatic authentication.

## Description

After uninstallation, reinstalling the launcher from official sources allows the application to detect and use persisted profile data, bypassing the need for re-authentication. This step is crucial in demonstrating the persistence vulnerability in the 64-bit Windows version.

## Requirements

1. Internet connection
2. Administrative privileges
3. Prior uninstallation with data retention

## Defense

Defensive measures and detection strategies:

- Scan for residual data before reinstalls
- Use virtual environments for testing
- Monitor registry and AppData changes

## Objectives

1. Reinstall the application
2. Trigger use of persisted data
3. Enable bypass verification

## Instructions

### Step 1: Download Installer

**Context**: Obtain the latest version for reinstall.

- Visit the official Rockstar Games download page.
- Download the Windows 64-bit launcher installer.

> Expected output: .exe file saved locally.

### Step 2: Perform Installation

**Context**: Run setup to place the app back on the system.

- Execute the downloaded .exe.
- Follow the installation wizard, selecting default options.

> Expected output: Launcher installed; ready to launch.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Registry Run Keys - Startup Folder]] Registry Run Keys / Startup Folder (analogous to auto-start data)

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[reinstallation]]
- [[Persistence]]
- [[windows]]
