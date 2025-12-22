---
id: a46c0354-0b81-469b-b4e7-044f2f3b6e24
type: tool
verified: true
created_at: '2019-08-28T21:17:22.104522Z'
updated_at: '2024-09-01T00:00:00Z'
platforms:
  - Windows
tags:
  - powershell
  - evasion
  - execution
  - dotnet
url: ''
validated: true
---

# UnmanagedPowerShell

**Status**: Unverified

## Overview

UnmanagedPowerShell is a technique and associated tooling for executing PowerShell scripts and commands from unmanaged .NET processes. By creating a custom PowerShell runspace in C# code, it avoids launching the detectable powershell.exe process, making it suitable for stealthy command execution in red team operations and post-exploitation scenarios.

## Description

This approach leverages the System.Management.Automation assembly to host PowerShell functionality within a standard .NET console application. It enables full access to PowerShell cmdlets, modules, and scripting capabilities while minimizing forensic footprints. Commonly used to bypass application whitelisting, process monitoring, and PowerShell-specific logging controls.

## Features

- In-memory PowerShell runspace creation without powershell.exe
- Support for arbitrary PowerShell commands via command-line arguments
- Error handling and output capture from PowerShell execution
- Integration with custom .NET applications for advanced payloads

## Installation

### Requirements

- Windows OS with .NET Framework 4.0+ installed
- Access to the Visual C# Compiler (csc.exe), typically in %WINDIR%\Microsoft.NET\Framework\v4.0.30319\
- System.Management.Automation.dll (included in Windows PowerShell 3.0+ or downloadable for older versions)

### Install Commands

1. Save the C# source code (see [[codes/csharp-unmanaged-powershell-runspace]]) to a file named UnmanagedPowerShell.cs.
2. Compile using the provided command.

```cmd
[[commands/csc-compile-unmanaged-powershell]]
```

## Basic Usage

```cmd
UnmanagedPowerShell.exe --help
```

(Note: The basic executable does not have a --help flag; pass a simple command like "Get-Host" to test.)

### Common Options

| Option | Description |
|--------|-------------|
| (Command-line arg) | PowerShell script/command to execute | 

## Examples

### Example 1: Basic Usage

Compile first, then execute a simple reconnaissance command:

```cmd
[[commands/csc-compile-unmanaged-powershell]]
UnmanagedPowerShell.exe "whoami"
```

### Example 2: Advanced Usage

Execute a more complex script for lateral movement:

```cmd
UnmanagedPowerShell.exe "Invoke-Command -ComputerName RemoteHost -ScriptBlock { Get-Service } -Credential (Get-Credential)"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[T1027.010]] Command Obfuscation (via in-memory execution)

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Process creation of csc.exe with references to System.Management.Automation.dll
- Non-PowerShell processes (e.g., custom EXEs) loading PowerShell assemblies (ETW tracing or Sysmon)
- Console output containing PowerShell cmdlet results from unexpected processes
- AMSI scans on compiled binaries or runtime .NET code

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[PowerShell]]
- [[C-Sharp-Compiler]]

## References

- Microsoft Documentation: System.Management.Automation.Runspaces
- LOLBAS Project: PowerShell Evasion Techniques
