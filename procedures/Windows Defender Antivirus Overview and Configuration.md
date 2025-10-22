---
id: 0ab2b46e-a3fe-47fb-aa6c-596d75997eff
name: Windows Defender Antivirus Overview and Configuration
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:26.630716+00:00'
updated_at: '2023-04-10T20:37:03.324651+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Security Software Discovery|T1063 - Security Software Discovery]]'
tags:
- '[[Windows Defender Antivirus]]'
- '[[Windows - Defenses]]'
commands:
- '[[Check Windows Defender status]]'
- '[[Disable Windows Defender scanning]]'
- '[[Enable Microsoft Defender]]'
- '[[Exclude folders from Windows Defender scanning]]'
- '[[Remove Windows Defender signatures]]'
- '[[Run a Full Scan]]'
- '[[Run a Quick Scan]]'
---

# Windows Defender Antivirus Overview and Configuration

## Summary

Windows Defender Antivirus is a built-in anti-malware solution that provides real-time protection against various types of threats. It uses machine learning and cloud-based protection to quickly detect and respond to new and emerging threats. Windows Defender Antivirus can be configured to meet the

## Description

# Description

Windows Defender Antivirus is a built-in anti-malware solution that provides real-time protection against various types of threats. It uses machine learning and cloud-based protection to quickly detect and respond to new and emerging threats. Windows Defender Antivirus can be configured to meet the specific needs of an organization, such as scanning schedules and exclusions. The use of Windows Defender Antivirus can help prevent the compromise of endpoints and protect sensitive data from theft or destruction.

## Requirements

1. Windows operating system

1. Administrator privileges

## Defense

1. Ensure that Windows Defender Antivirus is up-to-date with the latest security definitions

1. Configure Windows Defender Antivirus to scan all files and folders, including removable drives

1. Regularly review and update the Windows Defender Antivirus configuration to ensure it is aligned with the organization's security policies

## Objectives

1. To provide real-time protection against various types of threats

1. To configure Windows Defender Antivirus to meet the specific needs of an organization

1. To prevent the compromise of endpoints and protect sensitive data from theft or destruction

# Instructions

1. To use Microsoft Defender, simply open the Windows Security app and navigate to the Virus & threat protection section. From here, you can run quick or full scans, view scan history, and manage threat settings.

**Code**: [[Microsoft Defender]]

> Microsoft Defender provides real-time protection against viruses, malware, and other types of malicious software. It also includes features such as firewall and network protection, as well as browser and email protection. Microsoft Defender is designed to run in the background and keep your computer safe without requiring much user intervention.

**Command** ([[Enable Microsoft Defender]]):

```bash
To enable Microsoft Defender on Windows 10:
1. Open Windows Security.
2. Click on Virus & threat protection.
3. Under Virus & threat protection settings, click Manage settings.
4. Toggle the switch for Real-time protection to On.
```

**Command** ([[Run a Quick Scan]]):

```bash
To run a quick scan with Microsoft Defender:
1. Open Windows Security.
2. Click on Virus & threat protection.
3. Under Current threats, click Scan options.
4. Select Quick scan and click Scan now.
```

**Command** ([[Run a Full Scan]]):

```bash
To run a full scan with Microsoft Defender:
1. Open Windows Security.
2. Click on Virus & threat protection.
3. Under Current threats, click Scan options.
4. Select Full scan and click Scan now.
```

2. This command provides instructions on how to configure Windows Defender on a Windows machine. The command includes disabling real-time monitoring, disabling AMSI, excluding a folder and process from scanning, and removing signatures.

**Code**: [[# Check the status of Windows Defender
PS C:\> Get]]

> The command 'Get-MpComputerStatus' is used to check the status of Windows Defender on a Windows machine. The command 'Set-MpPreference' is used to disable real-time monitoring and AMSI. The command 'Set-MpPreference -DisableScriptScanning 1' is used to disable AMSI. The command 'Add-MpPreference' is used to exclude a folder and process from scanning. The command '& "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" -RemoveDefinitions -All' is used to remove all signatures from Windows Defender.

**Command** ([[Check Windows Defender status]]):

```bash
Get-MpComputerStatus
```

**Command** ([[Disable Windows Defender scanning]]):

```bash
Set-MpPreference -DisableRealtimeMonitoring $true; Get-MpComputerStatus
Set-MpPreference -DisableIOAVProtection $true
Set-MpPreference -DisableScriptScanning 1
```

**Command** ([[Exclude folders from Windows Defender scanning]]):

```bash
Add-MpPreference -ExclusionPath "C:\Temp"
Add-MpPreference -ExclusionPath "C:\Windows\Tasks"
Set-MpPreference -ExclusionProcess "word.exe", "vmwp.exe"
```

**Command** ([[Remove Windows Defender signatures]]):

```bash
& "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" -RemoveDefinitions -All
& "C:\Program Files\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All
```

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Security Software Discovery|T1063 - Security Software Discovery]]

## Commands Used

- [[Check Windows Defender status]]
- [[Disable Windows Defender scanning]]
- [[Enable Microsoft Defender]]
- [[Exclude folders from Windows Defender scanning]]
- [[Remove Windows Defender signatures]]
- [[Run a Full Scan]]
- [[Run a Quick Scan]]

## Tags

- [[Windows Defender Antivirus]]
- [[Windows - Defenses]]
