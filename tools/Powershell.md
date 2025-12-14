---
id: tool-powershell-001
url: 'https://learn.microsoft.com/en-us/powershell/'
tags:
  - scripting
  - automation
type: tool
verified: false
platforms:
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.940Z'
validated: true
submitted: true
---
# PowerShell

**Status**: Unverified

## Overview

PowerShell is a cross-platform task automation and configuration management framework from Microsoft, used here for scripting raw TCP/HTTP requests to automate file uploads in security testing.

## Description

It excels in network operations, allowing custom functions like Send-NetworkData for socket-based HTTP sends. In offensive security, it's common for automating exploits, DoS simulations, and payload delivery on Windows environments.

## Features

- Feature 1: Built-in .NET integration for TCP sockets and streams
- Feature 2: Looping and variable handling for bulk operations
- Feature 3: Encoding support for HTTP payloads

## Installation

### Requirements

- Windows 7+ or PowerShell Core on Linux/macOS

### Install Commands

```bash
# On Windows, pre-installed; for Core:
winget install --id Microsoft.PowerShell --source winget
```

## Basic Usage

```powershell
Get-Help
```

### Common Options

| Option | Description |
|--------|-------------|
| -Verbose | Detailed output |
| -ErrorAction | Handle errors |

## Examples

### Example 1: Basic Usage

```powershell
Test-NetConnection -ComputerName target -Port 80
```

### Example 2: Advanced Usage

Custom script for HTTP requests as in the DoS procedure.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for powershell.exe with network connections
- Log anomalous TCP sends to port 80
- Script block logging in Windows Event Logs

## Related Procedures

- [[procedures/Repeat-Uploads-for-Disk-Exhaustion]]

## Related Tools

- [[cmd.exe]]
- [[Python]]

## References

- Official documentation: https://learn.microsoft.com/en-us/powershell/
- Related resources: PowerShell for Pentesters guides
