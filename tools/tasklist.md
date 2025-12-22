---
id: 53182557-b183-44ac-bfdc-8002323b883c
name: tasklist
type: tool
verified: true
created_at: '2020-03-04T20:00:45.593036+00:00'
updated_at: '2023-05-30T19:55:11.440197+00:00'
platforms:
  - Windows
tags:
  - Enumeration
  - Operating Systems
  - process
url: >-
  https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tasklist
commands:
  - '[[commands/tasklist-enumerate-running-processes]]'
validated: true
---

# tasklist

**Status**: ✓ Verified

## Overview

tasklist is a built-in Windows command-line tool used to display a list of currently running processes on the local or remote system. In security testing, it is commonly used for process discovery to identify running applications, services, and potential targets for further enumeration or exploitation.

## Description

tasklist provides detailed information about processes, including process ID (PID), session name, session number, memory usage, and status. It supports filtering, verbose output, and remote execution, making it a valuable living-off-the-land binary (LOLBin) for offensive security operations without requiring additional tools. It maps to MITRE ATT&CK technique T1057 (Process Discovery) under the Discovery tactic.

## Features

- List all active processes with basic details (PID, memory, status)
- Verbose mode for extended information (CPU time, user name)
- Module listing to see DLLs loaded by processes
- Filtering options based on image name, PID, status, etc.
- Support for remote systems using /s and /u flags
- Output formatting (table, CSV, list) for scripting and parsing

## Installation

### Requirements

- Windows NT/2000 or later (pre-installed on all modern Windows versions)
- Administrative privileges for remote access or detailed info

### Install Commands

Not applicable; tasklist.exe is included by default in %SystemRoot%\System32.

## Basic Usage

```cmd
tasklist /?
```

### Common Options

| Option | Description |
|--------|-------------|
| `/v` | Verbose mode with additional columns (CPU, user, window title)
| `/m` | Displays modules (DLLs) loaded by each process
| `/fo <format>` | Specifies output format: table (default), list, or csv
| `/fi <filter>` | Applies filters, e.g., "imagename eq notepad.exe"
| `/s <system>` | Specifies remote system to query
| `/u <username>` | Specifies user for remote access
| `/p <password>` | Password for remote access

## Examples

### Example 1: Basic Usage

Lists all running processes in table format.

```cmd
tasklist
```

### Example 2: Advanced Usage

Lists processes with verbose details and filters for a specific image.

```cmd
tasklist /v /fi "imagename eq explorer.exe"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]] Process Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Windows Event Logs: Command line auditing (Event ID 4688) showing tasklist.exe execution
- Sysmon: Event ID 1 (Process Creation) with Image: tasklist.exe and CommandLine containing filters or remote flags
- EDR alerts on process enumeration activity from cmd.exe or PowerShell
- Unusual remote connections to admin shares (e.g., IPC$) for /s flag usage

## Related Procedures

- [[procedures/Process-Discovery-via-Tasklist]]

## Related Tools

- [[tools/Powershell]] (Get-Process cmdlet)
- [[tools/processexplorer]] (GUI alternative from Sysinternals)

## References

- Official Microsoft documentation: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/tasklist
- LOLBAS project: https://lolbas-project.github.io/lolbas/OtherMSBinaries/Tasklist/
