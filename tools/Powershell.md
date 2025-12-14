---
url: 'https://learn.microsoft.com/en-us/powershell/'
tags:
  - scripting
  - automation
  - dos
type: tool
platforms:
  - Windows
description: >-
  Scripting environment for automating HTTP requests and TCP communications in
  Windows.
id: 6f215576-088d-43d0-9674-c4c264d2349e
created_at: '2025-12-14T05:32:10.000Z'
updated_at: '2025-12-14T05:32:10.000Z'
verified: false
validated: true
submitted: true
---
# PowerShell

**Status**: Unverified

## Overview

PowerShell is a task automation and configuration management framework from Microsoft, consisting of a command-line shell and scripting language. In security testing, it's used for scripting network interactions, like raw HTTP POSTs for exploitation demos.

## Description

PowerShell excels in .NET integration, allowing custom functions for TCP sockets (e.g., Send-NetworkData) to bypass higher-level APIs. Here, it's configured for looping file uploads to embedded devices, simulating DoS attacks without external tools.

## Features

- Feature 1: Built-in .NET classes for TCPClient and Stream handling
- Feature 2: Pipeline support for sending multi-line data like HTTP requests
- Feature 3: Loop constructs for automation (e.g., 20,000 iterations)

## Installation

### Requirements

- Windows OS (native) or PowerShell Core for cross-platform

### Install Commands

```bash
# On Windows, pre-installed; for Linux/macOS:
winget install --id Microsoft.PowerShell --source winget
```

## Basic Usage

```powershell
Get-Help Send-NetworkData
```

### Common Options

| Option | Description |
|--------|-------------|
| -Verbose | Enable verbose output |
| -Debug | Debug mode for troubleshooting |

## Examples

### Example 1: Basic Usage

```powershell
"Hello" | Send-NetworkData -Computer 127.0.0.1 -Port 80
```

### Example 2: Advanced Usage

```powershell
# Define function then use in loop for uploads
for ($i=1; $i -le 10; $i++) { ... | Send-NetworkData ... }
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]]
- [[Remote File Copy]]

### Tactics

- [[Execution]]
- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for PowerShell.exe spawning with network connections to port 80
- Log script blocks containing TCPClient or loops with high iterations
- Detect rapid outbound HTTP POSTs from PowerShell processes

## Related Procedures

- [[procedures/test-unauthenticated-file-upload-to-login-cgi]]
- [[procedures/upload-multiple-files-to-exhaust-disk-space]]

## Related Tools

- [[tools/curl]]
- [[tools/netcat]]

## References

- Official documentation: https://learn.microsoft.com/en-us/powershell/
- Related resources: PowerShell for Pentesters
