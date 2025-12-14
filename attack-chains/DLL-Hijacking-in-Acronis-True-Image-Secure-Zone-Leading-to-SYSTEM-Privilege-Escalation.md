---
tags:
  - dll-hijacking
  - privilege-escalation
  - windows
  - acronis-true-image
type: attack_chain
tools:
  - '[[tools/Schtasks-EXE]]'
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
  - '[[procedures/Create-Acronis-Secure-Zone-Partition]]'
  - '[[procedures/Place-Malicious-DLL-in-User-PATH]]'
  - '[[procedures/Trigger-Aszbrowsehelper-EXE-to-Load-Malicious-DLL]]'
  - '[[procedures/Verify-Administrative-Privileges]]'
  - '[[procedures/Escalate-to-SYSTEM-via-Scheduled-Task]]'
  - '[[procedures/Execute-Scheduled-Task-as-SYSTEM]]'
step_count: 6
techniques:
  - '[[DLL Search Order Hijacking]]'
  - '[[Scheduled Task]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:29:09.438Z'
description: >-
  A multi-stage privilege escalation attack exploiting DLL search order
  hijacking in Acronis True Image 2021 to achieve full SYSTEM access on Windows.
skill_level: intermediate
impact_level: high
id: 73491d47-6a16-4f41-b0c5-8e0ed8a2ba1b
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
  - '[[Scheduled Task]]'
  - '[[Windows Command Shell]]'
---
# DLL Hijacking in Acronis True Image Secure Zone Leading to SYSTEM Privilege Escalation

Multi-stage attack chain demonstrating DLL search order hijacking in Acronis True Image 2021's aszbrowsehelper.exe, leading to administrative code execution and escalation to NT AUTHORITY\SYSTEM via scheduled tasks, resulting in full system compromise without requiring initial admin rights.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Secure Zone] --> B[Place Malicious DLL]
    B --> C[Trigger Process]
    C --> D[Verify Admin Privs]
    D --> E[Escalate to SYSTEM]
    E --> F[Execute as SYSTEM]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Schtasks-EXE]]
- C++ compiler (e.g., Visual Studio) for building malicious DLL

### Target Environment

- Windows OS (tested on Windows 10/11)
- Acronis True Image 2021 installed
- No open ports or services required beyond local access

### Initial Access Requirements

- Local user account (non-admin)
- Ability to install/reboot for Secure Zone creation
- No network access needed

## Detailed Attack Procedures

### Step 1: Create Acronis Secure Zone Partition
procedure: [[procedures/Create-Acronis-Secure-Zone-Partition]]

**Objective**: Establish the Secure Zone partition required to trigger the vulnerable aszbrowsehelper.exe process.

**Instructions**: Launch Acronis True Image 2021, navigate to the Tools tab, select Acronis Secure Zone, choose a partition, specify size (e.g., 500MB), proceed, and reboot to complete creation.

**Expected Output**: Secure Zone partition visible in Acronis interface post-reboot.

**Success Indicators**:
- Partition created successfully
- Reboot completes without errors

### Step 2: Place Malicious DLL in User-Controlled PATH Directory
procedure: [[procedures/Place-Malicious-DLL-in-User-PATH]]

**Objective**: Position the malicious tcmalloc.dll in a directory prioritized in the DLL search order.

**Instructions**: Compile the provided C++ code into tcmalloc.dll (payload: spawn cmd.exe as admin). Copy the DLL to %USERPROFILE%\AppData\Local\Microsoft\WindowsApps, which is in the user PATH and writable without admin rights.

**Expected Output**: DLL placed in target directory, verifiable via dir command.

**Success Indicators**:
- DLL file exists in the directory
- No permission errors during copy

### Step 3: Trigger the Vulnerable Process to Load the Malicious DLL
procedure: [[procedures/Trigger-Aszbrowsehelper-EXE-to-Load-Malicious-DLL]]

**Objective**: Invoke aszbrowsehelper.exe to load tcmalloc.dll from the hijacked PATH, executing the payload.

**Instructions**: In Acronis True Image, go to Tools tab and open Manage Acronis Secure Zone Wizard, or browse the Secure Zone in Windows Explorer. This launches aszbrowsehelper.exe, which searches for tcmalloc.dll in user PATH and executes the malicious code, spawning an elevated cmd.exe.

**Expected Output**: Elevated command prompt window appears.

**Success Indicators**:
- cmd.exe spawns without errors
- Process triggers on Secure Zone access

### Step 4: Confirm Administrative Privileges
procedure: [[procedures/Verify-Administrative-Privileges]]

**Objective**: Validate that the spawned shell has administrative rights.

**Instructions**: In the spawned cmd.exe, execute [[commands/net-session-verify-admin]] to check for admin access.

```cmd
net session
```

**Expected Output**: "There are no entries in this list" indicates admin; "Access denied" indicates failure.

**Success Indicators**:
- Output confirms admin privileges
- No access denied error

### Step 5: Escalate from Admin to SYSTEM Using Scheduled Task
procedure: [[procedures/Escalate-to-SYSTEM-via-Scheduled-Task]]

**Objective**: Leverage admin rights to create a scheduled task running as SYSTEM.

**Instructions**: In the elevated cmd.exe, execute [[commands/schtasks-create-elevated-task]] to set up the task.

```cmd
schtasks /create /SC WEEKLY /RU "NT AUTHORITY\SYSTEM" /TN EOP /TR C:\Windows\System32\winver.exe /IT /RL HIGHEST
```

**Expected Output**: "SUCCESS: The scheduled task \"EOP\" has successfully been created".

**Success Indicators**:
- Task created without errors
- Task listed in schtasks /query

### Step 6: Run the Scheduled Task to Execute as SYSTEM
procedure: [[procedures/Execute-Scheduled-Task-as-SYSTEM]]

**Objective**: Trigger the task to run winver.exe (or payload) as NT AUTHORITY\SYSTEM.

**Instructions**: In the elevated cmd.exe, execute [[commands/schtasks-run-elevated-task]] to start the task immediately.

```cmd
schtasks /run /I /TN EOP
```

**Expected Output**: "SUCCESS: Attempted to run the scheduled task \"EOP\""; winver.exe runs as SYSTEM (verifiable via Task Manager).

**Success Indicators**:
- Task runs successfully
- Process executes under SYSTEM context

## Attack Chain Summary

### Key Achievements

1. Hijack DLL loading in aszbrowsehelper.exe without admin rights
2. Achieve administrative code execution via malicious DLL
3. Escalate to full SYSTEM privileges using built-in schtasks
4. Compromise the system for persistent or further exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[DLL Search Order Hijacking]]
- [[Scheduled Task]]
- [[Windows Command Shell]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
