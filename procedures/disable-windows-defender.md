---
id: 4e367af7-1ef3-4c2b-8ab8-0a9010427fae
name: Disable-Windows-Defender
type: procedure
verified: true
submitted: true
created_at: '2023-01-10T04:46:44.859969+00:00'
updated_at: '2023-05-25T19:55:41.712236+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - antivirus-bypass
  - defense-evasion
commands:
  - '[[commands/powershell-set-mppreference-disable-realtime]]'
  - '[[commands/mpcmdrun-remove-definitions]]'
  - '[[commands/powershell-set-mppreference-disable-ioav]]'
platforms:
  - Windows
tools: []
validated: true
---

# Disable-Windows-Defender

## Summary

This procedure disables Windows Defender's real-time protection and removes its definition updates to bypass antivirus scanning on a target Windows machine. It is useful during post-exploitation phases when Defender blocks further actions like script execution or file drops, but note that this requires administrative privileges and may trigger alerts on modern systems with enhanced logging.

## Description

Windows Defender is the built-in antivirus solution on Windows systems, providing real-time file scanning and protection against malware. Disabling it allows attackers to execute malicious payloads without interference. This procedure uses PowerShell cmdlets from the Windows Defender module to turn off real-time monitoring and IOAV (Input/Output Antivirus) protection. An alternative method uses the mpcmdrun.exe tool to remove virus definitions entirely. These techniques map to MITRE ATT&CK's Defense Evasion tactic, specifically impairing antivirus defenses. Success depends on having local admin rights; without them, the commands will fail. On newer Windows versions (10/11), these actions are logged in Event Viewer under Security and may require Group Policy overrides for persistence.

## Requirements

1. Administrative privileges on the target Windows machine (local admin or higher).
2. PowerShell execution policy allowing script runs (or bypass if restricted).
3. Access to the Windows Defender installation path (default: C:\Program Files\Windows Defender).
4. Windows 10 or later (procedure may not work on older versions without updates).

## Defense

Defensive measures and detection strategies:

- Enable PowerShell logging and module logging to capture Set-MpPreference invocations.
- Monitor Event ID 5007 in Windows Defender logs for definition removal attempts.
- Use AppLocker or WDAC (Windows Defender Application Control) to restrict mpcmdrun.exe execution.
- Implement endpoint detection rules for process creation of powershell.exe with Defender-related arguments.

## Objectives

1. Disable real-time scanning to prevent immediate payload detection.
2. Remove or disable antivirus definitions to weaken signature-based detection.
3. Verify Defender is impaired to allow subsequent malicious activities.
4. Minimize alerts by using verbose flags only if needed for troubleshooting.

## Instructions

### Step 1: Disable Real-Time Monitoring via PowerShell

**Context**: This step uses the Set-MpPreference cmdlet to turn off Windows Defender's real-time protection, which scans files and processes as they execute. Run this first if PowerShell is available and not blocked, as it requires fewer privileges than definition removal.

**Command** ([[commands/powershell-set-mppreference-disable-realtime]]):
```powershell
Set-MpPreference -DisableRealtimeMonitoring $true -Verbose
```

> This command sets the real-time monitoring flag to true (disabled) and provides verbose output for confirmation. If successful, Defender will no longer scan new files or processes in real-time. Check for errors like 'Access Denied' if privileges are insufficient.

### Step 2: Remove Virus Definitions Using mpcmdrun.exe

**Context**: If PowerShell is restricted or the above fails, use the built-in mpcmdrun.exe tool to remove all virus definitions, effectively crippling Defender's ability to detect known threats. This is a more aggressive approach and may take time as it downloads and purges updates.

**Command** ([[commands/mpcmdrun-remove-definitions]]):
```cmd
"C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All
```

> Execute this from an elevated Command Prompt. The -All flag removes all definition types (antivirus, ASB, etc.). Expected output includes progress messages like 'Removing definitions...' and a completion notice. Verify by checking if the Definitions folder is empty post-execution.

### Step 3: Disable IOAV Protection via PowerShell

**Context**: After removing definitions, further disable IOAV protection, which scans network I/O and cloud uploads. This complements the real-time disable and is useful if scripts or downloads are still being blocked.

**Command** ([[commands/powershell-set-mppreference-disable-ioav]]):
```powershell
Set-MpPreference -DisableIOAVProtection $true
```

> This targets specifically IOAV scanning. Run in an elevated PowerShell session. Success is indicated by no errors and a confirmation message. Test by attempting to run a previously blocked script.
