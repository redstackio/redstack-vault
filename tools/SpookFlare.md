---
id: 9def6601-9a6d-4733-802a-b0cc6fe5c16b
name: SpookFlare
type: tool
verified: true
created_at: '2019-08-28T21:17:22.159674+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - evasion
  - obfuscation
  - powershell
  - bypass
  - edr
url: 'https://github.com/BloodHoundAD/SpookFlare'
validated: true
---

# SpookFlare

**Status**: Unverified

## Overview

SpookFlare is a PowerShell-based evasion framework designed to bypass endpoint detection and response (EDR) solutions, antivirus software, and other security measures. It provides modules for obfuscating PowerShell code, performing process injection, and executing payloads in ways that avoid common detection signatures, making it useful for red team operations and penetration testing where stealth is required.

## Description

SpookFlare offers a collection of scripts and functions that implement advanced evasion techniques, such as string obfuscation, AMSI (Antimalware Scan Interface) bypasses, ETW (Event Tracing for Windows) patching, and DLL/process injection. It differs from traditional tools by focusing on client-side and network-side evasion, allowing attackers to deliver and execute payloads without alerting defenders. Commonly used in post-exploitation to maintain persistence or escalate privileges while minimizing detection.

## Features

- **Obfuscation Modules**: Techniques to encode and scramble PowerShell scripts to evade static analysis.
- **Injection Capabilities**: Methods for DLL injection, process hollowing, and reflective loading to run code in memory.
- **Bypass Functions**: Patches for AMSI, ETW, and other Windows security features.
- **Payload Execution**: Supports encoded command execution and alternative invocation methods.
- **Modular Design**: Easy to load and extend with custom evasion scripts.

## Installation

### Requirements

- PowerShell 3.0 or higher on Windows.
- Administrative privileges for some injection features.
- Git for cloning the repository.

### Install Commands

```powershell
# Clone the repository
Invoke-WebRequest -Uri https://github.com/BloodHoundAD/SpookFlare/archive/master.zip -OutFile SpookFlare.zip
Expand-Archive SpookFlare.zip -DestinationPath .\
# Or using Git
# git clone https://github.com/BloodHoundAD/SpookFlare.git
```

On Kali Linux (for cross-compilation or testing):

```bash
sudo apt update && sudo apt install -y powershell
# Then clone and run via pwsh
pwsh -File .\SpookFlare.ps1
```

## Basic Usage

```powershell
tool-name --help
# SpookFlare doesn't have a CLI; load via dot-sourcing
. .\SpookFlare.ps1
Get-Help Get-ObfuscatedString
```

### Common Options

| Option | Description |
|--------|-------------|
| `-ScriptBlock` | Specifies the PowerShell block to process (e.g., for obfuscation) |
| `-OutputFormat` | Defines output type, like EncodedCommand or ObfuscatedString |
| `-ProcessID` | Target process ID for injection functions |
| `-Verbose` | Enables detailed logging for troubleshooting |

## Examples

### Example 1: Basic Usage

```powershell
# Load framework
. .\SpookFlare.ps1
# Obfuscate a simple command
Get-ObfuscatedString -ScriptBlock { Write-Host 'Evasion Test' } -OutputFormat EncodedCommand
```

### Example 2: Advanced Usage

```powershell
# Bypass AMSI and inject DLL
. .\SpookFlare.ps1
Disable-AMSI; Invoke-DllInjection -ProcessID 1234 -DllPath 'C:\temp\payload.dll'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[Process Injection]] Process Injection
- [[Impair Defenses]] Impair Defenses

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- PowerShell execution logs showing dot-sourcing of suspicious .ps1 files.
- Anomalous encoded commands in process arguments (e.g., base64 strings).
- Behavioral alerts for process injection or AMSI/ETW tampering.
- File creation in temp directories with SpookFlare artifacts.

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

## References

- Official GitHub: https://github.com/BloodHoundAD/SpookFlare
- Blog post on usage: https://example.com/spookflare-guide

*Last updated: 2023-10-01T00:00:00.000000+00:00*
