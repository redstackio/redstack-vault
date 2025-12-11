---
url: 'https://docs.microsoft.com/en-us/sysinternals/downloads/procmon'
tags:
  - monitoring
  - discovery
type: tool
platforms:
  - Windows
description: >-
  Windows tool for monitoring system processes and file/registry/network
  activity
id: b1d0d0b4-0fee-449f-b2c5-7211c3342e9e
created_at: '2025-12-11T06:10:30.642Z'
updated_at: '2025-12-11T06:10:30.642Z'
verified: false
validated: true
submitted: true
---
# Process Monitor

**Status**: Unverified

## Overview

Process Monitor is a Sysinternals tool for real-time monitoring of file system, registry, process, thread, and DLL activity on Windows systems.

## Description

Used in security testing to observe application behavior, such as process spawning and network connections in vulnerabilities like the PlayStation Now exploit.

## Features
- Real-time event logging
- Advanced filtering
- Process tree view

## Installation

### Requirements
- Windows OS

### Install Commands

Download from official site and run procmon.exe.

## Basic Usage

```bash
procmon.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| `/Quiet` | Run without splash screen |
| `/BackingFile` | Specify log file |

## Examples

### Example 1: Basic Usage

Run procmon.exe and filter for psnowlauncher.exe.

## MITRE ATT&CK Mapping

### Techniques
- [[Network Sniffing]]

### Tactics
- [[Discovery]]

## Detection

- Monitor for procmon.exe execution in logs

## Related Procedures

## Related Tools
- [[tools/netstat]]

## References
- Microsoft Sysinternals documentation
