---
id: c35f0faf-aee8-45d7-8da9-c4e0cbdb549b
type: tool
verified: true
description: >-
  A tool for converting PowerShell Empire launcher profiles into Apache
  mod_rewrite scripts to enable web-based payload delivery.
url: 'https://github.com/EmpireProject/Empire'
created_at: '2019-08-28T21:17:39.539451+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
  - Linux
  - macOS
tags:
  - empire
  - modrewrite
  - apache
  - payload-delivery
  - obfuscation
commands:
  - '[[commands/e2modrewrite-generate-htaccess]]'
category: Post-Exploitation
validated: true
---

# e2modrewrite

**Status**: Unverified

## Overview

e2modrewrite is a utility designed to convert launcher profiles from PowerShell Empire—a post-exploitation framework—into Apache mod_rewrite rules. This allows attackers to host Empire stagers (initial payload launchers) on a web server, using URL rewriting to obfuscate and deliver payloads dynamically. It's commonly used in red team operations to evade detection by serving payloads that appear as normal web requests, supporting techniques like ingress tool transfer and command execution in web environments.

## Description

e2modrewrite automates the transformation of Empire's profile files (which define stager configurations such as HTTP/HTTPS listeners, PowerShell download cradles, etc.) into .htaccess-compatible mod_rewrite directives. Once generated, these rules can be placed on an Apache server to route specific URLs to actual stager scripts, enabling stealthy payload delivery over HTTP. The tool is particularly useful for scenarios involving web server compromise or controlled C2 infrastructure, where direct file serving might trigger alerts. It integrates with Empire's ecosystem for generating diverse stagers (e.g., PowerShell, batch, Python) and supports customization for evasion.

## Features

- Feature 1: Parses Empire profile files to extract stager URLs and scripts.
- Feature 2: Generates mod_rewrite rules that map friendly URLs to obfuscated payloads.
- Feature 3: Supports multiple profile formats and output customization for different Apache configurations.
- Feature 4: Integrates with Empire workflows for automated C2 setup.

## Installation

### Requirements

- PowerShell 3.0 or later (cross-platform support via PowerShell Core).
- Apache HTTP Server with mod_rewrite enabled.
- PowerShell Empire installed (for profile generation).

### Install Commands

```powershell
# Clone Empire repository (e2modrewrite is included in Empire's lib/modules)
git clone https://github.com/EmpireProject/Empire.git
cd Empire
.\\setup\\install.ps1

# Alternatively, download the script directly if standalone
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/EmpireProject/Empire/master/lib/e2modrewrite.ps1" -OutFile "e2modrewrite.ps1"
```

For Linux/macOS (using PowerShell Core):

```bash
# Install PowerShell Core
sudo apt update && sudo apt install -y powershell

# Clone Empire
git clone https://github.com/EmpireProject/Empire.git
cd Empire
pwsh ./setup/install.ps1
```

## Basic Usage

```powershell
Get-Help .\e2modrewrite.ps1
```

### Common Options

| Option | Description |
|--------|-------------|
| -ProfileFile | Specifies the input Empire profile file |
| -OutFile | Specifies the output .htaccess file |
| -h, --help | Show help message |
| -v, --verbose | Enable verbose logging during conversion |

## Examples

### Example 1: Basic Usage

Convert a simple Empire profiles file to .htaccess:

```powershell
.\e2modrewrite.ps1 -ProfileFile profiles.txt -OutFile .htaccess
```

This reads Empire stager profiles and outputs rewrite rules for an Apache web root.

### Example 2: Advanced Usage

Generate rules with verbose output for a JSON profile:

```powershell
.\e2modrewrite.ps1 -ProfileFile stagers.json -OutFile web/.htaccess -Verbose
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Execution]] Execution
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of unusual .htaccess files with mod_rewrite rules pointing to PowerShell or encoded scripts.
- Detection method 2: Web server logs showing rewritten URLs serving non-standard payloads (e.g., .ps1 disguised as images).
- Detection method 3: Empire-related processes or network callbacks from converted stagers.

## Related Procedures

- Procedures using this tool for web-based Empire deployment can be found in the procedures folder.

## Related Tools

- [[tools/PowerShell-Empire]]
- [[tools/Apache-HTTP-Server]]

## References

- Official Empire GitHub: https://github.com/EmpireProject/Empire
- Apache mod_rewrite documentation: https://httpd.apache.org/docs/current/mod/mod_rewrite.html
- Blog post on Empire stagers: https://www.harmj0y.net/blog/powershell/going-nuclear-with-empire-stagers/
