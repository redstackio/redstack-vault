---
type: tool
verified: true
platforms:
  - Windows
tags:
  - Enumeration
  - Privilege Escalation
url: 'https://github.com/PowerShellMafia/PowerSploit/tree/dev/Privesc'
commands:
  - '[[commands/download-powerup-ps1-script]]'
validated: true
---

# PowerUp

**Status**: Unverified

## Overview

PowerUp is a Windows PowerShell-based privilege escalation enumeration tool designed to identify common misconfigurations that can lead to privilege escalation vectors. It automates the discovery of potential attack paths such as unquoted service paths, weak service permissions, and registry-based vulnerabilities, making it a key tool for post-exploitation enumeration in red team engagements.

## Description

PowerUp focuses on scanning the Windows environment for misconfigurations that attackers can exploit to elevate privileges from a standard user to administrator or SYSTEM level. Once loaded as a PowerShell module, it provides functions like Invoke-AllChecks to run comprehensive checks and report exploitable issues with suggested exploitation methods. Note that PowerUp has not been actively maintained since around 2016, as the original developers shifted focus; a modern alternative is SharpUp (C# implementation), which offers similar functionality but fewer weaponized exploits.

## Features

- **Comprehensive Checks**: Scans for service misconfigurations, scheduled tasks, DLL hijacking opportunities, and registry weaknesses.
- **Automated Reporting**: Invoke-AllChecks runs all modules and outputs findings in a structured format, highlighting high-risk issues.
- **Modular Design**: Individual functions for targeted enumeration (e.g., Get-ModifiableService, Find-ProcessInject).
- **No Dependencies**: Pure PowerShell, runs on Windows systems with PowerShell 2.0+.

## Installation

### Requirements

- PowerShell 2.0 or later (standard on Windows 7+).
- Internet access for direct download (or manual file transfer).
- Execution policy allowing script execution (e.g., Set-ExecutionPolicy Bypass).

### Install Commands

Download the script directly using the built-in command:

```powershell
# Use the dedicated command for download
[[commands/download-powerup-ps1-script]]
```

Alternatively, clone the full PowerSploit repository:

```powershell
# If Git is available
Invoke-WebRequest -Uri 'https://github.com/PowerShellMafia/PowerSploit/archive/dev.zip' -OutFile 'PowerSploit.zip'
Expand-Archive 'PowerSploit.zip' -DestinationPath 'C:\Temp'
```

Then import the module:

```powershell
Import-Module 'C:\Temp\PowerSploit-dev\Privesc\PowerUp.ps1'
```

## Basic Usage

```powershell
# After downloading and importing
Invoke-AllChecks
```

### Common Options

| Option | Description |
|--------|-------------|
| `-Verbose` | Enable detailed output for troubleshooting |
| `-HTML` (in some functions) | Generate HTML report of findings |

## Examples

### Example 1: Basic Usage

```powershell
# Download, import, and run all checks
[[commands/download-powerup-ps1-script]]
. "$env:TEMP\PowerUp.ps1"
Invoke-AllChecks
```

### Example 2: Advanced Usage

```powershell
# Targeted check for modifiable services
. "$env:TEMP\PowerUp.ps1"
Get-ModifiableService -Verbose
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Information Discovery]] System Information Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery
- [[Process Discovery]] Process Discovery
- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism

### Tactics

- [[Discovery]] Discovery
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- PowerShell execution logs showing script downloads from GitHub (e.g., via AMSI or Module logging).
- Console output or file creation of PowerUp.ps1 in temp directories.
- Anomalous PowerShell commands like Invoke-AllChecks or Get-ModifiableService in process monitoring.
- Network connections to raw.githubusercontent.com during download.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/SharpUp]] (C# alternative for privilege escalation enumeration)
- [[tools/winPEAS]] (cross-platform enumeration script)

## References

- Official GitHub Repository: https://github.com/PowerShellMafia/PowerSploit/tree/dev/Privesc
- PowerUp Usage Guide: https://github.com/PowerShellMafia/PowerSploit/blob/dev/Privesc/PowerUp.ps1
- Related Blog Post: https://posts.specterops.io/let-the-bots-do-the-work-powerup-ps1-walkthrough-1b4e956f8221
