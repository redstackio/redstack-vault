---
id: 4bd2652d-7810-4375-979c-212d8283c95c
type: tool
verified: true
created_at: '2019-08-28T21:17:24.404064+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
description: >-
  A PowerShell framework and collection of scripts for offensive security,
  penetration testing, and red teaming across all phases of an engagement.
url: 'https://github.com/samratashok/nishang'
platforms:
  - Windows
tags:
  - powershell
  - offensive-security
  - red-team
  - post-exploitation
  - execution
  - persistence
commands:
  - '[[commands/nishang-import-module]]'
  - '[[commands/nishang-invoke-powershell-tcp-reverse-shell]]'
  - '[[commands/nishang-get-net-user]]'
validated: true
---

# Nishang

**Status**: Unverified

## Overview

Nishang is a comprehensive PowerShell framework consisting of scripts and payloads tailored for offensive security operations, including penetration testing and red teaming. It facilitates the use of PowerShell for tasks ranging from initial access and execution to lateral movement, privilege escalation, and data exfiltration, making it versatile across all phases of an attack lifecycle.

## Description

Nishang provides a modular structure with over 100 scripts that leverage PowerShell's native capabilities to evade detection while performing advanced post-exploitation activities. It includes utilities for network reconnaissance, credential access, and command-and-control (C2) communications. The framework is particularly effective in Windows environments where PowerShell is ubiquitous, allowing attackers to blend in with legitimate administrative activities. Common use cases include generating reverse shells, keylogging, and enumerating domain users without relying on external binaries.

## Features

- **Reverse and Bind Shells**: TCP, HTTP/S-based shells for C2 communication.
- **Reconnaissance Scripts**: Tools for user enumeration, process listing, and network discovery.
- **Post-Exploitation Utilities**: Keyloggers, screenshot capture, and privilege escalation helpers.
- **Evasion Techniques**: Obfuscated payloads and AMSI bypass methods.
- **Integration Support**: Compatible with tools like Mimikatz for credential dumping.

## Installation

### Requirements

- PowerShell version 2.0 or higher (tested up to PowerShell 5.1 and PowerShell Core).
- Git for cloning the repository.
- Windows operating system (Server 2008+ or Windows 7+).
- Execution policy set to allow script execution (e.g., Bypass).

### Install Commands

```powershell
# Clone the repository
Invoke-WebRequest -Uri https://github.com/samratashok/nishang/archive/master.zip -OutFile nishang.zip
Expand-Archive nishang.zip -DestinationPath .

# Or using Git
# git clone https://github.com/samratashok/nishang.git

# Navigate to the directory
Set-Location nishang-master

# Import as a module (optional for easier access to functions)
Import-Module .\nishang.psm1
```

## Basic Usage

```powershell
# Import the module
Import-Module .\nishang.psm1

# View available functions
Get-Command -Module nishang

# Get help for a specific function
Get-Help Invoke-PowerShellTcp -Full
```

### Common Options

| Option | Description |
|--------|-------------|
| `-Verbose` | Enable verbose output for debugging. |
| `-Debug` | Provide detailed debug information. |
| `-WhatIf` | Simulate the action without executing. |

## Examples

### Example 1: Basic Usage

Import the module and list available commands:

```powershell
Import-Module .\nishang.psm1
Get-Command -Module nishang | Select-Object Name
```

### Example 2: Advanced Usage

Use a specific script for user enumeration (see related command for details):

```powershell
Import-Module .\nishang.psm1
Get-NetUser -Domain example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Web Protocols]] Web Protocols
- [[Windows Remote Management]] Windows Command Shell
- [[Bypass User Account Control]] Bypass User Account Control

### Tactics

- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement
- [[Persistence]] Persistence
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Enable PowerShell Script Block Logging and Module Logging to capture imported modules and executed functions.
- Monitor for unusual PowerShell processes spawning network connections (e.g., to attacker IPs on non-standard ports).
- Look for AMSI bypass attempts or execution policy changes via Event ID 4104 in Windows Event Logs.
- Network traffic analysis for HTTP/S beacons or TCP connections from PowerShell.exe.
- File system monitoring for Nishang script downloads or executions in temporary directories.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit]] (for integrating Nishang payloads into exploits)
- [[tools/Empire]] (alternative PowerShell-based C2 framework)
- [[tools/Covenant]] (GRPC-based .NET C2 with PowerShell support)

## References

- Official GitHub Repository: https://github.com/samratashok/nishang
- PowerShell Offensive Security Blog: https://powershell.org
- MITRE ATT&CK for Enterprise: https://attack.mitre.org/techniques/T1059/001/
