---
id: 7c88ca2e-eced-4567-bdf9-31e7291b647a
name: PowerShdll
type: tool
verified: true
created_at: '2019-08-28T21:17:26.555623+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - execution
  - bypass
  - powershell
  - dll
url: 'https://github.com/related-repo/powershdll (assumed; verify official source)'
validated: true
---

# PowerShdll

**Status**: Unverified

## Overview

PowerShdll is a dynamic link library (DLL) designed to execute PowerShell code through the Windows rundll32.exe utility. It is commonly used in offensive security operations to bypass application whitelisting, software restrictions, or endpoint detection rules that block direct invocation of powershell.exe. By leveraging the trusted rundll32.exe process, attackers can run PowerShell scripts or commands covertly.

## Description

PowerShdll works by exporting an entry point (typically DllMain) that interprets and executes provided PowerShell code when loaded via rundll32.exe. This technique evades many security controls since rundll32.exe is a signed Microsoft binary and often allowed by default. It is particularly useful in environments with strict PowerShell logging or execution policies, enabling post-exploitation activities like reconnaissance, lateral movement, or payload deployment without triggering alerts on powershell.exe.

## Features

- Feature 1: Direct PowerShell command execution via DLL loading
- Feature 2: Script loading and invocation support for complex operations
- Feature 3: Minimal footprint, as it uses native Windows components
- Feature 4: Configurable entry points for custom PowerShell integration

## Installation

### Requirements

- Windows OS (7 or later)
- Administrative privileges for DLL placement (optional, depending on policy)
- PowerShell 2.0 or higher installed (standard on Windows)

### Install Commands

```cmd
# Download the DLL (replace with actual download source)
powerShell -Command "Invoke-WebRequest -Uri 'https://example.com/PowerShdll.dll' -OutFile 'PowerShdll.dll'"

# Or copy to a working directory
copy PowerShdll.dll C:\temp\
```

For compilation from source (if available):

```cmd
# Assume Visual Studio or MinGW setup
cl /LD powershdll.c /link ole32.lib
```

## Basic Usage

```cmd
rundll32.exe PowerShdll.dll,DllMain "Get-Date"
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | N/A (DLL-based; use documentation for syntax) |
| Entry Point (e.g., DllMain) | Specifies the DLL function to invoke |
| Command String | PowerShell code passed as argument |

## Examples

### Example 1: Basic Usage

Execute a simple command to retrieve system info:

```cmd
rundll32.exe PowerShdll.dll,DllMain "whoami /all"
```

### Example 2: Advanced Usage

Load and run a script for network reconnaissance:

```cmd
rundll32.exe PowerShdll.dll,DllMain "& { . 'C:\temp\netscan.ps1'; Invoke-NetScan }"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Rundll32]] Signed Binary Proxy Execution: Rundll32

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor rundll32.exe spawning PowerShell processes or unusual DLL loads via Sysmon Event ID 7 (ImageLoad)
- Detection method 2: Enable PowerShell Script Block Logging to capture executed code
- Detection method 3: Alert on rundll32.exe with non-standard DLL arguments or network callbacks
- Detection method 4: File integrity monitoring for unexpected DLL files like PowerShdll.dll

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Powershell]]
- [[tools/Rundll32]]
- [[tools/Cobalt-Strike]] (for similar beacon execution)

## References

- Official documentation: Search for "PowerShdll GitHub" or related PoC repositories
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1059/001/
- Related resources: Windows Internals documentation on DLL loading
