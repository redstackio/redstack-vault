---
tags:
  - privilege-escalation
  - unquoted-service-path
  - windows-service
  - acronis
type: attack_chain
tools:
  - '[[tools/i686-w64-mingw32-gcc]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/query-acronis-service-config]]'
  - '[[commands/compile-adduser-exe]]'
  - '[[commands/restart-acronis-service]]'
  - '[[commands/add-local-user]]'
  - '[[commands/add-user-to-administrators]]'
platforms:
  - Windows
complexity: medium
procedures:
  - '[[procedures/Identify-Unquoted-Service-Path-in-Acronis-Service]]'
  - '[[procedures/Compile-and-Place-Malicious-Executable-for-Path-Hijacking]]'
  - '[[procedures/Trigger-Service-Restart-to-Execute-Hijacked-Payload]]'
  - '[[procedures/Perform-Privilege-Escalation-via-Payload-Execution]]'
step_count: 4
techniques:
  - '[[System Service Discovery]]'
  - '[[Hijack Execution Flow]]'
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Create Account]]'
description: >-
  A multi-stage attack exploiting an unquoted service path vulnerability in the
  Acronis Nonstop Backup Service to achieve local privilege escalation to SYSTEM
  level by hijacking the executable path and executing arbitrary code.
skill_level: intermediate
impact_level: high
id: 028cd271-824f-43fa-906a-a7535649b8da
created_at: '2025-12-14T17:26:17.585Z'
updated_at: '2025-12-14T17:26:17.585Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[System Service Discovery]]'
  - '[[Hijack Execution Flow]]'
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Create Account]]'
---
# Local Privilege Escalation via Unquoted Service Path in Acronis True Image 2020

Multi-stage attack chain demonstrating exploitation of an unquoted service path in the Acronis True Image 2020 Nonstop Backup Service (afcdpsrv.exe) for local privilege escalation. The vulnerability allows an attacker with write access to specific directories to hijack the service execution path, leading to arbitrary code execution as SYSTEM upon service restart or reboot. This affects Windows systems running Acronis True Image 2020 Build 22510.

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
    A[Identify Vulnerable Service] --> B[Compile and Place Malicious EXE]
    B --> C[Trigger Service Restart]
    C --> D[Execute Privilege Escalation Payload]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/i686-w64-mingw32-gcc]]
- Windows command-line tools (sc, net)

### Target Environment

- Windows OS (tested on Windows 10/11)
- Acronis True Image 2020 Build 22510 installed
- Acronis Nonstop Backup Service running
- No specific ports required; local access only

### Initial Access Requirements

- Local low-privilege user account
- Write access to exploitable directories (e.g., C:\Program.exe or C:\Program Files (x86)\Common.exe) – often requires misconfigurations, alternate data streams, or bootable media
- No network access needed

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Service Configuration
procedure: [[procedures/Identify-Unquoted-Service-Path-in-Acronis-Service]]

**Objective**: Examine the Acronis Nonstop Backup Service to confirm the unquoted path vulnerability, which contains spaces and allows path hijacking.

**Instructions**: Query the service configuration using [[commands/query-acronis-service-config]] to inspect the ImagePath:

```cmd
sc qc "Acronis Nonstop Backup Service"
```

Look for the ImagePath value: C:\Program Files (x86)\Common Files\Acronis\CDP\afcdpsrv.exe. Verify it lacks quotes around the path due to spaces.

**Expected Output**: Service details showing unquoted ImagePath with spaces, confirming hijackable paths like C:\Program.exe or C:\Program Files (x86)\Common.exe.

**Success Indicators**:
- Unquoted path confirmed in output
- Potential hijack locations identified (e.g., C:\Program.exe exists as a writable spot)

### Step 2: Compile and Place Malicious Executable
procedure: [[procedures/Compile-and-Place-Malicious-Executable-for-Path-Hijacking]]

**Objective**: Build a malicious executable that adds a new admin user and place it in a hijackable directory to intercept the service execution.

**Instructions**: First, compile the payload source (adduser.c, containing net user and net localgroup calls) using [[commands/compile-adduser-exe]] on a system with MinGW cross-compiler:

```bash
i686-w64-mingw32-gcc adduser.c -o adduser.exe
```

Then, copy the resulting adduser.exe to an exploitable location, such as renaming it to match the hijack (e.g., C:\Program.exe or C:\Program Files (x86)\Common.exe). Ensure write permissions:

```cmd
copy adduser.exe "C:\Program.exe"
```

**Expected Output**: adduser.exe binary generated; successful copy to target directory.

**Success Indicators**:
- Executable compiled without errors
- File placed in hijack path with execute permissions

### Step 3: Trigger Service Execution
procedure: [[procedures/Trigger-Service-Restart-to-Execute-Hijacked-Payload]]

**Objective**: Restart the service to force Windows to resolve the hijacked path and execute the malicious executable as SYSTEM.

**Instructions**: Stop and start the Acronis Nonstop Backup Service using [[commands/restart-acronis-service]]:

```cmd
sc stop "Acronis Nonstop Backup Service"
sc start "Acronis Nonstop Backup Service"
```

Alternatively, reboot the system if service restart is insufficient.

**Expected Output**: Service restarts; malicious executable runs silently as SYSTEM.

**Success Indicators**:
- Service status changes to RUNNING
- No errors in event logs indicating path resolution failure
- New user account created (check via net user)

### Step 4: Verify and Utilize Escalated Privileges
procedure: [[procedures/Perform-Privilege-Escalation-via-Payload-Execution]]

**Objective**: Confirm the payload executed successfully by checking for the new administrator account created during hijack.

**Instructions**: After trigger, verify the new user was added using standard net commands. The payload automates [[commands/add-local-user]] and [[commands/add-user-to-administrators]], but manually check:

```cmd
net user
net localgroup administrators
```

Log in with the new credentials (username: hacker, password: P@ssword!) to confirm admin access.

**Expected Output**: New user listed in net user output; user in Administrators group.

**Success Indicators**:
- New admin user exists
- Ability to perform privileged actions (e.g., whoami /priv shows elevated rights)

## Attack Chain Summary

### Key Achievements

1. Identified unquoted service path vulnerability in Acronis service
2. Hijacked execution flow by placing malicious EXE in interceptable directory
3. Triggered SYSTEM-level execution of arbitrary code
4. Achieved persistent local admin access via new user creation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[System Service Discovery]] System Service Discovery
- [[Hijack Execution Flow]] Hijack Execution Flow
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Create Account]] Create Account

### MITRE ATT&CK Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01*
