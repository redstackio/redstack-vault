---
type: tool
verified: true
description: >-
  Fully customizable Windows-based security distribution for malware analysis,
  incident response, penetration testing, and reverse engineering.
url: 'https://github.com/fireeye/flare-vm'
platforms:
  - Windows
tags:
  - malware-analysis
  - reverse-engineering
  - incident-response
  - penetration-testing
  - hacking
  - operating-systems
commands:
  - '[[commands/set-executionpolicy-unrestricted]]'
category: Security Distribution
validated: true
---

# Flare VM

**Status**: ✓ Verified

## Overview

Flare VM is a fully customizable Windows-based security distribution designed for malware analysis, incident response, penetration testing, reverse engineering, and other cybersecurity tasks. It is installed on top of a fully updated Windows 10 virtual machine using a PowerShell script. Flare VM includes popular tools such as debuggers (x64dbg, OllyDbg, WinDbg), disassemblers (Cutter, Ghidra), malware dumping tools, and more. It provides a comprehensive environment for offensive and defensive security operations on Windows.

## Description

Flare VM transforms a standard Windows 10 VM into a specialized security lab by automating the installation of dozens of tools and utilities. It supports customization through a configuration file, allowing users to select specific packages for their needs. Common use cases include dissecting malware samples, debugging exploits, analyzing network traffic, and conducting forensic investigations. The distribution ensures tools are pre-configured and compatible, reducing setup time for security professionals.

## Features

- Automated installation of 100+ security tools via PowerShell scripting
- Support for debuggers, disassemblers, and decompilers (e.g., x64dbg, Ghidra, IDA Pro Free)
- Integration with malware analysis frameworks and utilities (e.g., Volatility, REMnux tools)
- Customizable package selection for tailored environments
- Checkpoint-friendly design for safe experimentation with potentially malicious content
- Built-in support for scripting and automation in PowerShell and Python

## Installation

### Requirements

- A fully up-to-date Windows 10 virtual machine (64-bit recommended)
- 60 GB free hard drive space (150-200 GB if installing multiple Visual Studio builds)
- 3+ CPU cores
- 4 GB RAM (8 GB+ recommended for heavy analysis)
- Virtualization software (e.g., VMware, VirtualBox)
- Administrative privileges on the VM

### Install Commands

1. Create a new Windows 10 VM and apply all available updates.

2. Disable Windows Defender Tamper Protection. Refer to [Microsoft documentation](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/prevent-changes-to-security-settings-with-tamper-protection) for instructions.

3. Download the Flare VM installation script from GitHub:

   ```powershell
   Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mandiant/flare-vm/master/install.ps1" -OutFile "install.ps1"
   ```

4. Open PowerShell as Administrator and set the execution policy to allow script execution using [[commands/set-executionpolicy-unrestricted]].

5. Create a VM checkpoint before running the installer to enable rollback if needed.

6. Execute the installation script:

   ```powershell
   .\install.ps1
   ```

The installation process will prompt for configuration options, download and install packages, and may require multiple restarts. It typically takes 1-2 hours depending on hardware and selected packages. After completion, create another checkpoint as a clean restore point.

## Basic Usage

Once installed, Flare VM provides a desktop environment with shortcuts to all tools. Launch tools from the Start menu or command line. For example, to start Ghidra:

```powershell
& "C:\Program Files\Ghidra\ghidraRun.bat"
```

Use the Flare-VM GitHub repository for configuration tweaks and troubleshooting.

### Common Options

Flare VM uses a JSON configuration file (user_config.json) for customization:

| Option | Description |
|--------|-------------|
| `install_tools` | Array of tools to install (e.g., ["ghidra", "x64dbg"]) |
| `chocolatey_packages` | List of Chocolatey packages to include |
| `visual_studio_builds` | Specify VS versions for compilation support |

## Examples

### Example 1: Basic Installation

Run the default installer to get the full set of tools:

```powershell
.\install.ps1 -Verbose
```

### Example 2: Custom Installation

Edit user_config.json to install only reverse engineering tools, then run:

```powershell
.\install.ps1 -ConfigurationPath .\user_config.json
```

## Related Commands

- [[commands/set-executionpolicy-unrestricted]]

## References

- [Official GitHub Repository](https://github.com/mandiant/flare-vm)
- [Installation Script](https://github.com/mandiant/flare-vm/blob/master/install.ps1)
- [Microsoft Tamper Protection Docs](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/prevent-changes-to-security-settings-with-tamper-protection)
