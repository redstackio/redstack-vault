---
tags:
  - lpe
  - symlink
  - acronis
  - ransomware
  - privilege-escalation
  - windows-exploit
type: attack_chain
tools:
  - '[[tools/symboliclink-testing-tools]]'
  - '[[tools/requests-python-library]]'
  - '[[tools/ransomware-simulator]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Download-and-Setup-Symbolic-Link-Tools]]'
  - '[[procedures/Prepare-and-Trigger-Ransomware-Simulation]]'
  - '[[procedures/Create-Symlink-in-Quarantine-for-Overwrite]]'
  - '[[procedures/Trigger-Quarantine-Overwrite-via-REST-API-and-Verify]]'
step_count: 4
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:51.616Z'
description: >-
  Exploits a vulnerability in Acronis anti_ransomware_service.exe by abusing the
  user-writable quarantine folder to overwrite system files as SYSTEM via
  symlinks, achieving local privilege escalation on Windows.
skill_level: intermediate
impact_level: high
id: c7a0613e-eaae-4805-ac42-c8dc29f8871b
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Local Privilege Escalation in Acronis Anti-Ransomware Service via Quarantine Symlink Abuse

Multi-stage attack chain demonstrating local privilege escalation by exploiting the Acronis anti_ransomware_service.exe quarantine feature. An unprivileged user creates a symlink in the writable quarantine folder pointing to a system file, then triggers the service to copy a malicious ransomware simulator there as SYSTEM, overwriting the target file and enabling escalation to SYSTEM privileges.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Tools and Environment] --> B[Trigger Ransomware Detection]
    B --> C[Create Symlink for Overwrite]
    C --> D[Trigger Quarantine and Escalate]
    D --> E[Verify SYSTEM Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/symboliclink-testing-tools]]
- [[tools/requests-python-library]]
- [[tools/ransomware-simulator]]

### Target Environment

- Windows OS (tested on Windows 10/11)
- Acronis Active Protection installed with anti_ransomware_service.exe running
- Local unprivileged user access
- Port 6109 open locally for REST API (http://localhost:6109/alerts)

### Initial Access Requirements

- Local standard user account (no admin privileges needed initially)
- Ability to execute binaries and Python scripts
- No network access required beyond localhost

## Detailed Attack Procedures

### Step 1: Setup Tools and Environment
procedure: [[procedures/Download-and-Setup-Symbolic-Link-Tools]]

**Objective**: Obtain necessary tools for symlink creation and prepare the ransomware simulator in a detectable location.

**Instructions**: Download symbolic link testing tools from the repository and place the ransomware simulator executable in C:\ProgramData. Then create the quarantine folder if it doesn't exist using [[commands/mkdir-create-quarantine]]:

```cmd
mkdir "C:\Acronis Active Protection Storage\Quarantine\"
```

Copy ransomware_sim.exe to C:\ProgramData\ransomware_sim.exe.

**Expected Output**: Tools downloaded, simulator placed, quarantine directory created.

**Success Indicators**:
- symboliclink-testing-tools repository cloned successfully
- Quarantine folder exists and is writable
- ransomware_sim.exe is in ProgramData

### Step 2: Trigger Ransomware Detection
procedure: [[procedures/Prepare-and-Trigger-Ransomware-Simulation]]

**Objective**: Simulate ransomware activity to trigger Acronis detection without fully blocking the process.

**Instructions**: Execute the ransomware simulator targeting a user directory using [[commands/run-ransomware-simulator]]:

```cmd
ransomware_sim.exe C:\Users\UNPRIVILIEGEDUSER\"
```

Wait for the Acronis dialog to appear, then select 'block' but do not 'close' to keep the file in a detected state.

**Expected Output**: Acronis Active Protection detects the simulation and shows a block dialog.

**Success Indicators**:
- Ransomware simulation runs and targets the user folder
- Detection alert appears from Acronis
- File is blocked but not quarantined yet

### Step 3: Create Symlink for Overwrite
procedure: [[procedures/Create-Symlink-in-Quarantine-for-Overwrite]]

**Objective**: Create a symbolic link in the quarantine folder pointing to a sensitive system file for overwrite.

**Instructions**: Use CreateSymlink.exe from the tools to link a path in quarantine to a system executable, such as C:\Windows\SysWOW64\dpnsvr.exe, with [[commands/create-symlink-quarantine]]:

```cmd
CreateSymlink.exe "C:\Acronis Active Protection Storage\Quarantine\ProgramData\ransomware_sim.exe" "C:\Windows\SysWOW64\dpnsvr.exe"
```

**Expected Output**: Symlink created successfully without errors.

**Success Indicators**:
- Symlink exists in quarantine folder
- Points to the target system file
- No permission denied errors

### Step 4: Trigger Quarantine Overwrite via REST API and Verify
procedure: [[procedures/Trigger-Quarantine-Overwrite-via-REST-API-and-Verify]]

**Objective**: Use the service's REST API to move the detected file to quarantine, causing SYSTEM-level overwrite, then verify escalation.

**Instructions**: Run a Python script using the requests library to POST to http://localhost:6109/alerts, triggering the quarantine action on the detected ransomware_sim.exe. This causes the service to copy the file as SYSTEM to the symlink path, overwriting dpnsvr.exe.

After triggering, verify the overwrite by checking the file contents or attempting to run the modified binary for escalation.

**Expected Output**: API response confirms quarantine, target file overwritten with simulator content.

**Success Indicators**:
- REST API call succeeds and file is moved
- Target system file (e.g., dpnsvr.exe) contains ransomware_sim.exe payload
- Ability to execute the overwritten file as SYSTEM for further escalation

## Attack Chain Summary

### Key Achievements

1. Bypassed validation in Acronis quarantine to write arbitrary files as SYSTEM
2. Achieved local privilege escalation from unprivileged user to SYSTEM
3. Demonstrated symlink abuse in a security product for file overwrite

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation

---

*Last updated: 2023-10-01T00:00:00Z*
