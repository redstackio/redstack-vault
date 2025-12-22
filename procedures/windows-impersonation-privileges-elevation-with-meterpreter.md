---
type: procedure
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
  - '[[techniques/Process Injection|T1055 - Process Injection]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - eop-impersonation-privileges
  - meterpreter-getsystem-alternatives
  - windows-privilege-escalation
commands:
  - '[[commands/meterpreter-getsystem]]'
  - '[[commands/tokenvator-getsystem-cmd]]'
  - '[[commands/incognito-execute-nt-authority-system-cmd]]'
  - '[[commands/psexec-system-interactive-cmd]]'
  - '[[commands/run-getsystem-python-script]]'
tools:
  - '[[tools/meterpreter]]'
  - '[[tools/Tokenvator]]'
  - '[[tools/incognito]]'
  - '[[tools/psexec]]'
  - '[[tools/tokenx-priv-esc]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# windows-impersonation-privileges-elevation-with-meterpreter

## Summary

This procedure elevates privileges on a Windows system from a low-privileged account to SYSTEM level by abusing impersonation privileges, primarily using Meterpreter's getsystem command. It leverages access token manipulation to inject into privileged processes, enabling attackers to perform actions requiring high privileges such as installing malware or accessing sensitive data.

## Description

In a typical attack scenario, an attacker has gained initial access to a Windows system via a low-privileged user account, often through phishing or exploiting a vulnerability. This procedure uses post-exploitation tools like Meterpreter to escalate to SYSTEM privileges. Technically, the getsystem command in Meterpreter attempts multiple methods, including named pipe impersonation and token duplication from processes with SeDebugPrivilege, to impersonate the SYSTEM account. Alternative tools like Tokenvator, Incognito, PsExec, and custom scripts provide fallback options if the primary method fails. This is effective in environments without strict privilege separation or EDR monitoring for process injection. Prerequisites include an active Meterpreter session or equivalent shell access. Expected outcomes include a new shell or session running as NT AUTHORITY\SYSTEM, verified by commands like whoami.

## Requirements

1. Active low-privileged shell or Meterpreter session on the target Windows system (e.g., via initial access exploit).
2. Administrative tools installed or transferable, such as Metasploit for Meterpreter, or standalone executables like PsExec.
3. Network access if tools need to be downloaded or staged on the target.
4. SeDebugPrivilege enabled in a target process (common in many Windows environments).

## Defense

Defensive measures and detection strategies:

- Implement principle of least privilege: Restrict user accounts to minimal necessary permissions and monitor for unexpected privilege escalations.
- Deploy EDR tools to detect suspicious process injections, DLL loading, or token manipulations (e.g., monitor for SeDebugPrivilege abuse via Sysmon Event ID 10).
- Enable Windows Defender Credential Guard and Protected Process Light to prevent token theft and impersonation.
- Use application whitelisting to block unauthorized tools like PsExec or custom scripts, and audit PowerShell and command-line executions.

## Objectives

1. Escalate from low-privileged user to SYSTEM level using impersonation techniques.
2. Verify elevated access and maintain persistence if needed.
3. Enable further post-exploitation actions like data exfiltration or lateral movement.

## Instructions

### Step 1: Attempt Elevation with Meterpreter getsystem

**Context**: If a Meterpreter session is available (e.g., from Metasploit), use the built-in getsystem command to attempt privilege escalation via token manipulation and process injection. This tries multiple vectors automatically, such as impersonating via named pipes or debugging privileged processes.

**Command** ([[commands/meterpreter-getsystem]]):
```meterpreter
getsystem
```

> The command will output the method used (e.g., "Got system via technique 1 (NamedPipe") if successful. Verify with 'getuid' to confirm SYSTEM privileges. If it fails, proceed to alternatives.

### Step 2: Elevate Using Tokenvator Tool

**Context**: If getsystem fails, upload and run Tokenvator.exe, which injects a DLL into a SYSTEM process to elevate and spawn a cmd.exe shell. This relies on finding a process with impersonation privileges.

**Command** ([[commands/tokenvator-getsystem-cmd]]):
```cmd
Tokenvator.exe getsystem cmd.exe
```

> Expected output includes a new cmd.exe prompt running as SYSTEM. Use 'whoami /priv' to check for elevated privileges like SeDebugPrivilege.

### Step 3: Impersonate SYSTEM with Incognito

**Context**: Incognito allows stealing and impersonating tokens from existing processes. List available tokens first (incognito list_tokens -u), then execute a command as NT AUTHORITY\SYSTEM.

**Command** ([[commands/incognito-execute-nt-authority-system-cmd]]):
```cmd
incognito.exe execute -c "NT AUTHORITY\SYSTEM" cmd.exe
```

> Success spawns a cmd.exe as SYSTEM. If no SYSTEM token is available, it may fail; fallback to other methods.

### Step 4: Use PsExec for SYSTEM Shell

**Context**: PsExec from Sysinternals can create a SYSTEM service to spawn an interactive shell. Download psexec.exe if not present.

**Command** ([[commands/psexec-system-interactive-cmd]]):
```cmd
psexec -s -i cmd.exe
```

> Launches an interactive cmd.exe as SYSTEM. Verify with 'whoami' showing nt authority\system.

### Step 5: Run Custom Python Script for Elevation

**Context**: As a script-based alternative, use the getsystem.py from TokenX PrivEsc repository, which automates token extraction and impersonation.

**Command** ([[commands/run-getsystem-python-script]]):
```cmd
python getsystem.py
```

> The script will attempt elevation and output success or failure. Follow on-screen instructions for spawning a shell if successful.
