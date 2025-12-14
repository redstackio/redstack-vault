---
id: proc-examine-acronis-plists-001
name: Examine-Acronis-LaunchDaemon-Plist-Files
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.041Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
tags:
  - macos
  - launchdaemons
  - recon
commands:
  - '[[commands/cat-acronis-launchdaemons]]'
platforms:
  - macOS
tools: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---

# Examine-Acronis-LaunchDaemon-Plist-Files

## Summary

This procedure examines the LaunchDaemon plist files for Acronis services to identify root-executed binaries located in the writable /Applications/Acronis True Image.app/Contents/MacOS/ folder, revealing opportunities for privilege escalation.

## Description

Targeting macOS systems with Acronis True Image installed via drag-and-drop, this reconnaissance step reviews XML plist files in /Library/LaunchDaemons/com.acronis.*. These daemons run as root and reference executables like prl_stat, mms_mini.sh, and schedul2 from the app's MacOS directory. By identifying these, an attacker can select a target for replacement. Expected outcome: Discovery of vulnerable paths and triggers like RunAtLoad or StartInterval.

## Requirements

1. Admin access to read /Library/LaunchDaemons/
2. Acronis True Image installed
3. Built-in cat command available

## Defense

Defensive measures and detection strategies:

- Restrict read access to LaunchDaemons to root
- Log access to /Library/LaunchDaemons/ using auditd
- Validate plist integrity post-installation

## Objectives

1. Identify root binaries in writable locations
2. Note daemon triggers for exploitation
3. Map execution flow for hijacking

## Instructions

### Step 1: List Acronis LaunchDaemons

**Context**: Locate the relevant plist files.

```bash
ls /Library/LaunchDaemons/com.acronis.*
```

> Lists files like com.acronis.acep.plist.

### Step 2: Display Plist Contents

**Context**: Review configurations to find vulnerable binaries.

Execute [[commands/cat-acronis-launchdaemons]] to view the plists:

```bash
cat /Library/LaunchDaemons/com.acronis.*
```

> Outputs XML with <ProgramArguments> pointing to /Applications/Acronis True Image.app/Contents/MacOS/ binaries, run as <UserName>root</UserName>, with keys like <RunAtLoad>true</RunAtLoad> or <StartInterval>1209600</StartInterval>.

### Step 3: Analyze for Targets

**Context**: Identify suitable binaries for replacement.

Manually parse output for paths like mms_mini.sh or prl_stat, confirming they are in the writable MacOS folder.

> Success: Binaries executable as root from modifiable directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/cat-acronis-launchdaemons]]

## Tools Used


## Tags

- macos
- launchdaemons
- recon
