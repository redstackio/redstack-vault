---
type: tool
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - memory
url: 'https://learn.microsoft.com/en-us/sysinternals/downloads/procdump'
commands:
  - '[[commands/procdump-full-memory-dump]]'
validated: true
---

# ProcDump

**Status**: ✓ Verified

## Overview

ProcDump is a command-line utility from Microsoft Sysinternals designed for monitoring application performance and generating crash dumps. In security testing and red team operations, it is used to create memory dumps of running processes, which can reveal sensitive information such as credentials, encryption keys, and other in-memory data.

## Description

ProcDump enables the creation of full or mini dumps of processes, either on demand, based on CPU thresholds, or triggered by exceptions. It supports both 32-bit and 64-bit architectures and can target specific processes by name or PID. This tool is particularly valuable for credential access techniques, as it allows dumping memory from protected processes like LSASS without necessarily requiring additional privilege escalation tools.

## Features

- Full memory dumps (-ma): Captures all process memory, including private data.
- Mini dumps (-mi): Smaller dumps focused on stack and heap.
- Exception monitoring (-e): Dumps on unhandled exceptions.
- CPU spike detection (-t): Triggers dumps when CPU usage exceeds a threshold.
- Multiple dump files: Supports creating multiple dumps over time (-n).
- EULA acceptance (-accepteula): Automates acceptance for scripted use.

## Installation

### Requirements

- Windows XP or later (including Server editions).
- Administrative privileges recommended for dumping system processes.
- Matching architecture (x86 or x64) to the target system.

### Install Commands

ProcDump is a portable executable and does not require formal installation. Download the ZIP file, extract the appropriate binary, and place it in your working directory or add to the system PATH.

```cmd
# Download using PowerShell (example)
Invoke-WebRequest -Uri "https://download.sysinternals.com/files/Procdump.zip" -OutFile "Procdump.zip"
Expand-Archive -Path "Procdump.zip" -DestinationPath "."

# Or download the full Sysinternals Suite
Invoke-WebRequest -Uri "https://download.sysinternals.com/files/SysinternalsSuite.zip" -OutFile "SysinternalsSuite.zip"
```

Use procdump.exe for 32-bit systems or procdump64.exe for 64-bit systems.

## Basic Usage

```cmd
procdump -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help and usage information |
| -v, --verbose | Enable verbose output for detailed logging |
| -accepteula | Automatically accept the EULA for non-interactive use |
| -ma | Generate a full memory dump |
| -e | Wait for and dump on an exception |
| -o | Overwrite existing dump files without prompting |

## Examples

### Example 1: Basic Usage

Create a full memory dump of a process:

```cmd
procdump -ma notepad.exe notepad.dmp
```

### Example 2: Advanced Usage

Dump LSASS on CPU threshold exceedance:

```cmd
procdump -t 80 -ma lsass.exe lsass_cpu.dmp
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]] OS Credential Dumping
- [[LSASS Memory]] LSASS Memory

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- File artifacts: Presence of procdump.exe, procdump64.exe, or .dmp files in unusual locations.
- Process creation: Sysmon Event ID 1 for procdump spawning child processes or accessing sensitive PIDs like LSASS (PID 500-1000 range).
- File creation: Monitoring for large .dmp files (>100MB) in temp or user directories.
- Network: If downloaded, look for connections to sysinternals.com.
- Behavioral: Unusual memory reads from protected processes via API monitoring (e.g., MiniDumpWriteDump calls).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Mimikatz]] (for parsing dumps to extract credentials)
- [[tools/tasklist]] (for enumerating processes before dumping)

## References

- [Official Sysinternals ProcDump Documentation](https://learn.microsoft.com/en-us/sysinternals/downloads/procdump)
- [Sysinternals Suite Download](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)
