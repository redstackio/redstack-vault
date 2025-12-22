---
id: 24834aa9-27d7-428b-9a3f-cbe103f4a1e5
type: tool
verified: true
created_at: '2019-08-28T21:17:23.010803+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - redteam
  - phishing
  - initial-access
  - deployment
url: 'https://github.com/example/ClickOnceGenerator'
validated: true
---

# ClickOnce-Generator

**Status**: Unverified

## Overview

ClickOnce-Generator is a red team tool for quickly creating malicious ClickOnce deployment packages. It generates Windows applications using Microsoft's ClickOnce technology, embedding a simple WebBrowser widget that automatically navigates to a user-specified URL. This is commonly used for phishing campaigns, social engineering, or delivering secondary payloads via trusted-looking app installations.

## Description

ClickOnce applications are signed .NET deployments that users can install with a single click from a web link or file share. The tool simplifies crafting these for offensive security by producing a minimal app that loads a browser control pointing to an attacker-controlled site, potentially leading to credential harvesting, malware download, or further exploitation. It's particularly effective against Windows environments where users trust legitimate-looking software updates.

## Features

- Feature 1: Generates complete ClickOnce packages (.application, manifests, and executable) with embedded WebBrowser navigation.
- Feature 2: Customizable app name, icon, and description to mimic legitimate software.
- Feature 3: Supports offline deployment via file shares or email attachments.
- Feature 4: Minimal footprint—no external dependencies beyond .NET Framework on the target.

## Installation

### Requirements

- PowerShell 5.0 or later
- .NET Framework 4.5+ (for building the app)
- Windows environment (tool is Windows-specific)

### Install Commands

```powershell
# Clone from repository (assuming GitHub source)
git clone https://github.com/example/ClickOnceGenerator.git
cd ClickOnceGenerator

# No further installation needed; run as PowerShell script
```

For Ubuntu/Kali (cross-compilation via Wine/Mono, not recommended for production):

```bash
# Install Wine and Mono
sudo apt update && sudo apt install wine mono-complete

# Download and run via Wine (experimental)
wget https://github.com/example/ClickOnceGenerator/archive/main.zip
unzip main.zip
wine ClickOnceGenerator.exe
```

## Basic Usage

```powershell
.\ClickOnceGenerator.ps1 -Help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and available parameters |
| -v, --verbose | Enable verbose output during package generation |
| -SignCert | Path to code-signing certificate for trusted appearance (optional) |

## Examples

### Example 1: Basic Usage

```powershell
.\ClickOnceGenerator.ps1 -Url "http://example.com/phish" -OutputPath "./deploy/"
```

This creates a basic package navigating to the phishing URL.

### Example 2: Advanced Usage

```powershell
.\ClickOnceGenerator.ps1 -Url "https://attacker.net/payload" -OutputPath "C:\Output\" -AppName "Security Update Tool" -SignCert "mycert.pfx"
```

This generates a signed package mimicking a security tool.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Malicious File]] User Execution: Malicious File |
- [[Credentials from Web Browsers]] Credentials from Web Browsers (via embedded browser) |

### Tactics

- [[Initial Access]] Initial Access |
- [[Execution]] Execution |

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for ClickOnce deployments via Windows Event Logs (Application log for .NET runtime events).
- Detection method 2: Signature-based detection on generated manifests containing WebBrowser controls or suspicious URLs.
- Detection method 3: Network monitoring for outbound connections from newly installed ClickOnce apps to unknown domains.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/MSBuild]]
- [[tools/DotNetToJScript]]

## References

- Official ClickOnce Documentation: https://learn.microsoft.com/en-us/dotnet/desktop/winforms/advanced/clickonce-security-and-deployment
- Related resources: Red Team notes on ClickOnce abuse in phishing campaigns
