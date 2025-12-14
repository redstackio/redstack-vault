---
id: 16c4f64b-6fce-496d-81c0-2774cb5129e0
name: >-
  Local Privilege Escalation to SYSTEM in UniFi Video v3.10.1 via Arbitrary File
  Deletion and DLL Hijacking
type: attack_chain
description: >-
  A multi-stage local privilege escalation attack exploiting improper folder
  permissions and DLL loading in UniFi Video v3.10.1 on Windows to gain SYSTEM
  access.
verified: false
submitted: true
step_count: 2
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:28:59.222Z'
procedures:
  - >-
    [[procedures/Exploit-Arbitrary-File-Deletion-in-UniFi-Video-tsExport-Folder]]
  - '[[procedures/Perform-DLL-Hijacking-in-UniFi-Video-for-SYSTEM-Access]]'
techniques:
  - '[[DLL Search Order Hijacking]]'
tactics:
  - '[[Privilege Escalation]]'
tags:
  - privilege-escalation
  - dll-hijacking
  - arbitrary-file-deletion
  - local-access
  - windows
platforms:
  - Windows
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---

# Local Privilege Escalation to SYSTEM in UniFi Video v3.10.1 via Arbitrary File Deletion and DLL Hijacking

The vulnerability in UniFi Video v3.10.1 for Windows allows local privilege escalation to SYSTEM through a combination of arbitrary file deletion in the .tsExport folder and DLL hijacking due to misconfigured SafeDllSearchMode. An attacker with local low-privilege access can delete critical files to facilitate hijacking, then place a malicious DLL in a searchable path. When the UniFi Video process (running as SYSTEM) loads the hijacked DLL, the attacker's code executes with elevated privileges, leading to full system compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Local Low-Priv Access] --> B[Arbitrary File Deletion]
    B --> C[DLL Hijacking]
    C --> D[SYSTEM Code Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Built-in Windows tools (cmd.exe, reg.exe)

### Target Environment

- Windows OS
- UniFi Video v3.10.1 installed and running as a service
- Local low-privilege user account

### Initial Access Requirements

- Local logon access to the Windows host
- No network access required
- No prior elevated privileges

## Detailed Attack Procedures

### Step 1: Arbitrary File Deletion
procedure: [[procedures/Exploit-Arbitrary-File-Deletion-in-UniFi-Video-tsExport-Folder]]

**Objective**: Exploit weak permissions on the .tsExport folder to delete a critical DLL file used by the UniFi Video process, creating an opportunity for DLL hijacking.

**Instructions**: Identify the installation path of UniFi Video, typically C:\Program Files\Ubiquiti UniFi Video. The .tsExport folder, often in %PROGRAMDATA%\UniFi Video\.tsExport, has improper permissions allowing low-priv users to delete files. Use the built-in del command to target and remove a non-essential but loadable DLL, such as a logging or utility DLL (e.g., example.dll), to force the process to search further in the DLL load order.

Execute [[commands/delete-target-dll]] to remove the target file:

```cmd
del /f "C:\Program Files\Ubiquiti UniFi Video\example.dll"
```

Verify deletion with dir:

```cmd
dir "C:\Program Files\Ubiquiti UniFi Video\example.dll"
```

**Expected Output**: The file is successfully deleted, and the dir command reports "File Not Found".

**Success Indicators**:
- Target DLL deleted without errors
- No access denied messages due to weak .tsExport folder permissions

### Step 2: DLL Hijacking and Execution
procedure: [[procedures/Perform-DLL-Hijacking-in-UniFi-Video-for-SYSTEM-Access]]

**Objective**: Hijack the DLL load by placing a malicious DLL in a directory included in the Windows DLL search order, leveraging the prior deletion to execute code as SYSTEM when the UniFi Video service restarts or loads modules.

**Instructions**: Confirm SafeDllSearchMode is disabled (value 0) using [[commands/query-safe-dll-search-mode]]:

```cmd
reg query "HKLM\System\CurrentControlSet\Control\Session Manager" /v SafeDllSearchMode
```

If confirmed, prepare a malicious DLL (e.g., using a tool like msfvenom outside this chain, or a pre-built PoC DLL that spawns a SYSTEM shell). Place it in a writable directory in the PATH or current working directory of the UniFi Video process, such as %TEMP%.

Use [[commands/copy-malicious-dll]] to stage the DLL:

```cmd
copy /y "C:\path\to\malicious.dll" "C:\Program Files\Ubiquiti UniFi Video\example.dll"
```

Restart the UniFi Video service to trigger loading:

```cmd
net stop "UniFi Video"
net start "UniFi Video"
```

**Expected Output**: The service restarts successfully, and the malicious DLL executes, providing a SYSTEM shell (e.g., via net user or whoami showing nt authority\system).

**Success Indicators**:
- Registry query shows SafeDllSearchMode=0
- Malicious DLL copied without permission issues
- Post-restart, attacker gains SYSTEM prompt or reverse shell

## Attack Chain Summary

### Key Achievements

1. Deleted critical files using .tsExport folder weakness to enable hijacking
2. Hijacked DLL load order due to misconfigured SafeDllSearchMode
3. Achieved full SYSTEM access, compromising the host

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[DLL Search Order Hijacking]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2024-01-01T00:00:00Z*
