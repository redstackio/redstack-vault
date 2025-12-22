---
type: tool
description: >-
  JAWS is a PowerShell enumeration script designed to identify privilege
  escalation vectors on Windows systems by collecting detailed system
  information.
url: 'https://github.com/411Hall/JAWS'
verified: true
created_at: '2020-02-07T16:32:58.398919+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/jaws-run-privilege-escalation-enumeration]]'
tags:
  - Enumeration
  - Privilege Escalation
platforms:
  - Windows
validated: true
---

# JAWS-Just-Another-Windows-Script

**Status**: Unverified

## Overview

JAWS (Just Another Windows [Enum] Script) is a PowerShell 2.0-compatible script that automates the collection of system information on Windows hosts to uncover potential privilege escalation opportunities. It is particularly useful during penetration testing and red team engagements for post-exploitation enumeration, helping identify misconfigurations, weak permissions, and exploitable services.

## Description

JAWS performs comprehensive enumeration across categories such as user accounts, services, scheduled tasks, registry keys, file permissions, and network configurations. It outputs findings in a structured format, highlighting potential vectors like unquoted service paths, writable service binaries, and always-installed drivers. The script is lightweight, runs entirely in memory if downloaded remotely, and supports HTML report generation for easier analysis. It is commonly used in Windows environments to simulate attacker reconnaissance after initial access.

## Features

- **Comprehensive Enumeration**: Covers users, groups, services, tasks, registry, filesystem, and network details.
- **Privilege Escalation Focus**: Specifically flags common priv esc vectors like weak service permissions and credential exposures.
- **Output Flexibility**: Console output, CSV, or HTML reports.
- **Stealth Options**: Runs without writing files to disk when executed via IEX (Invoke-Expression).
- **Compatibility**: Works on Windows 7+ with PowerShell 2.0+, including Server editions.

## Installation

### Requirements

- PowerShell 2.0 or higher (default on Windows 7+).
- Administrative privileges recommended for full enumeration (script can run as standard user but with limited scope).
- Internet access if downloading remotely.

### Install Commands

JAWS does not require traditional installation; it is a single PowerShell script.

```powershell
# Download and save locally (Kali/Ubuntu with PowerShell Core or Windows)
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/411Hall/JAWS/master/JAWS.ps1" -OutFile "JAWS.ps1"

# Or run directly in memory (no disk footprint)
powershell.exe -nop -exec bypass -c "IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/411Hall/JAWS/master/JAWS.ps1')"
```

On Kali Linux (with PowerShell via pwsh):
```bash
# Install PowerShell if needed
sudo apt update && sudo apt install -y powershell

# Then run as above using pwsh
pwsh -nop -exec bypass -c "IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/411Hall/JAWS/master/JAWS.ps1')"
```

## Basic Usage

```powershell
# Run with default console output
.\JAWS.ps1

# Generate HTML report
.\JAWS.ps1 -HTMLReport

# Run and exit immediately
.\JAWS.ps1 -NoExit:$false
```

### Common Options

| Option | Description |
|--------|-------------|
| `-HTMLReport` | Generates an HTML report file with findings. |
| `-NoExit` | Keeps the PowerShell session open after execution (default: true). |
| `-CSVReport` | Outputs results to CSV files for parsing. |
| `-User` | Specifies a user context for enumeration (if running as admin). |

## Examples

### Example 1: Basic Enumeration

Run JAWS to enumerate the local system and display potential priv esc vectors in the console.

```powershell
powershell.exe -ExecutionPolicy Bypass -File JAWS.ps1
```

### Example 2: Generate HTML Report

Execute JAWS and save findings to an HTML file for offline review.

```powershell
powershell.exe -ExecutionPolicy Bypass -File JAWS.ps1 -HTMLReport
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]] Process Discovery
- [[System Information Discovery]] System Information Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery
- [[T1087.001]] Account Discovery: Local Account
- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism

### Tactics

- [[Discovery]] Discovery
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- PowerShell execution logs showing downloads from GitHub or script invocation (e.g., via Event ID 4104 ScriptBlock Logging).
- File creation of JAWS.ps1 or HTML/CSV reports in temp directories.
- Anomalous PowerShell processes with high CPU during enumeration.
- Network connections to raw.githubusercontent.com.
- AMSI (Antimalware Scan Interface) alerts on script execution.

## Related Procedures

- [[procedures/Windows-Privilege-Escalation-Enumeration]]
- [[procedures/Post-Exploitation-System-Reconnaissance]]

## Related Tools

- [[tools/PowerUp]]
- [[tools/winPEAS]]
- [[tools/SharpUp]]

## References

- Official GitHub Repository: https://github.com/411Hall/JAWS
- Author: Justin Metz (@411Hall)
- Related Blog: https://blog.netspi.com/jaws-just-another-windows-enum-script/
