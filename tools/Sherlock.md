---
id: cff19d06-10a0-4147-acbf-33498c51b2d2
name: Sherlock
type: tool
verified: true
created_at: '2019-08-28T21:17:39.744699+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Windows
tags:
  - Enumeration
  - PowerShell
commands:
  - '[[commands/sherlock-dot-source-and-run-find-allvulns]]'
url: 'https://github.com/rasta-mouse/Sherlock'
validated: true
---

# Sherlock

**Status**: Unverified

## Overview

Sherlock is a PowerShell script designed to quickly identify missing software patches and local privilege escalation vulnerabilities on Windows systems. It is commonly used in penetration testing and red team engagements to enumerate potential privilege escalation vectors by checking for known unpatched vulnerabilities.

## Description

Sherlock automates the detection of various Windows vulnerabilities related to privilege escalation, such as those in MS Bulletins and CVEs. It inspects system configurations, installed software, and registry entries to determine if the target is vulnerable, providing links to relevant exploits where applicable. This tool is particularly useful during post-exploitation phases to assess lateral movement and escalation opportunities without manual verification of each potential issue.

## Features

- Automated checks for over 20 common privilege escalation vulnerabilities
- Reports vulnerability status (Vulnerable, Patched, or Not Applicable)
- Provides direct links to Exploit-DB entries for vulnerable items
- Lightweight and script-based, requiring no additional dependencies beyond PowerShell
- Focuses on local system enumeration for quick assessment

## Installation

### Requirements

- Windows operating system with PowerShell 2.0 or later
- Git (optional, for cloning the repository)
- Administrative privileges may be required for some checks, but basic enumeration runs as a standard user

### Install Commands

```powershell
# Clone the repository from GitHub
git clone https://github.com/rasta-mouse/Sherlock.git

# Copy the script to the target directory (e.g., current working directory)
Copy-Item -Path "Sherlock/Sherlock.ps1" -Destination "."
```

On systems without Git, download the Sherlock.ps1 file directly from the GitHub repository and place it in an accessible directory.

## Basic Usage

```powershell
. .\Sherlock.ps1; Find-AllVulns
```

### Common Options

Sherlock primarily uses function calls within the script. No command-line flags are available as it is a sourced PowerShell module.

| Option | Description |
|--------|-------------|
| Find-AllVulns | Enumerates all supported vulnerabilities |
| Find-VulnMS10-015 | Checks specific vulnerability (e.g., MS10-015) |
| Find-VulnMS10-092 | Checks another specific vulnerability |

## Examples

### Example 1: Basic Usage

Run the full vulnerability scan:

```powershell
. .\Sherlock.ps1; Find-AllVulns
```

This will output a list of checked vulnerabilities with their status.

### Example 2: Advanced Usage

Check a specific vulnerability:

```powershell
. .\Sherlock.ps1; Find-VulnMS15-051
```

This targets a single MS Bulletin for focused enumeration.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Information Discovery]] System Information Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery
- [[Process Discovery]] Process Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Execution of unsigned PowerShell scripts (Sherlock.ps1) from unusual locations
- PowerShell logging events showing sourcing of external scripts and function calls like Find-AllVulns
- File system access patterns to Sherlock.ps1 or temporary downloads
- Console output containing vulnerability checks (e.g., MSBulletin references) in process logs
- Behavioral analytics flagging enumeration of system patches and registry keys

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PowerSploit]] (companion suite for PowerShell post-exploitation)
- [[tools/winPEAS]] (Windows enumeration script with similar priv esc checks)

## References

- Official GitHub Repository: https://github.com/rasta-mouse/Sherlock
- Author: @rasta_mouse
- Related Blog: https://www.artsat.com/blog/2015/5/11/sherlock
