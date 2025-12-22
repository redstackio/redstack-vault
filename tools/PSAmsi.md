---
id: ee73709a-60e2-45e4-ac69-24254860f814
type: tool
verified: true
created_at: '2019-08-28T21:17:28.953349Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - defense-evasion
  - amsi
  - powershell
  - bypass
url: 'https://github.com/matthewdunwoody/PSAmsi'
validated: true
---

# PSAmsi

**Status**: Unverified

## Overview

PSAmsi is a PowerShell module for auditing, testing, and bypassing AMSI (Antimalware Scan Interface) signatures on Windows systems. It is commonly used in red team operations to evaluate endpoint detection capabilities and evade script-based defenses during post-exploitation.

## Description

The module provides functions to inspect AMSI providers, test bypass techniques, and apply patches to disable AMSI scanning for PowerShell scripts. It targets Windows 10 and Server editions with PowerShell 5+. PSAmsi is particularly useful for understanding how antivirus solutions like Windows Defender interact with script execution and for developing custom evasion methods.

## Features

- Feature 1: Audit AMSI providers and signatures to identify detection patterns.
- Feature 2: Test non-persistent and persistent AMSI bypass methods.
- Feature 3: Combine AMSI evasion with ETW (Event Tracing for Windows) disabling to reduce logging.

## Installation

### Requirements

- PowerShell 5.0 or later
- Windows 10/Server 2016 or newer
- Administrative privileges for some bypass functions

### Install Commands

```powershell
# Download from GitHub
Invoke-WebRequest -Uri 'https://github.com/matthewdunwoody/PSAmsi/archive/master.zip' -OutFile 'PSAmsi.zip'
Expand-Archive -Path 'PSAmsi.zip' -DestinationPath 'C:\Tools\'

# Or clone the repo if Git is available
git clone https://github.com/matthewdunwoody/PSAmsi.git C:\Tools\PSAmsi
```

## Basic Usage

```powershell
Import-Module C:\Tools\PSAmsi\PSAmsi.ps1
Get-Help Bypass-AMSIAndETW
```

### Common Options

| Option | Description |
|--------|-------------|
| `-Verbose` | Enable detailed output for debugging |
| `-Persist` | Apply persistent changes across sessions (requires admin) |
| `-Force` | Overwrite existing module if loaded |

## Examples

### Example 1: Basic Usage

```powershell
Import-Module .\PSAmsi.ps1
Test-BypassAMSIAndETW
```

### Example 2: Advanced Usage

```powershell
Import-Module .\PSAmsi.ps1
Bypass-AMSIAndETW -Persist
# Now run evasive scripts
Invoke-Expression 'malicious payload'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools
- [[PowerShell]] Command and Scripting Interpreter: PowerShell

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: PowerShell module loading events in ETW logs (before bypass).
- Detection method 2: Modifications to amsi.dll or registry keys related to AMSI.
- Detection method 3: Suspicious Import-Module calls to unsigned scripts.

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
- [[tools/Invoke-Obfuscation]]

## References

- Official GitHub: https://github.com/matthewdunwoody/PSAmsi
- AMSI Bypass Techniques: https://posts.specterops.io/bypassing-amsi-in-memory-6044d4bc9c73
