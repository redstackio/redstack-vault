---
type: tool
description: >-
  SeatBelt is a C# tool designed for enumerating local Windows systems to
  identify potential security misconfigurations, vulnerabilities, and privilege
  escalation vectors.
url: 'https://github.com/GhostPack/Seatbelt'
tags:
  - C#
  - Enumeration
  - Post-Exploitation
platforms:
  - Windows
commands:
  - '[[commands/seatbelt-run-all-checks]]'
verified: true
validated: true
---

# SeatBelt

**Status**: Unverified

## Overview

SeatBelt is a lightweight C# executable that performs comprehensive enumeration of a Windows system, focusing on common security issues such as weak permissions, misconfigured services, and persistence mechanisms. It is particularly useful during post-exploitation phases for red team assessments to quickly identify privilege escalation opportunities without requiring administrative privileges for basic checks.

## Description

Developed as part of the GhostPack suite, SeatBelt runs a series of triage checks across categories like accounts, services, network shares, and registry settings. It outputs findings in a structured format, highlighting potential attack paths. The tool is standalone, requires no installation beyond compilation, and can be executed directly on target systems. It supports both user and admin contexts, with more detailed output in elevated modes.

## Features

- System triage checks for common privilege escalation vectors
- Enumeration of accounts, groups, services, and scheduled tasks
- Detection of weak permissions on files, shares, and registry keys
- Analysis of hotfixes, patches, and installed software
- Network configuration and RDP history enumeration
- Customizable checks via command-line arguments

## Installation

### Requirements

- .NET Framework 4.0 or later (typically pre-installed on Windows)
- Microsoft Visual Studio Community (free) with ".NET desktop development" workload for building from source

### Install Commands

SeatBelt is not installed via package managers; it must be compiled from source.

1. Clone the repository:
   ```bash
   git clone https://github.com/GhostPack/Seatbelt.git
   cd Seatbelt
   ```

2. Open `Seatbelt.sln` in Visual Studio.

3. Set configuration to "Release".

4. Build > Rebuild Solution.

The executable will be in `Seatbelt/bin/Release/Seatbelt.exe`.

For pre-compiled binaries, download releases from the GitHub repository (use with caution on air-gapped systems).

## Basic Usage

```command_prompt
Seatbelt.exe
```

This displays help and available check categories.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and available checks |
| `all` | Run all available enumeration checks |
| `<category>` | Run checks for a specific category (e.g., `accounts`, `services`) |
| `--stats` | Display summary statistics only |
| `-f <file>` | Output results to a file |

## Examples

### Example 1: Basic Usage

Run all checks:

```command_prompt
Seatbelt.exe all
```

### Example 2: Advanced Usage

Run only account-related checks and output to file:

```command_prompt
Seatbelt.exe accounts -f output.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.001]] Account Discovery: Local Account
- [[Process Discovery]] Process Discovery
- [[File and Directory Discovery]] File and Directory Discovery
- [[Local Groups]] Permission Groups Discovery: Local Groups

### Tactics

- [[Discovery]] Discovery
- [[Lateral Movement]] Lateral Movement

## Detection

- Monitor for execution of unsigned C# executables in user directories
- PowerShell or command-line logging showing `Seatbelt.exe` processes
- File creation in temp directories with SeatBelt artifacts
- Network shares or registry queries indicative of enumeration activity
- EDR alerts on process spawning from .NET runtimes without legitimate parent processes

## Related Procedures

- [[procedures/Windows-Local-Enumeration-for-Privesc]]
- [[procedures/Post-Exploitation-System-Recon]]

## Related Tools

- [[tools/PowerUp]]
- [[tools/SharpUp]]

## References

- Official GitHub: https://github.com/GhostPack/Seatbelt
- Blog post: https://www.netspi.com/blog/entryid/2000/attacking-kerberos-kicking-the-guard-dog-and-shooting-the-keysmith
