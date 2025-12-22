---
id: acronis-exe-hijack-chain-2021
tags:
  - exe-hijacking
  - privilege-escalation
  - local-attack
  - windows-vulnerability
type: attack_chain
tools:
  - '[[tools/Procmon]]'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
verified: false
platforms:
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Download-and-Monitor-Acronis-Installer]]'
  - '[[procedures/Place-Malicious-EXE-in-Root-Directory]]'
  - '[[procedures/Observe-Hijacking-During-Installation]]'
step_count: 5
techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Path Interception by PATH Environment Variable]]'
updated_at: '2025-12-14T17:28:51.509Z'
description: >-
  A multi-stage attack exploiting an EXE hijacking vulnerability in the Acronis
  True Image 2021 installer to execute arbitrary code with elevated privileges,
  enabling local privilege escalation on Windows systems.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
  - '[[Path Interception by PATH Environment Variable]]'
---
# Local Privilege Escalation via EXE Hijacking in Acronis True Image 2021 Installer

Multi-stage attack chain demonstrating a complete workflow for exploiting an EXE hijacking vulnerability in the Acronis True Image 2021 installer (version 25.4.30480), where the installer process searches for and executes 'C:\program.exe' in the root directory, allowing arbitrary code execution with elevated privileges.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Download Installer] --> B[Monitor with Procmon]
    B --> C[Start Installation]
    C --> D[Observe Hijack Attempt]
    D --> E[Place and Execute Malicious EXE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Procmon]]

### Target Environment

- Windows OS (tested on Windows 10/11)
- Administrative privileges for installation (exploited for escalation)
- Write access to C:\ (may require chaining with another vuln)

### Initial Access Requirements

- Local user access to the target machine
- Ability to download files and run executables
- No network access required beyond downloading the installer

## Detailed Attack Procedures

### Step 1: Download the Acronis Installer
procedure: [[procedures/Download-and-Monitor-Acronis-Installer]]

**Objective**: Obtain the vulnerable installer and prepare monitoring to identify the hijacking path.

**Instructions**: Download the Acronis True Image 2021 installer (version 25.4.30480) from the official source. Launch Procmon to monitor file system activities.

**Expected Output**: Installer executable saved locally; Procmon running with filters set.

**Success Indicators**:
- Installer file downloaded successfully
- Procmon filters applied for 'atih_installer_shell_standard.exe' process and CreateFile operations

### Step 2: Start Monitoring with Procmon
procedure: [[procedures/Download-and-Monitor-Acronis-Installer]]

**Objective**: Capture file access attempts during installation to discover the vulnerable path.

**Instructions**: Use Procmon to filter on the installer process. No specific command needed; launch via GUI.

**Expected Output**: Procmon logs ready for capture.

**Success Indicators**:
- Filters active: Process Name is 'atih_installer_shell_standard.exe', Operation is 'CreateFile'
- Monitoring session started

### Step 3: Initiate Installation Process
procedure: [[procedures/Observe-Hijacking-During-Installation]]

**Objective**: Trigger the installer's file access to observe the hijackable path.

**Instructions**: Run the installer executable `AcronisTrueImage2021.exe` as administrator to simulate real installation.

**Expected Output**: Installation wizard starts; Procmon captures events.

**Success Indicators**:
- Installer launches with elevated privileges
- Procmon shows activity from the process

### Step 4: Observe Access to Vulnerable Path
procedure: [[procedures/Observe-Hijacking-During-Installation]]

**Objective**: Confirm the installer attempts to access 'C:\program.exe'.

**Instructions**: Review Procmon logs during installation for CreateFile operations targeting 'C:\program.exe'.

**Expected Output**: Log entry with 'NAME NOT FOUND' for 'C:\program.exe'.

**Success Indicators**:
- Detection of unexpected root directory access
- Confirmation of hijackable executable name

### Step 5: Place Malicious Executable and Exploit
procedure: [[procedures/Place-Malicious-EXE-in-Root-Directory]]

**Objective**: Hijack the execution by placing a malicious EXE in the path, leading to privilege escalation.

**Instructions**: Before restarting installation, copy a malicious 'program.exe' (e.g., one that spawns a shell or shows a message box) to C:\. Relaunch the installer to trigger execution.

**Expected Output**: Malicious EXE executes with elevated privileges during installation.

**Success Indicators**:
- Malicious payload runs (e.g., popup or shell spawn)
- Privilege escalation achieved if chained with write vuln

## Attack Chain Summary

### Key Achievements

1. Identified hidden EXE hijacking path in legitimate installer via process monitoring.
2. Demonstrated arbitrary code execution with admin rights during setup.
3. Highlighted chainability for full LPE on systems with partial write access to root.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow
- [[Path Interception by PATH Environment Variable]] Path Interception by Search Order Hijacking

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
