---
id: e4bb8ac1-3b57-4b1f-80fd-0717fb19d5d5
name: GreatSCT
type: tool
verified: true
created_at: '2019-08-28T21:17:42.996228+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
  - Linux
tags:
  - defense-evasion
  - powershell
  - payload-generation
  - application-whitelist-bypass
  - red-team
  - blue-team
url: 'https://github.com/GreatSCT/GreatSCT'
validated: true
---

# GreatSCT

**Status**: Unverified

## Overview

GreatSCT (Great Security Constraint Tool) is an open-source Python-based tool designed to generate PowerShell payloads that bypass application whitelisting restrictions, such as those enforced by AppLocker or Windows Defender Application Control. It is useful for both red teamers to simulate attacks and blue teams to test and understand bypass techniques. The tool creates executable scripts leveraging signed Microsoft binaries to proxy malicious actions without direct execution of unsigned code.

## Description

GreatSCT automates the creation of obfuscated PowerShell scripts that chain together trusted system utilities (e.g., regsvr32.exe, mshta.exe) to achieve code execution in locked-down environments. Common use cases include generating reverse shells, downloading additional payloads, or executing simple binaries like calc.exe. It supports integration with Metasploit for advanced payloads and provides options for various bypass methods. The tool is particularly valuable in penetration testing for evading endpoint detection and response (EDR) tools that rely on signature-based whitelisting.

## Features

- Feature 1: Interactive menu for selecting payload types (e.g., Calculator, Meterpreter, EXE execution).
- Feature 2: Generation of signed binary proxy executions using tools like bitsadmin, certutil, and rundll32.
- Feature 3: Support for custom payloads and integration with external frameworks like PowerShell Empire or Metasploit.
- Feature 4: Output in PowerShell script format (.ps1) ready for delivery via phishing or initial access vectors.
- Feature 5: Blue team mode for generating test payloads to validate whitelisting policies.

## Installation

### Requirements

- Python 2.7 or 3.x (tool is compatible with both, but Python 3 recommended).
- Git for cloning the repository.
- Access to a Linux (Kali/Ubuntu) or Windows environment for running the tool.

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/GreatSCT/GreatSCT.git

# Navigate to the directory
cd GreatSCT

# No further installation needed; run directly with Python
python --version  # Ensure Python is installed
```

On Windows, use the same commands in PowerShell or Command Prompt. For Kali Linux, git and python3 are pre-installed.

## Basic Usage

```bash
tool-name --help
```

GreatSCT does not have a --help flag; it launches an interactive menu upon execution.

### Common Options

| Option | Description |
|--------|-------------|
| None (Interactive) | Launches the main menu for payload selection. |
| Piping input | Allows automation of menu choices (e.g., echo 1 | python GreatSCT.py). |

## Examples

### Example 1: Basic Usage

```bash
python GreatSCT.py
```

This starts the interactive menu. Select a number (e.g., 1 for Calculator) to generate a payload.

### Example 2: Advanced Usage

```bash
(echo 2; echo y; echo /path/to/output.ps1) | python GreatSCT.py
```

This automates selection of a Meterpreter payload, confirms, and specifies output path.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Signed Binary Proxy Execution]] Signed Binary Proxy Execution
- [[PowerShell]] PowerShell
- [[Execution through API]] Native API

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual PowerShell executions chaining signed binaries (e.g., regsvr32 spawning cmd.exe) via Sysmon or EDR logs.
- Detection method 2: File creation of .ps1 scripts with obfuscated download cradles; scan for GreatSCT-generated patterns like IEX(New-Object Net.WebClient).
- Detection method 3: Network traffic to known payload hosts during generation/testing; block or alert on PowerShell downloads from untrusted sources.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[PowerShell Empire]]
- [[Metasploit]]

## References

- Official GitHub Repository: https://github.com/GreatSCT/GreatSCT
- Related Resources: PowerShell obfuscation guides and AppLocker bypass research.
