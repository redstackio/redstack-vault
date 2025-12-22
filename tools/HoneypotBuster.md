---
id: 1a028663-337d-4ca0-b3c5-9c8362b748a2
type: tool
verified: true
created_at: '2019-08-28T21:17:37.613738+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - discovery
  - honeypot-detection
  - red-team
  - powershell
url: 'https://github.com/mgeeky/HoneypotBuster'
validated: true
---

# HoneypotBuster

**Status**: Unverified

## Overview

HoneypotBuster is a PowerShell module designed for red team operations to detect honeypots and honeytokens in network environments or on individual hosts. It helps attackers identify deceptive security measures early in reconnaissance, allowing for evasion or alternative attack paths.

## Description

This module provides functions to scan networks for unusual behaviors indicative of honeypots (e.g., delayed responses, atypical port configurations) and check hosts for honeytokens (e.g., fake credentials or files). It is particularly useful in penetration testing to validate the authenticity of discovered assets and avoid alerting defenders.

## Features

- Feature 1: Network scanning for honeypot indicators like tarpits or canary tokens.
- Feature 2: Host-level checks for suspicious files, registry entries, and processes.
- Feature 3: Configurable output formats (JSON, CSV) for integration with other tools.
- Feature 4: Support for remote host scanning via PowerShell remoting.

## Installation

### Requirements

- PowerShell 5.0 or later
- Administrative privileges for host scans
- Network access for remote operations

### Install Commands

```powershell
# Install from PowerShell Gallery (if available)
Install-Module -Name HoneypotBuster -Force

# Or clone from GitHub and import
Invoke-WebRequest -Uri https://github.com/mgeeky/HoneypotBuster/archive/master.zip -OutFile HoneypotBuster.zip
Expand-Archive HoneypotBuster.zip
Import-Module .\HoneypotBuster-master\HoneypotBuster.psm1
```

## Basic Usage

```powershell
tool-name --help
```

Get-Help Invoke-HoneypotBuster

### Common Options

| Option | Description |
|--------|-------------|
| -ScanType | Specifies scan mode (Network or Host) |
| -Target | Target network or host |
| -OutputPath | Path for results file |
| -Verbose | Enable detailed logging |

## Examples

### Example 1: Basic Usage

```powershell
Import-Module HoneypotBuster
Invoke-HoneypotBuster -ScanType Network -Target 192.168.1.0/24
```

### Example 2: Advanced Usage

```powershell
Import-Module HoneypotBuster
Invoke-HoneypotBuster -ScanType Host -Target localhost -CheckTypes Files,Registry -OutputPath results.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[System Information Discovery]] System Information Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: PowerShell module imports and invocations in event logs (Event ID 4104).
- Detection method 2: Unusual network probing patterns or host file/registry access.
- Detection method 3: Presence of HoneypotBuster.psm1 in temporary directories.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[PowerShell]]
- [[tools/Nmap]]

## References

- Official GitHub: https://github.com/mgeeky/HoneypotBuster
- PowerShell Gallery (if listed)

*Last updated: 2023-10-01*
