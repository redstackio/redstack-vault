---
id: b338f5ff-f18a-4747-99a8-c29a02309b77
name: exclude-folder-from-windows-defender
type: procedure
verified: true
submitted: true
created_at: '2020-03-04T18:38:21.982510+00:00'
updated_at: '2023-05-25T19:54:56.410181+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Disabling Security Tools|T1089 - Disabling Security Tools]]'
sub_techniques: []
tags:
  - '[[tags/administrator]]'
  - '[[tags/defender]]'
  - '[[tags/Defense Bypass]]'
commands:
  - '[[commands/add-mp-preference-exclusion-path]]'
platforms:
  - Windows
tools: []
validated: true
---

# exclude-folder-from-windows-defender

## Summary

This procedure excludes a specified folder from Windows Defender's real-time scanning using the Add-MpPreference PowerShell cmdlet. It requires administrative privileges and is effective on Windows systems with PowerShell 4.0 or later, allowing attackers to place tools or payloads in the excluded path without triggering antivirus detection.

## Description

Windows Defender is the built-in antivirus solution on Windows operating systems, performing real-time file scanning to detect malware. By adding an exclusion for a specific folder path, this procedure bypasses these scans for that location, enabling the execution of malicious tools, payloads, or scripts without interference. This is a common defense evasion technique during post-exploitation phases, such as after initial access or privilege escalation. The exclusion applies only to the specified path and does not disable Defender entirely, making it a subtle evasion method. It works on Windows 10, Windows 11, and Server editions where Defender is active. Note that this change persists until manually removed or Defender is reconfigured, but it may be logged in system events.

## Requirements

1. Administrative privileges on the target Windows system to modify Defender preferences.
2. PowerShell version 4.0 or higher (standard on Windows 10+).
3. Local or remote access to execute PowerShell commands (e.g., via WinRM for remote execution).
4. The target path must exist or be creatable; invalid paths will cause the command to fail.

## Defense

- Enable advanced auditing for PowerShell execution, including Module and Script Block Logging, to capture Add-MpPreference usage.
- Regularly review Windows Defender exclusions using Get-MpPreference -ExclusionPath in scheduled tasks or SIEM monitoring.
- Implement application whitelisting (e.g., via AppLocker) to restrict PowerShell to approved scripts.
- Monitor Event ID 5001 (Defender configuration changes) in Windows Security logs for unauthorized modifications.

## Objectives

1. Add a folder path to Windows Defender's exclusion list to prevent scanning of contents.
2. Verify the exclusion has been successfully applied without errors.
3. Enable placement of evasive tools or payloads in the excluded directory.

## Instructions

### Step 1: Add the Exclusion Path

**Context**: This step uses the Add-MpPreference cmdlet to configure Windows Defender to ignore scans on the specified folder. It is the core action of this procedure and requires replacing the placeholder with the actual path. Run this in an elevated PowerShell session to ensure administrative rights.

**Command** ([[commands/add-mp-preference-exclusion-path]]):
```powershell
Add-MpPreference -ExclusionPath "$_PATH"
```

> The command modifies the Defender configuration silently if successful. For example, to exclude C:\Temp\Tools, substitute $_PATH with "C:\\Temp\\Tools". If the path contains spaces, ensure it is properly quoted. This step accomplishes defense evasion by allowing files in the path to avoid real-time protection checks. To verify, run Get-MpPreference -ExclusionPath afterward to list all exclusions and confirm the new entry appears.
