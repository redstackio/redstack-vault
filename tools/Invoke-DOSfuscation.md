---
id: c85ce483-24a4-4e5b-94d7-6b5740e2531e
type: tool
verified: true
created_at: '2019-08-28T21:17:40.441611Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - obfuscation
  - cmd
  - evasion
  - powershell
  - defense-evasion
url: 'https://github.com/mdsolabs/Invoke-DOSfuscation'
validated: true
---

# Invoke-DOSfuscation

**Status**: Unverified

## Overview

Invoke-DOSfuscation is a PowerShell-based tool designed as a cmd.exe command obfuscation generator and detection test harness. It is commonly used in red team operations to create obfuscated versions of Windows command-line instructions that evade antivirus, EDR, and other security controls. The tool supports multiple obfuscation techniques and includes a testing framework to evaluate evasion success against various detection engines.

## Description

This tool generates obfuscated cmd.exe commands using methods like variable substitution, for loops, environment variables, and more, making it harder for signature-based defenses to detect malicious activity. It is particularly useful for post-exploitation scenarios where direct command execution might be blocked. The detection test harness allows simulating execution against tools like Windows Defender or Sysmon to measure evasion rates. Developed by MDSec, it runs entirely in PowerShell without requiring additional dependencies beyond standard Windows features.

## Features

- **Multiple Obfuscation Methods**: Supports Basic, Environment, ForLoop, PowerShell, and others for diverse evasion strategies.
- **Test Harness**: Built-in testing against detection tools to validate obfuscation effectiveness.
- **Batch Generation**: Produce all method variations for a single command and output to files.
- **No External Dependencies**: Pure PowerShell implementation for easy deployment in restricted environments.
- **Customizable**: Allows specification of commands, methods, and output formats.

## Installation

### Requirements

- PowerShell 3.0 or later (standard on Windows 7+).
- Administrative privileges not required for basic use, but may be needed for testing against system defenses.
- Internet access for initial download (optional if transferred manually).

### Install Commands

```powershell
# Download from GitHub
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mdsolabs/Invoke-DOSfuscation/master/Invoke-DOSfuscation.ps1" -OutFile "Invoke-DOSfuscation.ps1"

# Or clone the repository
git clone https://github.com/mdsolabs/Invoke-DOSfuscation.git
cd Invoke-DOSfuscation
Import-Module ./Invoke-DOSfuscation.ps1
```

For air-gapped environments, transfer the .ps1 file manually.

## Basic Usage

```powershell
Get-Help Invoke-DOSfuscation
```

### Common Options

| Option | Description |
|--------|-------------|
| `-Command` | The cmd.exe command to obfuscate |
| `-Method` | Specific obfuscation technique (e.g., Basic) |
| `-AllMethods` | Generate using all available methods |
| `-Test` | Run detection test harness |
| `-OutputFile` | Save results to a file |
| `-h, --help` | Show detailed help |

## Examples

### Example 1: Basic Usage

```powershell
Invoke-DOSfuscation -Command "whoami" -Method Basic
```

See [[commands/invoke-dosfuscation-obfuscate-basic-command]] for details.

### Example 2: Advanced Usage

```powershell
Invoke-DOSfuscation -Command "net user" -Test -DetectionTool WindowsDefender
```

See [[commands/invoke-dosfuscation-test-detection]] for details.

### Example 3: Batch Generation

```powershell
Invoke-DOSfuscation -Command "ipconfig" -AllMethods -OutputFile results.txt
```

See [[commands/invoke-dosfuscation-generate-all-methods]] for details.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[Process Injection]] Process Injection (when used in conjunction with other tools)

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- PowerShell execution logs showing Invoke-DOSfuscation imports or runs.
- Unusual cmd.exe subprocesses with obfuscated arguments (e.g., for loops echoing commands).
- Network downloads from GitHub repositories matching the tool's URL.
- EDR alerts on PowerShell script block logging for obfuscation patterns.

## Related Procedures

- [[procedures/Obfuscate-CMD-Commands-for-Evasion]]
- [[procedures/Test-Command-Detection-Evasion]]

## Related Tools

- [[tools/PowerSploit]] (for broader PowerShell attack frameworks)
- [[tools/Empire]] (for command and control with obfuscation)

## References

- Official GitHub: https://github.com/mdsolabs/Invoke-DOSfuscation
- MDSec Blog: https://www.mdsec.co.uk/category/activebreach/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1027/
