---
id: 3cd4a6d9-5f2f-44d2-a8f6-a3482171d98e
name: WePWNise
type: tool
verified: true
created_at: '2019-08-28T21:17:28.880157+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - office-macro
  - vba
  - bypass
  - amsi
  - emet
url: 'https://github.com/byt3bl33d3r/WePWNise'
validated: true
---

# WePWNise

**Status**: Unverified

## Overview

WePWNise is a Python-based tool for generating architecture-independent VBA (Visual Basic for Applications) code designed for use in Microsoft Office documents or templates. It automates the creation of code that bypasses application control mechanisms and exploit mitigation software, such as AMSI (Antimalware Scan Interface) and EMET (Enhanced Mitigation Experience Toolkit), enabling the execution of malicious macros in Office environments.

Common use cases include red teaming operations involving phishing attachments, macro-based payloads, and testing Office security controls.

## Description

WePWNise simplifies the development of malicious Office macros by generating obfuscated VBA code that evades common defenses. It supports embedding shellcode, custom payloads, and specific bypass techniques. The tool is particularly useful for cross-architecture compatibility (x86/x64) and can target Word, Excel, or PowerPoint documents. It does not require compilation and produces ready-to-use VBA modules that can be inserted into .docm, .xlsm, or .pptm files.

Key capabilities include AMSI patching, EMET evasion, API unhooking, and shellcode execution via reflective loading techniques.

## Features

- Feature 1: Architecture-independent VBA generation for x86 and x64 Office versions
- Feature 2: Automated bypasses for AMSI, EMET, and other mitigations
- Feature 3: Support for embedding custom shellcode or payloads (e.g., reverse shells)
- Feature 4: Obfuscation options to evade static analysis
- Feature 5: Output in formats compatible with Office macro editors

## Installation

### Requirements

- Python 2.7 or 3.x
- Git
- Windows environment for testing (Kali/Ubuntu for generation)

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python3 -y
git clone https://github.com/byt3bl33d3r/WePWNise.git
cd WePWNise
# No additional installation needed; run directly with Python
```

For Kali Linux: The tool is not pre-installed; follow the clone steps above.

For Ubuntu: Same as Kali; ensure Python is available.

## Basic Usage

```python
python wepwnise.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -o, --output | Specify output file for generated VBA |
| --word | Generate for Microsoft Word |
| --excel | Generate for Microsoft Excel |
| --amsi-bypass | Include AMSI evasion code |
| --emet-bypass | Include EMET evasion code |
| --shellcode | Embed provided shellcode (hex format) |

## Examples

### Example 1: Basic Usage

Generate a basic bypass macro for Word:

```python
python wepwnise.py --output basic_macro.vba --word
```

### Example 2: Advanced Usage

Generate a reverse shell with bypasses:

```python
python wepwnise.py --output shell_macro.vba --word --amsi-bypass --shellcode 'fc488d...'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Visual Basic]] Visual Basic
- [[Registry Run Keys - Startup Folder]] Registry Run Keys / Startup Folder
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Execution]] Execution
- [[Persistence]] Persistence
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for VBA macro generation tools or unusual Python processes accessing Office files
- Detection method 2: Enable Office macro logging and scan for AMSI/EMET bypass patterns in VBA code (e.g., AmsiScanBuffer patches)
- Detection method 3: Behavioral analysis of Office apps spawning network connections or child processes from macros
- Detection method 4: File integrity monitoring on .docm/.xlsm files for embedded shellcode

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Metasploit]]
- [[MacroPack]]

## References

- Official GitHub: https://github.com/byt3bl33d3r/WePWNise
- Related resources: Microsoft Office macro security documentation
