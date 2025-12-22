---
type: tool
description: >-
  Built-in Windows command for displaying detailed system configuration
  information, including OS details, hardware, security patches, and network
  settings.
url: >-
  https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/systeminfo
verified: true
platforms:
  - Windows
tags:
  - Enumeration
  - Operating Systems
commands:
  - '[[commands/systeminfo-display-system-configuration]]'
validated: true
---

# systeminfo

**Status**: ✓ Verified

## Overview

systeminfo is a built-in Windows command-line utility that provides detailed configuration information about the local computer. It is commonly used in security testing for system enumeration, revealing OS version, installed hotfixes, hardware specifications, and security settings. This tool is essential for initial reconnaissance in Windows environments to assess patch levels and identify potential vulnerabilities.

## Description

The systeminfo command queries the Windows operating system for a wide range of configuration data, outputting it in a structured text format. It covers categories such as boot device, system manufacturer, total physical memory, domain details, and a list of installed hotfixes (KB numbers). In offensive security operations, it helps attackers map the target's environment, determine exploit compatibility, and gather intelligence for privilege escalation or lateral movement. No external installation is required as it is native to all Windows versions from XP onward.

## Features

- **OS and Hardware Enumeration**: Displays OS name, version, build number, processor type, and memory details.
- **Patch and Hotfix Listing**: Provides a complete list of installed updates, useful for identifying unpatched vulnerabilities.
- **Network and Security Info**: Includes domain/workgroup status, logon server, and security policy settings.
- **Hotfix Tracking**: Dedicated section for KB updates, aiding in vulnerability assessment.
- **No Arguments Needed**: Runs comprehensively by default, with options for output redirection.

## Installation

### Requirements

- Windows operating system (XP or later).
- Command Prompt or PowerShell access.

### Install Commands

systeminfo is pre-installed on all Windows systems. No installation is required.

To verify availability:

```command_prompt
systeminfo /?
```

## Basic Usage

```command_prompt
systeminfo
```

### Common Options

| Option | Description |
|--------|-------------|
| /? | Show help message |
| > filename.txt | Redirect output to a file (no built-in flag, use shell redirection) |

## Examples

### Example 1: Basic Usage

Run the command to display all system information:

```command_prompt
systeminfo
```

### Example 2: Advanced Usage

Save output to a file for offline analysis:

```command_prompt
systeminfo > systeminfo_output.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Information Discovery]] System Information Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Command-line logging showing 'systeminfo.exe' execution.
- File creation or network transfer of output files containing system details.
- Process monitoring for cmd.exe or powershell.exe spawning systeminfo.
- EDR alerts on enumeration behaviors in user or system contexts.

## Related Procedures

- Procedures using systeminfo for Windows enumeration and patch assessment.

## Related Tools

- [[tools/wmic]] (alternative for WMI-based queries)
- [[tools/Powershell]] (for Get-ComputerInfo cmdlet)

## References

- Official Microsoft Documentation: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/systeminfo
