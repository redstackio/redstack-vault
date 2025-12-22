---
id: 5af28218-c780-4c01-ad68-be7010c1fe5e
type: tool
verified: true
created_at: '2020-03-04T18:53:49.229196+00:00'
updated_at: '2023-05-30T19:55:23.144003+00:00'
platforms:
  - Windows
tags:
  - administrator
  - defender
  - defense-evasion
commands:
  - '[[commands/add-mp-preference-add-exclusion-path]]'
url: 'https://docs.microsoft.com/en-us/powershell/module/defender/add-mppreference'
validated: true
---

# Add-MpPreference

**Status**: ✓ Verified

## Overview

Add-MpPreference is a PowerShell cmdlet that modifies Windows Defender Antivirus preferences. It is commonly used in security testing to adjust scan settings, add exclusions for files, folders, processes, or extensions, and configure threat detection behaviors. In offensive security operations, it aids in defense evasion by disabling real-time protection or excluding malicious payloads from scanning.

## Description

This cmdlet allows granular control over Windows Defender settings without needing to edit registry keys or use the GUI. Key capabilities include adding paths to exclusion lists to bypass scanning, setting default actions for threats (e.g., quarantine or remove), and enabling/disabling features like cloud protection. It requires administrative privileges and is available in Windows 10 and Server editions with Defender installed. Use it during post-exploitation to maintain persistence by evading endpoint detection.

## Features

- Add exclusions for paths, processes, extensions, and IP addresses to prevent scanning.
- Configure real-time protection, cloud-delivered protection, and automatic sample submission.
- Set threat action defaults (e.g., block, allow, or prompt).
- Enable or disable specific scan types (quick, full, custom).
- Integrate with PowerShell scripting for automated configuration changes.

## Installation

### Requirements

- Windows 10 or later with Windows Defender enabled.
- PowerShell 3.0 or higher (pre-installed on modern Windows).
- Administrative privileges to execute.

### Install Commands

No installation required; it is a built-in cmdlet in the Defender module, which loads automatically in elevated PowerShell sessions.

```powershell
# Import the module if needed (usually auto-loaded)
Import-Module Defender
```

## Basic Usage

```powershell
Get-Help Add-MpPreference -Full
```

### Common Options

| Option | Description |
|--------|-------------|
| -ExclusionPath | Adds a file or folder path to the exclusion list |
| -ExclusionExtension | Adds a file extension to exclude (e.g., .exe) |
| -ExclusionProcess | Excludes processes from scanning |
| -DisableRealtimeMonitoring | Disables real-time protection |
| -MAPSReporting | Configures Microsoft Active Protection Service reporting |

## Examples

### Example 1: Basic Usage

Add a folder exclusion to bypass scanning:

```powershell
Add-MpPreference -ExclusionPath "C:\Temp"
```

### Example 2: Advanced Usage

Disable real-time monitoring and add multiple exclusions:

```powershell
Add-MpPreference -DisableRealtimeMonitoring $true -ExclusionPath "C:\Tools", "C:\Payloads"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools
- [[Indicator Blocking]] Indicator Removal on Host

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

- Monitor PowerShell execution logs for Add-MpPreference invocations (Event ID 4104 in Windows Event Logs).
- Audit changes to Defender preferences via Group Policy or registry (HKLM\SOFTWARE\Policies\Microsoft\Windows Defender).
- Use Sysmon to log process creation by powershell.exe with command-line arguments containing exclusion paths.
- Baseline exclusion lists and alert on unauthorized additions.

## Related Procedures

No related procedures documented.

## Related Tools

- [[PowerShell]]
- [[Get-MpPreference]]

## References

- Official Microsoft Documentation: https://docs.microsoft.com/en-us/powershell/module/defender/add-mppreference
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1562/001/
