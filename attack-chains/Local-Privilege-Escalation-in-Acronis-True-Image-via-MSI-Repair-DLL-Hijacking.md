---
tags:
  - privilege-escalation
  - dll-hijacking
  - windows
  - acronis
  - msi
  - local-exploit
type: attack_chain
tools:
  - '[[tools/cmd-exe]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/msiexec-repair-msi]]'
  - '[[commands/whoami-check-privileges]]'
platforms:
  - Windows
complexity: medium
procedures:
  - '[[procedures/Identify-Acronis-MSI-File]]'
  - '[[procedures/Initiate-MSI-Repair-Process]]'
  - '[[procedures/Hijack-Schedule-DLL-in-TEMP]]'
  - '[[procedures/Complete-Repair-and-Handle-UAC]]'
  - '[[procedures/Verify-SYSTEM-Privilege-Escalation]]'
step_count: 5
techniques:
  - '[[DLL Search Order Hijacking]]'
  - '[[Bypass User Account Control]]'
description: >-
  A multi-stage local privilege escalation exploiting insecure MSI handling in
  Acronis True Image, allowing non-admin users to hijack a DLL loaded by an
  elevated process for SYSTEM-level code execution.
skill_level: intermediate
impact_level: high
id: a01aeeab-60b2-42d9-ba86-d2ec5080f066
created_at: '2025-12-14T17:29:44.293Z'
updated_at: '2025-12-14T17:29:44.293Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
  - '[[Bypass User Account Control]]'
---
# Local Privilege Escalation in Acronis True Image via MSI Repair DLL Hijacking

## Overview

This attack chain exploits a vulnerability in Acronis True Image where non-administrative users can access MSI installer files in the readable C:\Windows\Installer directory. By initiating a repair operation on the MSI, a 'schedule.dll' is created in the user-writable %TEMP% directory. Replacing this DLL with a malicious version allows DLL hijacking when the elevated MsiExec.exe process loads it, resulting in arbitrary code execution as NT AUTHORITY\SYSTEM. This enables attackers to install malware, rootkits, or perform lateral movement while evading detection.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify MSI File] --> B[Initiate Repair]
    B --> C[DLL Hijacking in TEMP]
    C --> D[Handle UAC and Execute]
    D --> E[Verify SYSTEM Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/cmd-exe]]

### Target Environment

- Windows OS with Acronis True Image installed
- Non-administrative user context
- Access to C:\Windows\Installer and %TEMP% directories

### Initial Access Requirements

- Local low-privilege account on the target system
- No network access required; fully local exploit

## Detailed Attack Procedures

### Step 1: Identify Acronis MSI File
procedure: [[procedures/Identify-Acronis-MSI-File]]

**Objective**: Locate the Acronis True Image MSI file in the Installer directory to prepare for repair exploitation.

**Instructions**: Open File Explorer or use command prompt to navigate to C:\Windows\Installer and search for MSI files authored by 'Acronis'. Note the random, unique filename (approximately 1.3 GB in size).

**Expected Output**: Identification of the target MSI file, e.g., a file like {GUID}.msi with Acronis metadata.

**Success Indicators**:
- MSI file located and path noted
- File confirmed as readable by non-admin user

### Step 2: Initiate MSI Repair Process
procedure: [[procedures/Initiate-MSI-Repair-Process]]

**Objective**: Trigger the MSI repair to create a vulnerable DLL in the writable %TEMP% directory.

**Instructions**: Use [[commands/msiexec-repair-msi]] from an elevated or standard cmd.exe to start the repair, which generates a temporary folder containing schedule.dll after a few seconds.

```cmd
msiexec /fa C:\Windows\Installer\installer_name.msi
```

**Expected Output**: A new folder appears in %TEMP% with schedule.dll; MsiExec.exe process starts.

**Success Indicators**:
- Temporary folder created in %TEMP%
- schedule.dll file present

### Step 3: Hijack Schedule DLL in TEMP
procedure: [[procedures/Hijack-Schedule-DLL-in-TEMP]]

**Objective**: Replace the legitimate DLL with a malicious one to hijack execution flow.

**Instructions**: Navigate to the newly created %TEMP% folder and substitute schedule.dll with a pre-prepared malicious DLL (e.g., one that spawns an elevated cmd.exe).

**Expected Output**: Malicious DLL in place; original file backed up if needed.

**Success Indicators**:
- DLL replacement confirmed
- No errors in file permissions

### Step 4: Complete Repair and Handle UAC
procedure: [[procedures/Complete-Repair-and-Handle-UAC]]

**Objective**: Allow the elevated MsiExec.exe to load the hijacked DLL while managing the UAC prompt.

**Instructions**: Let the repair process continue; when the UAC prompt appears for elevation, select 'No' to avoid additional interaction, enabling the DLL to load under SYSTEM context.

**Expected Output**: Repair completes; elevated cmd.exe pops up automatically.

**Success Indicators**:
- UAC handled without granting extra perms
- New elevated process launches

### Step 5: Verify SYSTEM Privilege Escalation
procedure: [[procedures/Verify-SYSTEM-Privilege-Escalation]]

**Objective**: Confirm successful escalation to NT AUTHORITY\SYSTEM.

**Instructions**: In the popped-up elevated cmd.exe, execute [[commands/whoami-check-privileges]] to validate privileges.

```cmd
whoami
```

**Expected Output**: Output shows 'nt authority\system'.

**Success Indicators**:
- whoami confirms SYSTEM user
- Arbitrary commands executable as SYSTEM

## Attack Chain Summary

### Key Achievements

1. Non-admin access to MSI triggers elevated DLL loading
2. DLL hijacking achieves SYSTEM code execution
3. Enables persistent malware deployment or lateral movement

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[DLL Search Order Hijacking]] Hijack DLL
- [[Bypass User Account Control]] Bypass User Account Control

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---
*Last updated: 2023-10-01*
