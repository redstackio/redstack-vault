---
id: 728a8253-4649-49f5-a715-2b356edf5e80
type: tool
verified: true
created_at: '2019-08-28T21:17:27.307699+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Windows
tags:
  - Enumeration
  - Privilege Escalation
url: 'https://github.com/GhostPack/SharpUp'
description: >-
  A C# tool for enumerating common Windows privilege escalation vectors
  including vulnerable services, DLL hijacking opportunities, and registry
  settings.
tactics:
  - '[[Discovery]]'
techniques:
  - '[[System Information Discovery]]'
  - '[[Permission Groups Discovery]]'
  - '[[Abuse Elevation Control Mechanism]]'
validated: true
---

# SharpUp

**Status**: Unverified

## Overview

SharpUp is a C# tool designed for offensive security testing, providing enumeration of potential privilege escalation paths on Windows systems. It focuses on identifying misconfigurations and vulnerabilities that could allow an attacker to elevate privileges, such as unquoted service paths, always install elevated settings, and DLL hijacking opportunities. Commonly used during post-exploitation phases to assess lateral movement and persistence risks.

## Description

SharpUp is a port of popular PowerUp.ps1 functions into a standalone C# executable, implementing key checks without weaponization features to maintain a focus on detection and enumeration. It scans for common privesc vectors including vulnerable services, registry auto-elevations, weak service permissions, and more. The tool runs locally on the target Windows machine and outputs findings in a readable format, making it suitable for red team engagements and penetration testing.

## Features

- Service enumeration: Identifies services with unquoted paths, modifiable binaries, or weak permissions.
- DLL hijacking detection: Checks for hijackable DLL search order issues in services and startup programs.
- Registry checks: Scans for AlwaysInstallElevated, AlwaysMarkAsElevated, and other auto-elevation settings.
- Common paths: Examines well-known directories for writable executables that run with high privileges.
- No network dependencies: Runs entirely offline after execution.

## Installation

### Requirements

- Windows development environment with .NET Framework support (Visual Studio 2015-2019 recommended).
- For Linux/Ubuntu (cross-compilation): .NET SDK 6.0+ and Git.

### Install Commands

#### Windows (Build from Source)

1. Clone the repository:
```powershell
git clone https://github.com/GhostPack/SharpUp.git
cd SharpUp
```

2. Open SharpUp.sln in Visual Studio.

3. Set configuration to Release and rebuild the solution.

The executable will be in SharpUp/bin/Release/SharpUp.exe.

#### Ubuntu/Kali (Using .NET)
```bash
sudo apt update
sudo apt install -y dotnet-sdk-6.0 git
git clone https://github.com/GhostPack/SharpUp.git
cd SharpUp
dotnet build -c Release
```
The executable will be in bin/Release/net6.0/SharpUp.exe (may require mono to run on Linux for testing).

## Basic Usage

```powershell
& '$env:TEMP\SharpUp.exe'
```

### Common Options

| Option | Description |
|--------|-------------|
| No flags needed for basic scan | Performs all default enumerations |
| Run without output to file | Outputs to console by default |

## Examples

### Example 1: Basic Usage

Download and run SharpUp for a full privesc scan:
```powershell
# First download (see related command)
& '$env:TEMP\SharpUp.exe'
```

### Example 2: Advanced Usage

SharpUp does not have extensive flags; run directly for comprehensive output:
```powershell
& 'C:\Path\To\SharpUp.exe' > privesc_results.txt
```

## Detection

Indicators and methods for detecting this tool's usage:
- Execution of unsigned C# binaries in temp directories.
- PowerShell or process creation logs showing SharpUp.exe spawning.
- File creation events for SharpUp.exe downloads from GitHub.
- Console output or file writes containing privesc enumeration strings like 'Unquoted Service Path'.

## Related Commands

- [[commands/download-sharpup]]
- [[commands/run-sharpup-privesc-scan]]

## References

- Official GitHub Repository: https://github.com/GhostPack/SharpUp
- Related to GhostPack tools for .NET security testing.
