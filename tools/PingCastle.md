---
id: 7ee70280-a3ad-449c-9606-c3930f159ab5
type: tool
verified: true
created_at: '2019-08-28T21:17:38.252367+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - auditing
  - reconnaissance
  - security-assessment
url: 'https://www.pingcastle.com/'
commands:
  - '[[commands/pingcastle-basic-audit]]'
  - '[[commands/pingcastle-export-ad-data]]'
  - '[[commands/pingcastle-console-mode]]'
validated: true
---

# PingCastle

**Status**: Unverified

## Overview

PingCastle is a free, open-source Windows-based utility designed for auditing Active Directory (AD) security. It assesses the risk level of AD infrastructure by checking for vulnerable practices, misconfigurations, and compliance issues, providing actionable recommendations to improve security posture. Commonly used in red teaming for reconnaissance, blue teaming for audits, and compliance assessments.

## Description

PingCastle scans AD environments for issues like weak password policies, excessive privileges, stale objects, and STIG violations. It generates detailed HTML reports with risk scores (Low/Medium/High/Critical) and supports both GUI and console modes for flexibility in automated or manual operations. The tool collects data on users, groups, computers, trusts, and schema to identify attack paths and hardening opportunities. It's particularly valuable for domain admins and security professionals evaluating AD resilience against threats like pass-the-hash or golden ticket attacks.

## Features

- **Risk Scoring**: Assigns scores based on detected vulnerabilities and best practices.
- **STIG Compliance**: Checks against DISA STIG requirements for AD.
- **Report Generation**: Produces HTML, CSV, and console outputs for analysis.
- **Console Mode**: Supports scripting and automation without GUI.
- **Data Export**: Allows extraction of AD objects for further processing.

## Installation

### Requirements

- Windows OS (Windows 7 or later, Server 2008 or later).
- .NET Framework 4.5 or higher.
- Domain admin credentials or read access to AD (for full audits).
- No additional dependencies; self-contained executable.

### Install Commands

1. Download the latest release from the official website.

```powershell
# Download using PowerShell (example for latest version)
Invoke-WebRequest -Uri "https://www.pingcastle.com/download" -OutFile "PingCastle.zip"

# Extract the ZIP file
Expand-Archive -Path "PingCastle.zip" -DestinationPath "C:\Tools\PingCastle"

# Navigate to the directory
cd "C:\Tools\PingCastle"
```

- For Kali Linux or cross-platform use: Run via Wine, but native Windows is recommended.
- Official download: https://www.pingcastle.com/ (ZIP file containing PingCastle.exe).

## Basic Usage

```cmd
PingCastle.exe
```

This launches the GUI for interactive auditing. For command-line, use console mode.

### Common Options

| Option | Description |
|--------|-------------|
| --server | Specifies the target domain controller |
| --adcsv | Exports AD data to CSV |
| /console | Runs in console mode |
| --outputdir | Sets output directory for reports |
| -h, --help | Shows help and available options |

## Examples

### Example 1: Basic Usage

Run a GUI audit:

```cmd
PingCastle.exe
```

Select the domain and click "Run" to generate a health check report.

### Example 2: Advanced Usage

Automated console audit:

```cmd
PingCastle.exe /console /server:dc01.example.com
```

This performs a full scan and outputs results to console and files.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.002]] Domain Trust Discovery
- [[T1087.001]] Account Discovery: Local Account
- [[Domain Groups]] Permission Groups Discovery: Domain Groups

### Tactics

- [[Discovery]] Discovery
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- File creation: PingCastle.exe execution or report files (e.g., *.html, *.csv) in temp directories.
- Process monitoring: PingCastle.exe running with LDAP queries to domain controllers.
- Network traffic: Increased LDAP/AD queries from non-admin workstations.
- EDR alerts: Unsigned executable or anomalous AD enumeration.

## Related Procedures

- [[procedures/Active-Directory-Risk-Audit]]
- [[procedures/Enumerate-AD-Objects]]

## Related Tools

- [[tools/BloodHound]]
- [[tools/PowerView]]

## References

- Official website: https://www.pingcastle.com/
- GitHub repository: https://github.com/vletoux/pingcastle (for source and updates)
- Documentation: Included in the ZIP download or online wiki.
