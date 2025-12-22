---
id: ffa2fe99-5228-47e7-b41e-2e0ed8486653
type: tool
verified: true
created_at: '2019-08-28T21:17:21.307722+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Windows
tags:
  - powershell
  - execution
  - evasion
  - dotnet
url: 'https://github.com/related-repo (inferred from technique)'
validated: true
---

# nps

**Status**: Unverified

## Overview

nps is a tool designed for executing PowerShell scripts without invoking the powershell.exe process, utilizing .NET runspaces to run code in memory. This approach is commonly used in red team operations to bypass endpoint detection and response (EDR) tools that flag traditional PowerShell executions.

## Description

The tool leverages the System.Management.Automation namespace to create isolated runspaces for PowerShell execution, avoiding disk writes and process creation signatures associated with powershell.exe. It is particularly useful in environments with strict PowerShell logging or constrained language mode enabled, allowing operators to perform tasks like reconnaissance, credential dumping, or lateral movement stealthily.

## Features

- Feature 1: In-memory execution of PowerShell code without spawning powershell.exe
- Feature 2: Support for inline scripts and file-based execution
- Feature 3: Minimal footprint with no external dependencies beyond .NET Framework

## Installation

### Requirements

- .NET Framework 4.5 or later
- Windows operating system (Server 2008 R2 or later)
- C# compiler (csc.exe) for building from source

### Install Commands

```cmd
# Download or create the C# source file (nps.cs)
# Compile using the C# compiler
csc /target:exe /reference:System.Management.Automation.dll /out:nps.exe nps.cs
```

Note: System.Management.Automation.dll must be available (typically from a PowerShell installation).

## Basic Usage

```cmd
nps.exe --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -e, --execute | Execute inline PowerShell code |
| -f, --file | Execute PowerShell code from a file |
| -v, --verbose | Enable verbose output for debugging |
| -h, --help | Show usage information |

## Examples

### Example 1: Basic Usage

```cmd
nps.exe -e "whoami"
```

### Example 2: Advanced Usage

```cmd
nps.exe -f "recon.ps1" -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for .NET processes loading System.Management.Automation.dll without powershell.exe in the process tree
- Detection method 2: Analyze command-line arguments for encoded PowerShell syntax in custom executables
- Detection method 3: Enable ETW logging for .NET runtime events to capture runspace creations

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

- Official documentation: Technique inspired by "PowerShell without PowerShell" methods (e.g., https://posts.specterops.io/oops-try-catch-finally-execution-anti-patterns-part-2-6e0d5e045ee1)
- Related resources: MITRE ATT&CK T1059.001
