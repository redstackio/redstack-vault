---
id: procmon-sysinternals
url: 'https://docs.microsoft.com/en-us/sysinternals/downloads/procmon'
tags:
  - monitoring
  - debugging
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.840Z'
validated: true
submitted: true
---
# ProcMon

**Status**: Unverified

## Overview

Process Monitor (ProcMon) is a Sysinternals tool for real-time monitoring of file system, registry, process/thread, and network activity on Windows systems. In security testing, it's commonly used to debug application behavior, such as observing DLL search paths during execution to identify hijacking opportunities.

## Description

ProcMon provides advanced filtering and logging to capture detailed events, making it essential for reverse engineering vulnerabilities like DLL search-order issues. It logs operations like CreateFile for DLL loads, allowing attackers to pinpoint exploitable paths without code access.

## Features

- Feature 1: Real-time event capture with filters for processes, operations, and paths
- Feature 2: Boot logging for persistent monitoring
- Feature 3: Exportable logs (CSV, XML) for analysis

## Installation

### Requirements

- Windows 7 or later
- Administrative privileges for full access

### Install Commands

No installation needed; download and run the EXE from Sysinternals.

```powershell
# Download via PowerShell
Invoke-WebRequest -Uri "https://download.sysinternals.com/files/ProcMon.zip" -OutFile "ProcMon.zip"
Expand-Archive ProcMon.zip -DestinationPath "C:\Tools\"
```

## Basic Usage

```cmd
ProcMon.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| `/AcceptEula` | Auto-accepts EULA on first run |
| `/BackingFile file.pml` | Saves log to file |
| `/Filter filter` | Applies filter on startup |

## Examples

### Example 1: Basic Usage

```cmd
ProcMon.exe /AcceptEula
```

Filter for a process: Capture > Filter > Process Name is systeminfo.exe > Include.

### Example 2: Advanced Usage

```cmd
ProcMon.exe /BackingFile dll_log.pml /Filter "Path contains snapapi.dll"
```

Monitor specific DLL searches during execution.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[DLL Search Order Hijacking]]

### Tactics

- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- ProcMon.exe process running with filters on sensitive paths
- Log files (.pml) in temp directories
- Sysinternals suite downloads in browser history

## Related Procedures

- [[procedures/Install-and-Monitor-Acronis-Agent-with-ProcMon]]
- [[procedures/Trigger-DLL-Hijacking-for-Escalation]]

## Related Tools

- [[Related Tool: Process Explorer]]
- [[Related Tool: Wireshark]]

## References

- Official documentation: https://docs.microsoft.com/en-us/sysinternals/downloads/procmon
- Sysinternals Suite overview
