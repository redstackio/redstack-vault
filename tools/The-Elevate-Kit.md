---
id: c491825c-afe1-4202-ae28-3e22cbba76aa
type: tool
verified: true
created_at: '2019-08-28T21:17:40.974312+00:00'
updated_at: '2023-10-01T12:00:00Z'
platforms:
  - Windows
tags:
  - privilege-escalation
  - cobalt-strike
  - post-exploitation
  - uac-bypass
url: 'https://www.cobaltstrike.com/help-managing-payloads#elevate'
validated: true
---

# The-Elevate-Kit

**Status**: Unverified

## Overview

The Elevate Kit is an extension for Cobalt Strike that demonstrates and implements third-party privilege escalation techniques using the Beacon payload. It provides modular scripts (Aggressor CNA files) to perform UAC bypasses, token manipulation, and process spawning for elevating privileges on Windows targets during red team operations.

## Description

Cobalt Strike's Beacon is a post-exploitation agent, and the Elevate Kit enhances it by integrating community-developed or custom scripts for local privilege escalation. Common techniques include environment variable manipulation (e.g., via Fodhelper), COM interface hijacking, and spawning elevated children. This kit is particularly useful in engagements where initial access is gained with standard user privileges, allowing escalation to SYSTEM or Administrator without additional tools. It supports Windows 7 through 11, focusing on stealthy bypasses to evade EDR detection.

## Features

- **UAC Bypass Modules**: Multiple methods like eventvwr, fodhelper, and sdclt for silent elevation.
- **Token Operations**: Steal and impersonate tokens from privileged processes.
- **Process Spawning**: Spawn elevated cmd.exe or PowerShell sessions as children.
- **Modular Loading**: Easy integration via Aggressor scripts for team server customization.
- **Detection Evasion**: Techniques designed to minimize logging and network artifacts.

## Installation

### Requirements

- Cobalt Strike 4.0 or later (commercial license required).
- Windows team server host (for running the C2).
- Basic knowledge of Aggressor scripting.
- Target: Windows systems with UAC enabled.

### Install Commands

1. Download the Elevate Kit scripts from the Cobalt Strike community or official resources.

```bash
# On Kali/Ubuntu (team server setup)
sudo apt update
sudo apt install cobaltstrike  # Assuming licensed installation

# Copy Elevate Kit to scripts directory
cp elevate-kit.cna /opt/cobaltstrike/scripts/
```

2. Start Cobalt Strike team server:

```bash
# Launch team server
./teamserver <IP> <password>
```

3. Load the kit in the Cobalt Strike client via Script Manager.

For macOS:

```bash
# Using Homebrew (if available, though CS is Java-based)
brew install --cask cobaltstrike  # Licensed only
```

## Basic Usage

```beacon
# In Beacon console after initial access
elevate uac
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show available elevate methods |
| `--method <name>` | Specify bypass technique (e.g., fodhelper, eventvwr) |
| `--verbose` | Enable detailed logging for troubleshooting |

## Examples

### Example 1: Basic UAC Bypass

Load the kit and elevate:

```aggressor
script-load elevate-kit.cna
```

Then in Beacon:

```beacon
elevate uac --method fodhelper
```

### Example 2: Spawn Elevated Process

After elevation:

```beacon
spawnas child powershell.exe -w hidden -nop
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Bypass User Account Control]] Bypass User Account Control: Simple Elevation
- [[Access Token Manipulation]] Access Token Manipulation: Token Impersonation/Theft
- [[Dynamic-link Library Injection]] Process Injection: Dynamic-link Library Injection

### Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- **Process Anomalies**: Look for cmd.exe or powershell.exe spawning from unusual parents (e.g., via Sysmon Event ID 1).
- **Registry Changes**: Modifications to HKCU\Environment or COM registrations (Event ID 13).
- **Network Artifacts**: Beacon C2 callbacks during elevation (Suricata rules for HTTP/SMB beacons).
- **Logging**: Enable UAC verbose logging and PowerShell transcription to capture script execution.
- **EDR Signatures**: YARA rules for known Elevate Kit strings or beacon DLLs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Cobalt-Strike]]
- [[tools/Mimikatz]]

## References

- Official Cobalt Strike Documentation: https://www.cobaltstrike.com/help-managing-payloads#elevate
- Community Scripts: https://github.com/rsmudge/cobalt-strike-pkgs (for Aggressor extensions)
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1548/002/
