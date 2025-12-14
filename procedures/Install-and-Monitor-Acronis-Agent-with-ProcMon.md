---
id: proc-acronis-install-monitor
tags:
  - monitoring
  - installation
  - dll-search
type: procedure
tools:
  - '[[tools/ProcMon]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:29:36.858Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---
# Install-and-Monitor-Acronis-Agent-with-ProcMon

## Summary

This procedure installs the Acronis Cyber Protection Agent on a Windows system and uses Process Monitor (ProcMon) to observe the file access patterns of systeminfo.exe, specifically focusing on DLL loading attempts to identify search-order vulnerabilities.

## Description

The Acronis Cyber Protection Agent includes a utility at C:\Program Files\Common Files\Acronis\AdvReport\systeminfo.exe that runs with elevated privileges and searches for snapapi.dll in the system's PATH before its intended location. By installing the agent and monitoring with ProcMon, attackers can confirm the vulnerable search order, which prioritizes writable directories like C:\Python27. This sets the stage for hijacking in a local privilege escalation scenario. Prerequisites include local access to a Windows machine and download rights for the installer.

## Requirements

1. Windows OS with administrative install rights for the agent
2. Access to download the installer from https://mc-beta-cloud.acronis.com
3. ProcMon installed from Sysinternals

## Defense

Defensive measures and detection strategies:

- Restrict PATH modifications to trusted directories only
- Monitor for unexpected DLL loads in system utilities using EDR tools
- Apply least-privilege principles to agent installations

## Objectives

1. Successfully install the Acronis agent
2. Capture DLL search behavior for exploitation planning
3. Identify writable PATH directories for payload placement

## Instructions

### Step 1: Download and Install Acronis Agent

**Context**: Obtain and install the latest Cyber Protection Agent to introduce the vulnerable systeminfo.exe utility.

No specific command; manually download from https://mc-beta-cloud.acronis.com/download/u/baas/4.0/12.5.23130/Cyber_Protection_Agent_for_Windows_web.exe and run the installer, following on-screen prompts to complete setup.

> The installation places systeminfo.exe at C:\Program Files\Common Files\Acronis\AdvReport\systeminfo.exe. Verify by checking the directory post-install.

### Step 2: Launch ProcMon and Set Filters

**Context**: Start monitoring to capture file system activity from systeminfo.exe.

Launch ProcMon.exe from Sysinternals Suite.

> In ProcMon, go to Filter > Filter... and add: Process Name is systeminfo.exe, then Operation is CreateFile. This focuses on DLL load attempts.

### Step 3: Execute systeminfo.exe for Observation

**Context**: Run the utility to log DLL searches in ProcMon.

Execute the following (via Run dialog or command line):

```cmd
C:\Program Files\Common Files\Acronis\AdvReport\systeminfo.exe
```

> ProcMon will show searches for snapapi.dll in PATH folders (e.g., C:\Python27\snapapi.dll) with 'NAME NOT FOUND' results, confirming the hijackable order.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[DLL Search Order Hijacking]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ProcMon]]

## Tags

- monitoring
- installation
