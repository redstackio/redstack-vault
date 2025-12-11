---
url: null
tags:
  - monitoring
  - windows
type: tool
platforms:
  - Windows
description: Windows tool for monitoring processes and file system activity.
id: 9b32f912-62c5-416a-9849-8d616703a933
created_at: '2025-12-11T03:47:56.451Z'
updated_at: '2025-12-11T03:47:56.451Z'
verified: false
validated: true
submitted: true
---
# Process Monitor

**Status**: Unverified

## Overview

Process Monitor is a Windows Sysinternals tool used for real-time monitoring of process creations, file system operations, and registry activity, essential for identifying spawned processes in applications like PlayStation Now.

## Description

It captures detailed events for troubleshooting and security analysis, such as process starts (e.g., AGL.exe) and network bindings.

## Features

- Feature 1: Real-time process monitoring
- Feature 2: File and registry event logging
- Feature 3: Filtering and highlighting

## Installation

### Requirements

- Windows OS
- Administrative privileges

### Install Commands

```bash
# Download from Sysinternals website
```

## Basic Usage

```bash
procmon.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| `/Quiet` | Run without UI |
| `/BackingFile` | Specify log file |

## Examples

### Example 1: Basic Usage

```bash
procmon.exe
```

### Example 2: Advanced Usage

```bash
procmon.exe /Quiet /BackingFile log.pml
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for procmon.exe execution
- Detection method 2: Log file creations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #netstat

## References

- https://docs.microsoft.com/en-us/sysinternals/downloads/procmon
