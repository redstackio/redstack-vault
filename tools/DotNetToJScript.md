---
id: 25f8b736-e836-4fb1-8577-e050c2ad2b91
name: DotNetToJScript
type: tool
verified: true
created_at: '2019-08-28T21:17:38.554912+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - bypass
  - execution
  - dotnet
  - jscript
url: 'https://github.com/tyranid/DotNetToJScript'
validated: true
---

# DotNetToJScript

**Status**: Unverified

## Overview

DotNetToJScript is a utility for generating JScript code that loads and executes .NET v2 (and compatible) assemblies directly from memory. It is commonly used in offensive security to deliver and run .NET-based payloads without writing files to disk, helping to evade antivirus and EDR detection during red team engagements.

## Description

The tool takes a compiled .NET assembly (DLL or EXE) and converts it into a self-contained JScript file that can be executed via Windows Script Host (cscript/wscript). This approach leverages JScript's ability to interface with .NET runtime, allowing in-memory loading to avoid filesystem artifacts. It supports specifying entry points and custom templates for further obfuscation. Ideal for scenarios involving command-and-control, payload delivery, or executing custom .NET tools in memory on Windows targets.

## Features

- Feature 1: In-memory .NET assembly loading to avoid disk writes
- Feature 2: Support for specifying entry points for targeted execution
- Feature 3: Custom JScript template integration for evasion
- Feature 4: Compatible with .NET Framework v2.0 and higher (via compatibility modes)

## Installation

### Requirements

- .NET Framework 4.0 or later (for the tool itself)
- Windows environment (tool is Windows-specific)
- Access to a compiled .NET assembly

### Install Commands

```powershell
# Download from GitHub releases
Invoke-WebRequest -Uri "https://github.com/tyranid/DotNetToJScript/releases/download/v1.0/DotNetToJScript.exe" -OutFile "DotNetToJScript.exe"

# Or clone and build from source (requires Visual Studio)
git clone https://github.com/tyranid/DotNetToJScript.git
cd DotNetToJScript
msbuild DotNetToJScript.csproj
```

For Kali Linux or cross-compilation, use Wine or a Windows VM, as the tool is native to Windows.

## Basic Usage

```powershell
DotNetToJScript.exe --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -f, --file | Input .NET assembly path |
| -o, --output | Output JScript file path |
| -e, --entrypoint | Entry point to invoke |
| --template | Path to custom JScript template |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Generate a simple JScript loader from an assembly:

```powershell
DotNetToJScript.exe -f C:\payloads\MyPayload.dll -o memory_loader.js
```

Execute the generated JScript:

```powershell
cscript memory_loader.js
```

### Example 2: Advanced Usage

Generate with a specific entry point:

```powershell
DotNetToJScript.exe -f C:\payloads\MyPayload.dll -e MyPayload.Program.Run -o advanced_loader.js
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Regsvr32]] Exploited Third-party Software
- [[Hijack Execution Flow]] Hijack Execution Flow

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for cscript/wscript executions spawning .NET processes
- Detection method 2: Analyze JScript files for base64-encoded .NET assembly data
- Detection method 3: EDR rules for in-memory .NET loading via scripting hosts
- Detection method 4: Fileless execution patterns in process trees (wscript -> mscoree.dll)

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
- [[tools/Cobalt-Strike]]

## References

- Official GitHub: https://github.com/tyranid/DotNetToJScript
- James Forshaw's Blog: https://tyranidslair.blogspot.com/2017/12/bypassing-amsi-and-etw-in-net-with.html
- Related Resource: https://www.blackhat.com/docs/us-18/thu-aug-09/Bypassing-User-Mode-Hooks-and-Direct-Invocation-of-System-Calls-for-Red-Teams.pdf
