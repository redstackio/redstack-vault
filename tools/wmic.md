---
id: 82ef6bbc-b218-49b4-8229-0372efe326cf
name: wmic
type: tool
verified: true
created_at: '2020-03-05T00:02:29.991918+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - '[[Enumeration]]'
  - '[[Operating Systems]]'
url: 'https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmic'
commands:
  - '[[commands/wmic-query-installed-hotfixes]]'
validated: true
---

# wmic

**Status**: ✓ Verified

## Overview

wmic (Windows Management Instrumentation Command-line) provides a command-line interface for interacting with Windows Management Instrumentation (WMI), allowing users to manage system data and operations on Windows-based systems. It is commonly used in security testing for enumeration tasks such as querying processes, services, installed software, and hotfixes to gather information about the target environment.

## Description

wmic enables comprehensive control and scripting of WMI through a simple command-line syntax. It supports numerous aliases for common actions (e.g., 'process', 'service', 'qfe' for hotfixes), making it a powerful tool for remote and local system queries without needing additional software. In offensive security, it is often used during reconnaissance and discovery phases to identify system configurations, patch levels, and running services that could reveal vulnerabilities or escalation paths.

## Features

- **Aliases for Common Queries**: Built-in shortcuts like 'wmic process list' or 'wmic qfe' for quick enumeration.
- **Remote Execution**: Supports querying remote systems with /node, /user, and /password options.
- **Output Formatting**: Customizable formats including CSV, XML, and table for easy parsing.
- **WMI Class Access**: Direct access to WMI classes for detailed system information retrieval.
- **Scripting Integration**: Easily integrable into batch scripts or PowerShell for automated tasks.

## Installation

### Requirements

- Windows XP or later (built-in on modern Windows versions).
- Administrative privileges for certain queries.

### Install Commands

wmic is pre-installed on all supported Windows platforms. No additional installation is required.

If needed on older systems or for verification:

```command_prompt
# Verify installation
wmic /?
```

## Basic Usage

```command_prompt
wmic /?
```

This displays the help menu with available aliases and syntax.

### Common Options

| Option | Description |
|--------|-------------|
| `/node:hostname` | Specify remote target machine |
| `/user:username` | Credentials for remote access |
| `/password:password` | Password for authentication |
| `/format:csv` | Output in CSV format |
| `/format:table` | Output in table format (default) |
| `alias` | Use predefined aliases like 'process', 'service', 'qfe' |

## Examples

### Example 1: Basic Usage

Query installed hotfixes:

```command_prompt
wmic qfe get HotFixID,InstalledOn
```

### Example 2: Advanced Usage

Query processes on a remote system and output to CSV:

```command_prompt
wmic /node:remotehost /user:admin /password:pass process list /format:csv > processes.csv
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Information Discovery]] System Information Discovery
- [[Process Discovery]] Process Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Windows Event Logs for WMI activity (Event ID 5858 in Microsoft-Windows-WMI-Activity/Operational).
- Look for command-line executions of 'wmic.exe' in process monitoring tools like Sysmon.
- Network traffic anomalies if using remote /node queries.
- File system changes if outputting to files (e.g., CSV exports).

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
- [[tools/systeminfo]]

## References

- [Microsoft Docs: WMIC](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmic)
- [WMI Overview](https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page)
