---
type: tool
verified: true
created_at: '2019-08-28T21:17:40.530984Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - lolbas
  - living-off-the-land
  - post-exploitation
  - execution
  - persistence
url: 'https://lolbas-project.github.io/'
validated: true
---

# Living Off The Land Binaries Scripts and Libraries

**Status**: Unverified

## Overview

Living Off The Land Binaries and Scripts (LOLBAS) refers to the technique of using legitimate, built-in operating system binaries, scripts, and libraries for malicious purposes, such as execution, downloading payloads, or persistence. This tool documentation serves as a reference for identifying and misusing these native components in red teaming and security testing to evade detection by blending with normal system activity.

## Description

LOLBAS are pre-installed executables and scripts on Windows systems (e.g., certutil.exe, bitsadmin.exe, regsvr32.exe, mshta.exe) that can be abused beyond their intended functions. The LOLBAS project catalogs hundreds of such items, categorized by abuse potential. In offensive security, they enable attackers to perform reconnaissance, lateral movement, and command execution without introducing foreign tools, reducing forensic footprints. This reference helps security professionals understand attack vectors and build defenses like behavioral monitoring.

## Features

- **Comprehensive Catalog**: Lists binaries, scripts, and libraries with abuse examples.
- **Abuse Functions**: Covers execution, download, upload, and obfuscation capabilities.
- **Detection Guidance**: Includes signatures for EDR/SIEM rules.
- **Platform Focus**: Primarily Windows, with extensions to scripts (e.g., PowerShell) and libraries (e.g., DLL side-loading).

## Installation

### Requirements

- Windows OS (7 or later; most effective on Server 2016+).
- Administrative privileges for some abuses (user-level for many).
- No external dependencies; all components are native.

### Install Commands

LOLBAS are built-in; no installation required. To reference the full list:

```cmd
# Clone the LOLBAS project for local reference (optional)
git clone https://github.com/LOLBAS-Project/LOLBAS.git
```

On Kali or other pentest distros, install Git for cloning:

```bash
sudo apt update && sudo apt install git
```

## Basic Usage

```cmd
# View help for a specific binary (e.g., certutil)
certutil -?
```

Identify potential LOLBAS by checking system directories like %SystemRoot%\System32.

### Common Options

| Option | Description |
|--------|-------------|
| -? or /? | Display help for the binary |
| /s | Silent mode (common across tools) |
| -f | Force operation |

## Examples

### Example 1: Basic Usage

Review the LOLBAS project website for a full list, or query a specific entry:

```cmd
# Example: Check regsvr32 help
regsvr32 /?
```

### Example 2: Advanced Usage

Use in a script to enumerate potential LOLBAS:

```powershell
Get-ChildItem C:\Windows\System32 | Where-Object {$_.Name -match "certutil|bitsadmin|regsvr32|mshta"}
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Signed Binary Proxy Execution]] System Binary Proxy Execution
- [[Remote File Copy]] Ingress Tool Transfer
- [[Windows Command Shell]] Windows Command Shell

### Tactics

- [[Execution]] Execution
- [[Persistence]] Persistence
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor unusual command-line arguments for native binaries (e.g., certutil with -urlcache).
- Enable PowerShell logging and process auditing for child process creation from LOLBAS.
- Use Sysmon Event ID 1 (Process Creation) with filters for known LOLBAS paths and args.
- Behavioral analytics: Flag downloads or executions from system tools outside normal patterns.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Mimikatz]]
- [[powershell-empire]]

## References

- Official LOLBAS Project: https://lolbas-project.github.io/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1218/
- Related Resources: https://www.sans.org/reading-room/whitepapers/forensics/living-off-land-techniques-avoid-detection-38467
