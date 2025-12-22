---
id: 37020e3e-e7f1-4af4-a65d-8c2704a7f363
type: tool
verified: true
created_at: '2020-03-04T05:39:38.734754+00:00'
updated_at: '2023-05-30T19:57:25.636401+00:00'
commands:
  - '[[commands/set-mp-preference-disable-realtime-monitoring]]'
platforms:
  - Windows
tags:
  - administrator
  - defender
  - Defense Bypass
url: 'https://docs.microsoft.com/en-us/powershell/module/defender/set-mppreference'
validated: true
---

# Set-MpPreference

**Status**: ✓ Verified

## Overview

Set-MpPreference is a PowerShell cmdlet used to configure Windows Defender preferences, including scans, updates, real-time protection, exclusions for files, folders, and processes, and default actions for threats. It is commonly used in security testing to modify antivirus behaviors for evasion purposes.

## Description

Set-MpPreference allows administrators to customize Windows Defender settings programmatically. Key capabilities include enabling/disabling real-time monitoring, adding exclusions to bypass scanning of specific paths or processes, and configuring scan schedules. In offensive security, it is often employed to weaken defenses post-compromise, such as disabling real-time protection to allow malware execution without detection.

## Features

- Feature 1: Toggle real-time protection on/off
- Feature 2: Add exclusions for files, folders, processes, and IP addresses
- Feature 3: Configure default actions for low/medium/high severity threats
- Feature 4: Manage update and scan preferences

## Installation

### Requirements

- Windows 10 or later with Windows Defender enabled
- PowerShell 5.1 or higher (pre-installed on modern Windows)
- Administrator privileges

### Install Commands

Set-MpPreference is installed by default with Windows Defender and PowerShell. No additional installation is required.

```powershell
# Verify availability
Get-Command Set-MpPreference
```

## Basic Usage

```powershell
Get-Help Set-MpPreference -Full
```

### Common Options

| Option | Description |
|--------|-------------|
| -DisableRealtimeMonitoring | Enable/disable real-time protection |
| -ExclusionPath | Add file/folder paths to exclusion list |
| -ExclusionProcess | Add process names to exclusion list |
| -MAPSReporting | Configure cloud protection reporting |

## Examples

### Example 1: Basic Usage

Disable real-time monitoring:

```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
```

### Example 2: Advanced Usage

Add an exclusion for a folder and disable behavior monitoring:

```powershell
Set-MpPreference -ExclusionPath "C:\Temp" -DisableBehaviorMonitoring $true
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor PowerShell execution logs for Set-MpPreference invocations
- Detection method 2: Audit changes in Windows Defender preferences via Event ID 5007 in Microsoft-Windows-Windows Defender/Operational
- Detection method 3: Baseline Defender settings and alert on unauthorized modifications

## Related Procedures

- [[procedures/disable-windows-defender]]

## Related Tools

- [[tools/Powershell]]

## References

- Official documentation: https://docs.microsoft.com/en-us/powershell/module/defender/set-mppreference
