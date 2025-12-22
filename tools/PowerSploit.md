---
id: f2063482-207f-4a17-aa4f-c4b6f723177b
type: tool
verified: true
created_at: '2019-08-28T21:17:33.769050+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Windows
tags:
  - Active Directory
  - hacking
  - persistence
  - powershell
url: 'https://github.com/PowerShellMafia/PowerSploit'
validated: true
---

# PowerSploit

**Status**: Unverified

## Overview

PowerSploit is a collection of Microsoft PowerShell modules designed to assist penetration testers and red teamers across all phases of an assessment, from reconnaissance and execution to persistence, privilege escalation, and exfiltration. It provides offensive security capabilities without requiring compilation or external dependencies beyond PowerShell itself.

## Description

PowerSploit consists of several modules and scripts that enable advanced post-exploitation techniques on Windows environments. It is particularly useful in Active Directory domains for enumeration, credential dumping, and maintaining access. The framework is modular, allowing selective loading of components like PowerView for domain reconnaissance or Mimikatz integration for credential extraction. Use it in controlled environments only, as it can trigger antivirus and EDR detections.

## Features

- **Execution**: Code injection and remote command execution capabilities.
- **Script Modification**: Obfuscation and encoding tools for payloads.
- **Persistence**: Mechanisms to establish long-term access via registry, services, or SSPs.
- **Antivirus Bypass**: Signature detection and evasion techniques.
- **Exfiltration**: Credential dumping, keylogging, screenshot capture, and file copying.
- **Mayhem**: Destructive functions for proof-of-concept attacks (use with extreme caution).
- **Privilege Escalation**: Automated checks for common privesc vectors via PowerUp.
- **Reconnaissance**: Network scanning, HTTP probing, DNS enumeration, and domain analysis via PowerView.

## Installation

### Requirements

- Windows system with PowerShell 2.0 or later.
- Git (optional, for cloning).
- Administrative privileges for module installation in system directories.

### Install Commands

```powershell
# Clone the repository from GitHub (dev branch recommended for latest features)
git clone https://github.com/PowerShellMafia/PowerSploit.git -b dev

# Copy the PowerSploit folder to the PowerShell modules directory
# Default location: $env:PSModulePath (e.g., C:\Windows\System32\WindowsPowerShell\v1.0\Modules)
Copy-Item -Path .\PowerSploit -Destination "$env:ProgramFiles\WindowsPowerShell\Modules\" -Recurse

# Alternative: Load directly without installation
Import-Module .\PowerSploit\PowerSploit.psm1
```

For user-level installation (non-admin):

```powershell
# Copy to user modules path
Copy-Item -Path .\PowerSploit -Destination "$env:USERPROFILE\Documents\WindowsPowerShell\Modules\" -Recurse
```

## Basic Usage

```powershell
# Import the module
Import-Module PowerSploit

# List available commands
Get-Command -Module PowerSploit

# Example: Retrieve GPP passwords
Get-GPPPassword
```

### Common Options

PowerSploit functions have module-specific options; use `Get-Help <FunctionName> -Full` for details.

| Option | Description |
|--------|-------------|
| `-Verbose` | Enable verbose output for debugging |
| `-Debug` | Enable debug mode |
| `-Force` | Suppress prompts and force execution |

## Examples

### Example 1: Basic Usage (Reconnaissance)

```powershell
# Enumerate domain users with PowerView
Get-NetDomainController
```

### Example 2: Advanced Usage (Exfiltration)

```powershell
# Dump credentials using integrated Mimikatz
Invoke-Mimikatz -Command '"sekurlsa::logonpasswords"'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Boot or Logon Autostart Execution]] Boot or Logon Autostart Execution
- [[Credential Dumping]] OS Credential Dumping
- [[Windows Remote Management]] Windows Command Shell
- [[Windows Management Instrumentation]] Windows Management Instrumentation
- [[T1087.002]] Domain Account
- [[Hijack Execution Flow]] Hijack Execution Flow

### Tactics

- [[Execution]] Execution
- [[Persistence]] Persistence
- [[Discovery]] Discovery
- [[Lateral Movement]] Lateral Movement
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- PowerShell Script Block Logging capturing module imports or function calls.
- Event ID 400 (PowerShell engine start) with unusual module loads.
- File creation in modules directory or temporary execution of .ps1 files.
- Network connections from PowerShell processes (e.g., WMI or SMB).
- Antivirus signatures for known PowerSploit hashes or strings like "Invoke-Mimikatz".
- Process injection detections via ETW or Sysmon (Event ID 8).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Mimikatz]]
- [[tools/PowerView]]
- [[tools/Empire]]

## References

- Official GitHub Repository: https://github.com/PowerShellMafia/PowerSploit
- PowerShell Logging Documentation: https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging
- MITRE ATT&CK for PowerShell: https://attack.mitre.org/techniques/T1059/001/
