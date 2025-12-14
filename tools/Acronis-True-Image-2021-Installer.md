---
id: acronis-ti-2021
url: 'https://download.acronis.com/AcronisTrueImage2021.exe'
tags:
  - installer
  - vulnerable-software
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:52.175Z'
validated: true
submitted: true
---
# Acronis-True-Image-2021-Installer

**Status**: Unverified

## Overview

The Acronis True Image 2021 installer is the executable used to deploy the backup software, which triggers the vulnerable Scheduler2 Service during setup, enabling EXE hijacking demonstrations.

## Description

This MSI/EXE package installs the application and its services. In security testing, it's used to reproduce the LPE vuln by starting schedul2.exe. Supports silent installation for automation. Note: Vulnerable version; update to latest for mitigation.

## Features

- Feature 1: Silent install mode (/SILENT)
- Feature 2: Backup and imaging capabilities (irrelevant for exploit)
- Feature 3: Service auto-start on install

## Installation

### Requirements

- Windows 10/11
- Admin privileges
- ~2GB free space

### Install Commands

```cmd
# Run installer
AcronisTrueImage2021.exe /SILENT
```

## Basic Usage

```cmd
AcronisTrueImage2021.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| /SILENT | No UI |
| /LOG | Enable logging |
| /UNINSTALL | Remove software |

## Examples

### Example 1: Basic Usage

```cmd
AcronisTrueImage2021.exe /SILENT
```
Installs without prompts.

### Example 2: Advanced Usage

```cmd
AcronisTrueImage2021.exe /SILENT /LOG install.log
```
With logging for troubleshooting.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Malicious File]] User Execution: Malicious File (as trigger)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- AcronisTrueImage2021.exe process
- New services like schedul2
- Install logs in %TEMP%

## Related Procedures

- [[procedures/Install-Acronis-True-Image-to-Trigger-Service]]

## Related Tools

- [[tools/Procmon]]

## References

- Download: https://www.acronis.com/en-us/support/trueimage/2021/
- Vulnerability report: https://hackerone.com/reports/971610
