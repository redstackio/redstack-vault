---
id: tool-procmon
url: ''
tags:
  - monitoring
  - rce
type: tool
verified: false
platforms:
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.228Z'
validated: true
submitted: true
---
# Process Monitor (ProcMon)

**Status**: Unverified

## Overview

Sysinternals tool for monitoring real-time file system, registry, and process/thread activity on Windows, used to verify RCE by detecting spawned processes.

## Description

In security testing, ProcMon captures process creation events to confirm exploits like the Simplenote RCE, filtering for cmd.exe or netplwiz in user context.

## Features

- Feature 1: Real-time process monitoring
- Feature 2: Filtering by process name/path
- Feature 3: Export logs for analysis

## Installation

### Requirements

- Windows OS

### Install Commands

```bash
# Download from Microsoft Sysinternals
# Run ProcMon.exe as admin
```

## Basic Usage

```bash
procmon.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| Filter | Add filters (e.g., Process Name is cmd.exe) |
| Capture | Start/stop events |

## Examples

### Example 1: Basic Usage

Run ProcMon, set filter for Process Name contains "netplwiz", start capture, trigger exploit.

### Example 2: Advanced Usage

Export to PML for offline analysis.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]] Process Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- ProcMon.exe running on system
- High event logging from Sysinternals

## Related Procedures

- [[procedures/Trigger-XSS-by-Previewing-Note]]

## Related Tools

- [[tools/JavaScript-Eval-Encoder]]

## References

- Microsoft Sysinternals documentation
