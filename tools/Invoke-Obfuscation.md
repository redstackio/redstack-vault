---
id: 2defac2a-e757-4e92-83d4-99d8f28e070b
type: tool
verified: true
created_at: '2019-08-28T21:17:18.061613+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - obfuscation
  - powershell
  - evasion
  - red-team
url: 'https://github.com/danielbohannon/Invoke-Obfuscation'
validated: true
---

# Invoke-Obfuscation

**Status**: Unverified

## Overview

Invoke-Obfuscation is a PowerShell module designed for obfuscating PowerShell scripts and commands to evade antivirus detection, endpoint detection and response (EDR) systems, and other security controls during penetration testing and red team operations. It supports multiple obfuscation techniques including token manipulation, string encoding, and script block encoding, making it a key tool for command-and-control (C2) evasion and payload delivery.

## Description

This tool provides an interactive menu-driven interface or non-interactive commands for applying layered obfuscation to PowerShell code. Commonly used in post-exploitation scenarios to disguise malicious scripts, it helps attackers bypass signature-based detection by transforming readable code into functionally equivalent but obscured versions. It is particularly effective against PowerShell logging and monitoring tools like AMSI (Antimalware Scan Interface).

## Features

- Feature 1: Interactive obfuscation wizard for step-by-step technique selection
- Feature 2: Supports 14+ obfuscation methods including TOKEN, STRING, ENCODING, LAUNCHER, and LAUNCHER-AMSIBypass
- Feature 3: Non-interactive mode for scripting and automation
- Feature 4: Clipboard integration for quick obfuscation of copied code
- Feature 5: Multi-layer obfuscation stacking for increased evasion

## Installation

### Requirements

- PowerShell 2.0 or later (Windows environments)
- Internet access for downloading from GitHub
- Execution policy set to allow script execution (e.g., Bypass or Unrestricted)

### Install Commands

```powershell
# Download and execute directly (one-liner)
iwr -Uri 'https://raw.githubusercontent.com/danielbohannon/Invoke-Obfuscation/master/Invoke-Obfuscation.ps1' -UseBasicParsing | iex

# Or clone the repository for persistent use
cd $env:USERPROFILE\Documents
git clone https://github.com/danielbohannon/Invoke-Obfuscation.git
. .\Invoke-Obfuscation\Invoke-Obfuscation.ps1
```

## Basic Usage

```powershell
Invoke-Obfuscation
```

This launches the interactive menu. Select techniques like 'TOKEN' or 'STRING' to obfuscate input.

### Common Options

| Option | Description |
|--------|-------------|
| `-ScriptBlock` | Obfuscates a provided script block |
| `-ScriptPath` | Obfuscates a file at the specified path |
| `-Command` | Specifies the obfuscation technique path (e.g., 'TOKEN\ALL\1') |
| `-Quiet` | Suppresses menu output for scripting |
| `-Clipboard` | Obfuscates content from the clipboard |

## Examples

### Example 1: Basic Usage

```powershell
# Load the module first
download-and-execute-invoke-obfuscation

# Then obfuscate a simple command
Invoke-Obfuscation -ScriptBlock {Get-Process} -Command 'TOKEN\ALL\1' -Quiet
```

### Example 2: Advanced Usage

```powershell
# Obfuscate a file with string encoding
Invoke-Obfuscation -ScriptPath 'malicious.ps1' -Obfuscation 'String' -EncodingType 'Base64' -Quiet
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[PowerShell]] PowerShell

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: PowerShell script block logging showing downloads from GitHub raw URLs or obfuscated command patterns (e.g., unusual variable renaming like '$vAr1bLe')
- Detection method 2: AMSI scans flagging layered encodings or Invoke-Obfuscation imports
- Detection method 3: Network monitoring for connections to github.com/danielbohannon
- Detection method 4: Behavioral analysis of PowerShell processes spawning with high entropy strings

## Related Commands

- [[commands/download-and-execute-invoke-obfuscation]]
- [[commands/invoke-obfuscation-token-all]]
- [[commands/invoke-obfuscation-string-encode]]

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official GitHub Repository: https://github.com/danielbohannon/Invoke-Obfuscation
- Daniel Bohannon's Blog: https://danielbohannon.com
- PowerShell Obfuscation Deep Dive: Various SANS and Black Hat presentations
