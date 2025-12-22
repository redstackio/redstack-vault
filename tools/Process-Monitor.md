---
id: tool-procmon
url: 'https://docs.microsoft.com/en-us/sysinternals/downloads/procmon'
tags:
  - monitoring
  - debugging
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.099Z'
validated: true
submitted: true
---
# Process-Monitor

**Status**: Unverified

## Overview

Process Monitor (ProcMon) is a Sysinternals tool for real-time monitoring of file system, registry, process, and thread activity on Windows, ideal for identifying failed DLL loads in applications like Burp Suite during vulnerability research.

## Description

ProcMon captures detailed events including path not found errors for DLLs, helping pinpoint hijackable locations. It's commonly used in offensive security to reverse-engineer load orders and in defensive ops for anomaly detection.

## Features

- Feature 1: Real-time event logging with filters for processes/DLLs
- Feature 2: Stack traces for load attempts
- Feature 3: Exportable logs for analysis

## Installation

### Requirements

- Windows 7+ (admin rights for full capture)

### Install Commands

```cmd
# Download from Microsoft Sysinternals
# No install; run Procmon.exe directly
```

## Basic Usage

```cmd
Procmon.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| /AcceptEula | Auto-accept EULA on first run |
| /BackingFile | Save to file |
| /Quiet | Minimize on start |

## Examples

### Example 1: Basic Usage

```cmd
Procmon.exe /AcceptEula
```

Filter for 'burp' process and 'NAME NOT FOUND' to see DLL attempts.

### Example 2: Advanced Usage

```cmd
Procmon.exe /BackingFile burp_loads.pml
```

Capture during Burp startup, then analyze for paths.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[DLL Search Order Hijacking]]
- [[Process Discovery]]

### Tactics

- [[Discovery]]
- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Procmon.exe process running
- High I/O from Sysinternals paths
- Log files like .pml in temp dirs

## Related Procedures


## Related Tools

- [[Related Tool: Sysmon]]
- [[Related Tool: API Monitor]]

## References

- Official documentation: https://docs.microsoft.com/en-us/sysinternals/downloads/procmon
- Related resources: Sysinternals Suite

