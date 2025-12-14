---
id: proc-install-acronis-dragdrop-001
name: Install-Acronis-True-Image-via-Drag-and-Drop
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.045Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
tags:
  - macos
  - installation
  - permissions
commands: []
platforms:
  - macOS
tools: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---

# Install-Acronis-True-Image-via-Drag-and-Drop

## Summary

This procedure installs Acronis True Image on macOS using the drag-and-drop method from a DMG file, resulting in insecure permissions that allow admin users to write to the application bundle and its Contents/MacOS/ subfolder, setting the stage for privilege escalation.

## Description

In the attack scenario, an admin user downloads the Acronis True Image DMG and drags the app to /Applications/. This installation method does not enforce root:wheel ownership or restrictive permissions (e.g., 755 root-owned), leaving the folder writable by admins. This misconfiguration allows modification of binaries executed as root by LaunchDaemons, enabling local privilege escalation without passwords. Prerequisites include admin access and the DMG file from official sources.

## Requirements

1. Admin privileges on the target macOS system
2. Downloaded Acronis True Image DMG file
3. No prior installation (fresh setup)

## Defense

Defensive measures and detection strategies:

- Use pkg-based installers for applications to ensure proper ownership
- Monitor /Applications/ for unexpected permission changes using tools like Tripwire or macOS's fsevents
- Audit LaunchDaemons for paths in user-writable directories

## Objectives

1. Install the app with permissive permissions to enable binary replacement
2. Verify write access to /Applications/Acronis True Image.app/Contents/MacOS/
3. Prepare for escalation by confirming admin write capabilities

## Instructions

### Step 1: Download and Mount DMG

**Context**: Obtain and prepare the installation package.

Download the DMG from the official Acronis site and mount it:

```bash
hdiutil attach AcronisTrueImage.dmg
```

> This mounts the disk image containing the app bundle.

### Step 2: Drag-and-Drop Installation

**Context**: Perform the installation to set insecure permissions.

Drag Acronis True Image.app from the mounted volume to /Applications/ using Finder, or via command line:

```bash
cp -R /Volumes/Acronis\ True\ Image/Acronis\ True\ Image.app /Applications/
```

> Installation completes, setting permissions like drwxr-xr-x staff admin on the app and subfolders.

### Step 3: Verify Permissions

**Context**: Confirm the vulnerability is present.

Check ownership and permissions:

```bash
ls -la /Applications/Acronis\ True\ Image.app/
ls -la /Applications/Acronis\ True\ Image.app/Contents/MacOS/
```

> Expected: Writable by admin group, not root-only.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- macos
- installation
- permissions
