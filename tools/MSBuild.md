---
type: tool
verified: true
platforms:
  - Windows
tags:
  - applocker
  - Build
  - Defense Bypass
url: 'https://dotnet.microsoft.com/download/dotnet-framework'
commands:
  - '[[commands/msbuild-execute-xml-payload]]'
validated: true
---

# MSBuild

**Status**: ✓ Verified

## Overview

MSBuild (Microsoft Build Engine) is a platform for building applications. It uses an XML schema to control how the platform processes and builds software (similar to Linux's make). MSBuild is a standalone program that can be used to execute commands and bypass AppLocker restrictions when AppLocker is configured to only run signed binaries, as it is a Microsoft-signed binary.

## Description

MSBuild is often installed alongside .NET Framework and does not require Visual Studio to function. It processes XML project files that can include inline tasks or references to assemblies, allowing for the execution of arbitrary code during the build process. This makes it valuable in red team operations for defense evasion and proxy execution of payloads without triggering application whitelisting controls.

## Features

- XML-based project file processing for build automation
- Support for inline C# code execution via custom tasks
- Integration with .NET assemblies for extended functionality
- Microsoft-signed executable, enabling bypass of strict application controls
- Verbose logging and diagnostic output for troubleshooting builds

## Installation

### Requirements

- Windows operating system (typically included with .NET installations)
- Administrative privileges for system-wide installation if not present

### Install Commands

MSBuild is installed via .NET Framework, Visual Studio, or Build Tools:

- Download and install .NET Framework from [https://dotnet.microsoft.com/download/dotnet-framework](https://dotnet.microsoft.com/download/dotnet-framework)
- Install Visual Studio Community from [https://visualstudio.microsoft.com/vs/community/](https://visualstudio.microsoft.com/vs/community/)
- Download Build Tools for Visual Studio from [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)

On modern Windows, it may be available via winget:

```cmd
winget install Microsoft.VisualStudio.2022.BuildTools
```

## Basic Usage

```cmd
MSBuild.exe /help
```

### Common Options

| Option | Description |
|--------|-------------|
| `/help` or `/?` | Show help message and available options |
| `/v:n` | Set verbosity level (n: quiet, m: minimal, n: normal, d: detailed, diag: diagnostic) |
| `/t:Build` | Specify the target to build (default is Build) |
| `/p:Configuration=Release` | Set project properties like configuration |

## Examples

### Example 1: Basic Usage

Build a simple XML project file:

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe project.xml
```

### Example 2: Advanced Usage

Build with detailed verbosity and custom properties:

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe /v:d /p:Configuration=Debug project.xml
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Signed Binary Proxy Execution]] Signed Binary Proxy Execution

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor process creation events for MSBuild.exe spawning child processes like cmd.exe or powershell.exe
- Analyze command-line arguments for references to unusual or user-created XML files in temporary directories
- Enable ETW logging for .NET runtime to capture inline code execution
- Look for MSBuild.exe executions outside of standard development paths or during non-build times

## Related Procedures

- [[procedures/Windows-AppLocker-Whitelist-Bypass-Using-MSBuild]]

## Related Tools

- [[tools/nps-payload]]

## References

- Official .NET Framework downloads: [https://dotnet.microsoft.com/download/dotnet-framework](https://dotnet.microsoft.com/download/dotnet-framework)
- Visual Studio Community: [https://visualstudio.microsoft.com/vs/community/](https://visualstudio.microsoft.com/vs/community/)
- Build Tools: [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/)
- MITRE ATT&CK: [T1218 Signed Binary Proxy Execution](https://attack.mitre.org/techniques/T1218/)
