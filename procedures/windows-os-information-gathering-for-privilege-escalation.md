---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.595982+00:00'
updated_at: '2023-04-10T20:37:36.279741+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Execution through API|T1106 - Execution through API]]'
  - >-
    [[techniques/System Information Discovery|T1082 - System Information
    Discovery]]
sub_techniques: []
tags:
  - windows-privilege-escalation
  - windows-os-information
  - discovery
commands:
  - '[[commands/cmd-retrieve-os-name-and-version]]'
  - '[[commands/cmd-list-installed-hotfixes]]'
  - '[[commands/powershell-list-environment-variables]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-os-information-gathering-for-privilege-escalation

## Summary

This procedure collects essential operating system information on Windows systems, including version details, installed updates, architecture, environment variables, and available drives. This discovery technique is used during privilege escalation to identify misconfigurations, outdated patches, or architecture-specific vulnerabilities that can be exploited to gain higher privileges.

## Description

In privilege escalation scenarios, attackers often start by gathering system information to map the environment and pinpoint weaknesses. This procedure focuses on Windows systems, using built-in commands to query OS details without requiring additional tools. It targets elements like the OS build version to check for known exploits (e.g., unpatched vulnerabilities in older builds), update status to find missing security patches, architecture to select appropriate exploits, environment variables for path hijacking opportunities, and drive enumeration to locate sensitive data or writable locations. The technique aligns with passive reconnaissance from a low-privilege shell, minimizing detection risk while providing actionable intel for further escalation.

## Requirements

1. Command Prompt or PowerShell access on the target Windows system (local or remote via initial foothold).
2. Low-privilege user account sufficient for execution (no admin rights needed initially).
3. Windows OS (tested on Windows 7+; WMIC availability varies by version).

## Defense

- Regularly update and patch the operating system to address vulnerabilities.
- Implement the principle of least privilege to limit the impact of privilege escalation attacks.
- Monitor system logs (e.g., via Sysmon or Windows Event Logs) and network traffic for signs of suspicious activity, such as unusual WMIC or systeminfo executions.

## Objectives

1. Gather information about the Windows version, configuration, and architecture.
2. Identify vulnerabilities and weaknesses, such as missing patches or misconfigured paths.
3. Collect drive and environment details to support targeted escalation attempts.

## Instructions

### Step 1: Retrieve OS Name and Version

**Context**: Start by identifying the exact OS name and version to determine potential vulnerabilities tied to specific builds, such as privilege escalation exploits in outdated Windows versions.

**Command** ([[commands/cmd-retrieve-os-name-and-version]]):

```cmd
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```

> This filters the systeminfo output to show only the OS name and version lines. It helps verify if the system is vulnerable to known issues, like CVE-2019-0708 (BlueKeep) on older versions. Run in Command Prompt for best compatibility.

### Step 2: List Installed Hotfixes and Updates

**Context**: Check for installed patches to identify gaps in security updates, which could expose the system to escalation vectors like kernel exploits.

**Command** ([[commands/cmd-list-installed-hotfixes]]):

```cmd
wmic qfe
```

> The WMIC query lists all Quick Fix Engineering (QFE) updates with details like ID, installation date, and description. Cross-reference missing KBs against vulnerability databases to prioritize exploits.

### Step 3: Determine OS Architecture

**Context**: Identify if the system is 32-bit or 64-bit to select architecture-appropriate payloads or exploits, as some privilege escalation techniques differ by bitness.

**Code** ([[codes/cmd-os-architecture-discovery-with-fallback]]):

```cmd
wmic os get osarchitecture || echo %PROCESSOR_ARCHITECTURE%
```

> This attempts to use WMIC for precise architecture info; if WMIC fails (e.g., disabled or older OS), it falls back to the PROCESSOR_ARCHITECTURE environment variable. Output will indicate '64-bit' or 'x86' to guide tool selection.

### Step 4: List Environment Variables

**Context**: Enumerate environment variables to spot misconfigurations, such as writable PATH directories or credentials in vars like USERNAME/PASSWORD, which can aid in escalation via hijacking or credential reuse.

**Command** ([[commands/powershell-list-environment-variables]]):

```powershell
Get-ChildItem Env: | ft Key,Value
```

> This PowerShell cmdlet displays all environment variables in a formatted table. Look for variables like PATH (for injection points) or custom ones with sensitive data. Alternative in CMD: `set` for a simple list.

### Step 5: Enumerate System Drives

**Context**: Map all available drives to locate sensitive files, identify removable media, or find writable locations for dropping payloads during escalation.

**Code** ([[codes/mixed-shell-enumerate-windows-drives]]):

```cmd
wmic logicaldisk get caption || fsutil fsinfo drives
wmic logicaldisk get caption,description,providername
Get-PSDrive | where {$_.Provider -like "Microsoft.PowerShell.Core\FileSystem"}| ft Name,Root
```

> Run the first two lines in Command Prompt to list drive letters, descriptions, and providers using WMIC and fsutil (fallback if WMIC unavailable). Then switch to PowerShell for the third line to get filesystem drives with roots. This reveals mounted volumes, network drives, or hidden partitions for further exploration.
