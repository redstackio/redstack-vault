---
tags:
  - symlink
  - file-manipulation
  - macos
  - bypass
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/ln-create-symlink]]'
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:26.832Z'
sub_techniques: []
id: f98bdf3d-d1a0-4108-ad90-34b760d971ac
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create Symbolic Links to Redirect File Operations

## Summary

This procedure creates symbolic links on macOS to exploit the Mozilla VPN installer's improper resolution, redirecting file accesses to allow unprivileged control over root-privileged operations during installation.

## Description

As part of a privilege escalation attack, symbolic links are placed in paths the installer predicts, pointing to sensitive system areas. This manipulates the installer's logic to perform unauthorized writes or reads. Requires local unprivileged access and knowledge of vulnerable paths from analysis; results in setup for escalation without triggering defenses.

## Requirements

1. Temporary directory writable by unprivileged user (e.g., /tmp)
2. Identified vulnerable paths from installer analysis
3. macOS environment

## Defense

Defensive measures and detection strategies:

- Enforce safe path resolution in installers using realpath or chroot
- Log symlink creations via filesystem auditing (e.g., fseventsd)
- Restrict /tmp usage in privileged processes

## Objectives

1. Establish symlinks targeting root files
2. Ensure links are followed by installer without detection
3. Prepare for privilege escalation trigger

## Instructions

### Step 1: Prepare Temporary Directory

**Context**: Create a staging area for symlinks to avoid cluttering the system.

**Command** ([[commands/mkdir-create-dir]]):
```bash
mkdir -p /tmp/vpn-exploit
```

> This sets up /tmp/vpn-exploit. Expected output: Directory created successfully.

### Step 2: Create Redirecting Symlinks

**Context**: Link user-controlled files to root-protected targets the installer will access.

**Command** ([[commands/ln-create-symlink]]):
```bash
ln -s /etc/sudoers /tmp/vpn-exploit/target-sudoers
ln -s /Library/Preferences/com.apple.system.plist /tmp/vpn-exploit/redirect-pref
```

> These commands create symlinks. Verify with `ls -l /tmp/vpn-exploit`. Success: Links point to root areas, enabling redirection during install.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/ln-create-symlink]]
- [[commands/mkdir-create-dir]]

## Tools Used


## Tags

- [[symlink]]
- [[file-manipulation]]
- [[bypass]]
