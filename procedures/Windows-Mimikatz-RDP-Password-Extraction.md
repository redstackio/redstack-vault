---
id: ff0152e4-76ed-437d-98ac-f780ed474c15
name: Windows-Mimikatz-RDP-Password-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.450645+00:00'
updated_at: '2024-10-01T12:00:00+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques:
  - '[[techniques/OS Credential Dumping|T1003.001 - LSASS Memory]]'
tags:
  - '[[tags/RDP Passwords]]'
  - '[[tags/Windows - Mimikatz]]'
  - credential-dumping
commands:
  - '[[commands/procdump64-create-process-dump]]'
  - '[[commands/mimikatz-extract-logon-passwords]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
  - '[[tools/ProcDump]]'
validated: true
---

# Windows-Mimikatz-RDP-Password-Extraction

## Summary

This procedure uses Mimikatz to extract plaintext passwords associated with RDP (Remote Desktop Protocol) sessions from the memory of a compromised Windows system. RDP credentials are often stored in cleartext within the LSASS process during active sessions, making them recoverable with tools like Mimikatz. An alternative manual method using Procdump to create a memory dump for offline analysis is also included for scenarios where direct execution of Mimikatz is risky or blocked.

## Description

In Windows environments, when a user connects via RDP, their credentials are loaded into memory by the LSASS process for authentication and session management. Mimikatz exploits this by enabling SeDebugPrivilege to read LSASS memory directly, dumping details like usernames, domains, and plaintext passwords for interactive logons (including RDP). The 'ts::logonpasswords' module specifically targets Terminal Services (RDP) logon data. This technique is common in post-exploitation for credential harvesting to enable lateral movement to other RDP-enabled systems. The manual alternative involves dumping LSASS memory with Procdump, exfiltrating the dump, and analyzing it with string extraction tools to locate passwords. This procedure assumes a compromised system with local admin access and targets Windows 7-11/Server editions where LSA protection is not enabled.

## Requirements

1. Local administrator privileges on the target Windows system to access LSASS and enable debug privileges.
2. Mimikatz executable downloaded and placed on the target (for primary method); avoid antivirus detection by renaming or using in-memory execution.
3. Procdump executable (for alternative method); part of Microsoft Sysinternals suite.
4. For offline analysis, a separate analysis machine (e.g., Kali Linux) with tools like strings and grep, plus network access to exfiltrate the dump file (dumps can be 100MB+).
5. Task Manager or command-line access to identify process PIDs.

## Defense

- Enable LSA Protection and Credential Guard via Group Policy to isolate and protect LSASS memory from unauthorized access.
- Deploy endpoint detection and response (EDR) tools that monitor for SeDebugPrivilege elevation, LSASS access, or known Mimikatz behaviors (e.g., YARA rules for Mimikatz strings).
- Use application whitelisting (e.g., AppLocker) to block execution of unsigned binaries like mimikatz.exe or procdump.exe.
- Monitor for large file creations in temp directories and anomalous network exfiltration of .dmp files.
- Implement multi-factor authentication (MFA) for RDP to reduce credential value even if extracted.

## Objectives

1. Recover plaintext RDP and logon passwords from active sessions for reuse in lateral movement.
2. Harvest credentials without triggering real-time alerts by using offline dump analysis if needed.
3. Identify associated domains, usernames, and authentication types for further targeting.

## Instructions

### Step 1: Alternative Method - Identify and Dump LSASS Process Memory

**Context**: Before dumping, identify the PID of lsass.exe, as it holds credential data. This step creates a full memory dump for offline extraction, useful if Mimikatz is detected by AV/EDR.

**Command** ([[commands/procdump64-create-process-dump]]):
```cmd
procdump64.exe -ma $_PID -accepteula $_OUTPUT_FILE
```

> Run as administrator. First, find the lsass PID with `tasklist /fi "imagename eq lsass.exe"`. Replace $_PID with the PID (e.g., 988) and $_OUTPUT_FILE with a path like C:\temp\lsass.dmp. This performs a full memory acquisition (-ma). Expected output: Confirmation of dump creation, e.g., "[13:45:30] Dump file written to lsass.dmp". Verify the file size (should be several hundred MB).

### Step 2: Alternative Method - Analyze Dump for Passwords

**Context**: Exfiltrate the dump file to an attacker-controlled machine for analysis to avoid on-target tools. Search for password strings in the dump, focusing on RDP-related contexts like "rdpcred" or logon buffers.

**Instructions**: On a Linux analysis machine (e.g., Kali), use strings to extract ASCII/Unicode strings longer than default, then grep for password indicators.

```bash
strings -el $_DUMP_FILE | grep -i "password\|rdp" -A 5 -B 5
```

> Replace $_DUMP_FILE with the path to lsass.dmp. The -el flag extracts little-endian Unicode strings. Expected output: Lines showing potential credentials, e.g., "Username: user Domain: CORP Password: Pass123". Manually review for valid plaintext; false positives are common. Success if RDP session passwords are recovered in context.

### Step 3: Primary Method - Extract Passwords with Mimikatz

**Context**: Use Mimikatz directly on the target for immediate credential access. This requires running Mimikatz interactively or non-interactively; the interactive mode uses the preserved code snippet for step-by-step execution.

**Command** ([[commands/mimikatz-extract-logon-passwords]]):
```cmd
mimikatz.exe "privilege::debug" "ts::logonpasswords" "exit"
```

> Run as administrator from the directory containing mimikatz.exe. This non-interactive invocation enables debug mode and dumps Terminal Services logon passwords (RDP-specific). Expected output: Detailed logon sessions with credentials, e.g., "Password: ActualRDPpass". If interactive is preferred, launch `mimikatz.exe` and input the commands from [[codes/Mimikatz-Debug-and-Logon-Passwords]]. Verify success by presence of plaintext passwords in the output; no passwords indicate protected memory or inactive sessions.
