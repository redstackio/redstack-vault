---
id: proc-acronis-download-monitor
tags:
  - reconnaissance
  - process-monitoring
  - windows
type: procedure
tools:
  - '[[tools/Procmon]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:28:51.505Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Download-and-Monitor-Acronis-Installer

## Summary

This procedure involves downloading the Acronis True Image 2021 installer and setting up monitoring with Procmon to capture file system interactions, revealing unexpected access paths for potential hijacking.

## Description

In the context of vulnerability research on Windows installers, this step prepares the environment by obtaining the target executable and using Sysinternals Procmon to log process activities. It targets the 'atih_installer_shell_standard.exe' subprocess, focusing on file create operations to identify paths like 'C:\program.exe' that can be exploited for EXE hijacking. Prerequisites include local access to a Windows machine and download permissions.

## Requirements

1. Internet access to download the installer from official Acronis sources.
2. Sysinternals Procmon installed (part of Windows Sysinternals Suite).
3. Administrative privileges to run Procmon and the installer.

## Defense

Defensive measures and detection strategies:

- Monitor installer processes with EDR tools for anomalous file accesses to root directories.
- Enforce application whitelisting to prevent unsigned EXEs in sensitive paths like C:\.
- Use file integrity monitoring to alert on changes to system directories.

## Objectives

1. Acquire the vulnerable installer version 25.4.30480.
2. Establish real-time monitoring of file system calls.
3. Identify exploitable paths without triggering the full exploit.

## Instructions

### Step 1: Download the Installer

**Context**: Obtain the specific vulnerable version to ensure reproducibility.

No command required; manually download from https://www.acronis.com/en-us/support/trueimage/2021/ or official archives.

> Save as 'AcronisTrueImage2021.exe' in a working directory.

### Step 2: Launch and Configure Procmon

**Context**: Set up filters to focus on the installer process and relevant operations.

Launch Procmon.exe (GUI tool):

- Go to Filter > Add > Process Name is 'atih_installer_shell_standard.exe' > Include
- Add another: Operation is 'CreateFile' > Include
- Start capture with Ctrl+E

> Expected output: Procmon interface showing active filters and ready for events.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Procmon]]

## Tags

- [[Reconnaissance]]
- [[process-monitoring]]
