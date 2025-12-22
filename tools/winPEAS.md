---
id: b075d77e-0007-4f83-b697-b6db5f795b18
type: tool
verified: true
created_at: '2020-03-06T05:51:58.563727+00:00'
updated_at: '2023-10-10T18:30:49.995974+00:00'
platforms:
  - Windows
tags:
  - Enumeration
  - privileges
commands:
  - '[[commands/winpeas-download-with-certutil]]'
url: 'https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS'
validated: true
---

# winPEAS

**Status**: ✓ Verified

## Overview

winPEAS (Windows Privilege Escalation Awesome Script) is an enumeration tool designed to identify potential privilege escalation vectors on Windows systems. It automates the discovery of misconfigurations, weak permissions, and other vulnerabilities that could allow an attacker to elevate privileges from a low-privileged account to administrator or SYSTEM level. Commonly used in penetration testing and red team engagements for post-exploitation reconnaissance.

## Description

winPEAS scans a Windows host for common privilege escalation paths, including service misconfigurations, scheduled tasks, weak file permissions, registry settings, and more. It is part of the PEASS (Privilege Escalation Awesome Scripts Suite) and supports both batch script (.bat) and executable (.exe) formats. The .bat version is lightweight and runs without dependencies, while the .exe requires .NET Framework 4.0 or higher and offers more advanced enumeration capabilities, including obfuscation options to evade basic detection.

## Features

- Service enumeration for unquoted paths and weak permissions
- Checks for writable system files and directories
- Analysis of scheduled tasks and cron jobs
- Credential discovery in registry, files, and processes
- Network configuration and port scanning
- DLL hijacking and path hijacking detection
- Support for both x86 and x64 architectures
- Obfuscated builds to reduce signature-based detection

## Installation

### Requirements

- For .bat version: No additional requirements; runs on any Windows system with cmd.exe
- For .exe version: .NET Framework 4.0 or higher
- Optional: Visual Studio Community 2019 with ".NET desktop development" workload for building from source

### Install Commands

The tool is typically downloaded rather than installed. Use the following to acquire it:

For downloading the executable, see the related command [[commands/winpeas-download-with-certutil]].

#### Download .bat Version

Manually download from the GitHub repository:

1. Navigate to https://github.com/carlospolop/PEASS-ng/blob/master/winPEAS/winPEASbat/winPEAS.bat
2. Save as winPEAS.bat

#### Download Pre-built .exe (Obfuscated)

1. Go to https://github.com/carlospolop/PEASS-ng/releases/latest
2. Download winPEASx64.exe (or winPEASx86.exe for 32-bit)

#### Build .exe from Source (Windows)

1. Clone the repository:
   ```cmd
   git clone https://github.com/carlospolop/PEASS-ng.git
   cd PEASS-ng/winPEAS/winPEASexe
   ```
2. Open winPEAS.sln in Visual Studio 2019
3. Set configuration to "Release" and platform to target architecture (x64 or x86)
4. Build > Rebuild Solution
5. Find the output at winPEAS/bin/x64/Release/winPEAS.exe (or x86 equivalent)

To obfuscate the build and reduce malware detection, install Visual Studio's Dotfuscator Community Edition and apply it post-build as per the repository instructions.

## Basic Usage

```cmd
winPEAS.exe
```

This runs the default enumeration scan, outputting results to the console and log files.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help and available arguments |
| `-f <file>` | Specify an output file for results |
| `--network` | Include network enumeration (e.g., open ports, shares) |
| `--credentials` | Focus on credential dumping and storage checks |
| `--services` | Enumerate services only |
| `--fast` | Quick scan mode, skipping intensive checks |

## Examples

### Example 1: Basic Enumeration

Run the full scan on a compromised host:

```cmd
winPEASx64.exe > enum_results.txt
```

Review enum_results.txt for potential priv esc vectors like writable services or weak ACLs.

### Example 2: Network-Focused Scan

```cmd
winPEASx64.exe --network
```

This identifies open ports, active shares, and network misconfigurations that could aid lateral movement.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Information Discovery]] System Information Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery
- [[Process Discovery]] Process Discovery
- [[File and Directory Discovery]] File and Directory Discovery
- [[Network Service Scanning]] Network Service Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

- Monitor for downloads from GitHub PEASS releases or certutil executions fetching .exe files
- Look for .NET processes spawning with unusual command lines (e.g., winPEAS.exe)
- File creation of .bat or .exe in temp directories
- Console output or log files containing enumeration keywords (e.g., "Potential PrivEsc")
- EDR alerts on privilege escalation scanning behaviors or registry queries

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[tools/PowerUp]]
- [[tools/Sherlock]]

## References

- Official GitHub: https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS
- Building Instructions: https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS/winPEASexe
