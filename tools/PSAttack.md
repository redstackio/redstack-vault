---
id: c94289a8-a550-4fb5-9d40-9d689d1a83ec
type: tool
verified: true
created_at: '2019-08-28T21:17:30.247183+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - powershell
  - post-exploitation
  - framework
url: 'https://github.com/PSAttack/PSAttack'
validated: true
---

# PSAttack

**Status**: Unverified

## Overview

PSAttack is a self-contained custom PowerShell console that combines leading infosec PowerShell projects, such as PowerSploit, Empire, and other offensive security modules, into a unified environment for red teaming and penetration testing.

## Description

PSAttack provides an integrated console for executing post-exploitation tasks, payload generation, enumeration, and lateral movement without needing to manage multiple separate tools. It loads modules dynamically and offers a menu-driven interface for common attack workflows, making it suitable for Windows environments in offensive security operations.

## Features

- Feature 1: Integrated module loading for PowerSploit, Atomic Red Team, and custom scripts
- Feature 2: Built-in payload generation for reverse shells, Meterpreter, and obfuscated code
- Feature 3: Enumeration capabilities for system, network, and credential discovery
- Feature 4: Stealth options to minimize logging and detection
- Feature 5: Extensible scripting support for custom attack chains

## Installation

### Requirements

- PowerShell 3.0 or higher
- Execution Policy set to Unrestricted or Bypass (for testing environments)
- Windows OS (Server 2008+ or client equivalents)

### Install Commands

```powershell
# Download from repository
Invoke-WebRequest -Uri "https://github.com/PSAttack/PSAttack/archive/main.zip" -OutFile "PSAttack.zip"
Expand-Archive -Path "PSAttack.zip" -DestinationPath "C:\Tools\"

# Or clone if Git is available
git clone https://github.com/PSAttack/PSAttack.git C:\Tools\PSAttack

# Import the module
Import-Module C:\Tools\PSAttack\PSAttack.ps1
```

## Basic Usage

```powershell
tool-name --help
```

Start the console:

```powershell
Import-Module PSAttack.ps1; Start-PSAttackConsole
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Verbose output for debugging |
| -s, --stealth | Enable stealth mode |

## Examples

### Example 1: Basic Usage

```powershell
Start-PSAttackConsole
```

This launches the interactive console where you can run commands like `Invoke-PSAttackPayload`.

### Example 2: Advanced Usage

```powershell
Import-Module PSAttack.ps1; Invoke-PSAttackEnum -Type SystemInfo -OutputPath C:\temp\enum.txt
```

Performs enumeration directly without entering the console.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[DLL Side-Loading]] Scheduled Task/Job
- [[Boot or Logon Autostart Execution]] Boot or Logon Autostart Execution

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: PowerShell ScriptBlock logging showing PSAttack module imports
- Detection method 2: Unusual PowerShell processes spawning child processes or network connections
- Detection method 3: File creation of PSAttack.ps1 or related modules in temp directories
- Detection method 4: AMSI scans for obfuscated PowerShell code

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PowerSploit]]
- [[tools/Empire]]
- [[tools/Cobalt Strike]]

## References

- Official GitHub Repository: https://github.com/PSAttack/PSAttack
- PowerShell Offensive Security Documentation

*Last updated: 2023-10-01T00:00:00Z*
