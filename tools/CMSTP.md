---
id: fdce6099-d49d-4606-98d7-8d987924826d
type: tool
verified: true
created_at: '2019-08-28T21:17:37.410908+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Windows
tags:
  - applocker
  - defense-bypass
url: >-
  https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/deployment/troubleshooting/connection-manager-profile-installer-cmstp-exe
validated: true
---

# CMSTP

**Status**: Unverified

## Overview

CMSTP (Microsoft Connection Manager Profile Installer) is a built-in Windows command-line utility designed to install Connection Manager service profiles using INF files. In offensive security contexts, it is commonly abused to bypass application whitelisting restrictions like AppLocker by executing arbitrary code through crafted INF files that load DLLs or SCT (Script Component) files from remote locations.

## Description

CMSTP.exe processes INF files to configure VPN and dial-up connections but can be manipulated to download and execute remote payloads. Attackers create malicious INF files with sections that reference remote URLs for DLLs or SCT files, which CMSTP then fetches and runs under the context of a signed Microsoft binary. This technique evades defenses that only allow execution of trusted, signed executables. It is particularly effective in environments with strict application control policies but limited network monitoring for such legitimate tools.

## Features

- Processes INF files to install connection profiles
- Supports silent execution without user interaction
- Can load external DLLs or SCT scripts referenced in INF files
- Runs with the privileges of the invoking user, enabling lateral movement or payload execution
- Integrated with Windows since Windows 2000

## Installation

### Requirements

- Windows operating system (XP and later)
- No additional dependencies; it is a native system binary

### Install Commands

CMSTP.exe is pre-installed on all modern Windows versions and located in `C:\Windows\System32\cmstp.exe`. No installation is required.

To verify presence:

```cmd
where cmstp
```

## Basic Usage

```cmd
cmstp /?
```

### Common Options

| Option | Description |
|--------|-------------|
| `/ni` | No user interaction; runs silently |
| `/s <path>` | Specifies the INF file to process |
| `/au` | Installs for all users |
| `/c` | Cleanup mode |

## Examples

### Example 1: Basic Usage

Process an INF file silently:

```cmd
cmstp.exe /ni /s C:\path\to\profile.inf
```

### Example 2: Advanced Usage

Install a profile for all users:

```cmd
cmstp.exe /au /s C:\Temp\malicious.inf
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Signed Binary Proxy Execution]] System Binary Proxy Execution
- [[Hijack Execution Flow]] Hijack Execution Flow
- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor command-line arguments to cmstp.exe for `/ni /s` with suspicious INF paths
- Watch for network connections from cmstp.exe to unexpected domains (e.g., downloading SCT/DLL)
- Enable process creation logging (Sysmon Event ID 1) to track cmstp spawning child processes like scrobj.dll
- AppLocker or WDAC logs showing cmstp executing unsigned scripts
- Unusual file creations in system directories like `C:\Windows\Tasks`

## Related Commands

- [[commands/cmstp-execute-inf-file]]

## References

- Official Microsoft Documentation: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/deployment/troubleshooting/connection-manager-profile-installer-cmstp-exe
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1218/
- LOLBAS Project: https://lolbas-project.github.io/lolbas/Binaries/Cmstp/
