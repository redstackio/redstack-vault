---
id: i9j0k1l2-m3n4-5678-ijkl-901234567890
url: null
tags:
  - batch
  - payload
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:29:44.536Z'
validated: true
submitted: true
---
# malstaller-bat

**Status**: Unverified

## Overview

A custom malicious batch script serving as the payload in the VeraCrypt UAC bypass, executed with elevated privileges to compromise the installation.

## Description

malstaller.bat is the hijacked target; it performs actions like copying a fake executable (PoC: putty.exe as VeraCrypt2.exe) to the VeraCrypt folder and running it. Customize username and paths; receives URL via %1 but ignores it for PoC.

## Features

- Copies and executes fake binaries
- Runs silently in elevated context
- Easily extensible for deletion/scheduling

## Installation

### Requirements

- Elevated execution context (via hijack)
- Access to source files (e.g., putty.exe for PoC)

### Install Commands

```batch
# Create on desktop: notepad malstaller.bat
# Add copy and exec lines
```

## Basic Usage

```batch
malstaller.bat
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Edit script for actions |

## Examples

### Example 1: Basic Usage

```batch
@echo off
copy "C:\Windows\System32\putty.exe" "C:\Program Files\VeraCrypt\VeraCrypt2.exe"
"C:\Program Files\VeraCrypt\VeraCrypt2.exe"
```

### Example 2: Advanced Usage

Add task scheduling: schtasks /create /tn "MalTask" /tr "malware.exe" /sc once /st 00:00

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Bypass User Account Control]]

### Tactics

- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor file copies to Program Files\VeraCrypt
- Detect anomalous batch executions post-UAC
- Scan for putty.exe or similar in app folders

## Related Procedures

- [[procedures/Create-Malicious-Payload-for-Elevation]]

## Related Tools

- [[tools/add-bat]]

## References

- HackerOne Report #530292
