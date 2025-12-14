---
tags:
  - lpe
  - setup
  - tools
type: procedure
tools:
  - '[[tools/symboliclink-testing-tools]]'
  - '[[tools/ransomware-simulator]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/mkdir-create-quarantine]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:51.612Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 53a1e4f9-f803-49a4-b5fb-854e2725cba8
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Download-and-Setup-Symbolic-Link-Tools

## Summary

This procedure downloads tools for creating symbolic links and sets up the ransomware simulator executable in a location detectable by Acronis Active Protection, while ensuring the quarantine folder is ready for abuse.

## Description

In the context of exploiting the Acronis anti_ransomware_service.exe, an unprivileged user must first acquire tools to create symlinks and place a custom ransomware simulator. The simulator mimics ransomware behavior to trigger detection, and the quarantine folder (C:\Acronis Active Protection Storage\Quarantine\) is created if needed since it's user-writable. This setup enables the subsequent symlink creation and overwrite without alerting the service prematurely. Prerequisites include local unprivileged access on a Windows system with Acronis installed.

## Requirements

1. Internet access to download from GitHub
2. Unprivileged user account on Windows
3. Acronis Active Protection service running
4. Ability to execute binaries and create directories

## Defense

Defensive measures and detection strategies:

- Monitor directory creations in C:\Acronis Active Protection Storage\ for suspicious activity
- Restrict write access to quarantine folders in security software configurations
- Log symlink creations using Windows auditing (enable Object Access auditing)

## Objectives

1. Obtain symlink creation tools
2. Prepare ransomware simulator for detection
3. Ensure quarantine folder exists for exploitation

## Instructions

### Step 1: Download Symbolic Link Tools

**Context**: Clone the repository containing tools like CreateSymlink.exe for symlink testing on Windows.

**Command** ([[commands/git-clone-tools]]):
```cmd
git clone https://github.com/googleprojectzero/symboliclink-testing-tools.git
```

> This downloads the tools; navigate to the directory and ensure CreateSymlink.exe is available.

### Step 2: Prepare Ransomware Simulator

**Context**: Copy the ransomware_sim.exe (a Go-based simulator that encrypts files but executes payload in quarantine) to C:\ProgramData for easy detection.

No direct command; manually copy ransomware_sim.exe to C:\ProgramData\ransomware_sim.exe.

> Expected: File placed without errors.

### Step 3: Create Quarantine Folder

**Context**: The unprivileged user can write to this path, so create it if missing.

**Command** ([[commands/mkdir-create-quarantine]]):
```cmd
mkdir "C:\Acronis Active Protection Storage\Quarantine\"
```

> Creates the directory; verify with dir command.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/mkdir-create-quarantine]]

## Tools Used

- [[tools/symboliclink-testing-tools]]
- [[tools/ransomware-simulator]]

## Tags

- lpe
- setup
- tools
