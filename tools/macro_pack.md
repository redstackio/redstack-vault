---
id: d032e2d6-37ed-403b-bb22-2765b6fa860d
type: tool
verified: true
description: >-
  Tool for automating the obfuscation and generation of Microsoft Office macros,
  VBScripts, and other formats for penetration testing and social engineering.
url: 'https://github.com/emericnasi/macro_pack'
created_at: '2019-08-28T21:17:31.474341+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - macro
  - obfuscation
  - office
  - vbs
  - pentest
  - social-engineering
validated: true
---

# macro_pack

**Status**: Unverified

## Overview

macro_pack is a Python-based tool developed by @EmericNasi for generating and obfuscating malicious payloads in formats like Microsoft Office macros (VBA), VBScripts, HTA files, and more. It is primarily used in penetration testing, red team operations, and social engineering assessments to create evasive documents that can deliver payloads while bypassing basic security controls.

## Description

The tool automates the process of creating obfuscated code snippets that can be embedded in Office documents or scripts. It supports multiple output formats and includes built-in obfuscation techniques to make the payloads harder to detect by antivirus software or static analysis. Common use cases include phishing campaigns where users are tricked into enabling macros in Word/Excel files, or delivering scripts via email attachments.

## Features

- Feature 1: Generation of Office macros (Excel, Word) with embedded payloads
- Feature 2: Obfuscation of VBScripts, JavaScript, and HTA files
- Feature 3: Custom payload injection and variable renaming for evasion
- Feature 4: Support for multiple output formats including .xlsm, .docm, .vbs
- Feature 5: Preset templates for common pentest scenarios

## Installation

### Requirements

- Python 3.6+
- pip package manager

### Install Commands

```bash
# Clone from GitHub
sudo apt update && sudo apt install git python3-pip -y
git clone https://github.com/emericnasi/macro_pack.git
cd macro_pack
pip3 install -r requirements.txt

# Or install via pip (if available)
pip3 install macro-pack
```

For Kali Linux, it may require additional dependencies like `python3-impacket` for advanced features.

## Basic Usage

```python
macro_pack --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -g, --generate | Specify generation type (1=Office, 2=VBS, etc.) |
| -o, --output | Output file path |
| -l, --list | List available presets |
| --payload | Custom payload to embed |
| -O, --obfuscate | Apply obfuscation level (1-3) |

## Examples

### Example 1: Basic Usage - Generate Office Macro

```python
macro_pack -g 1 -o payload.xlsm
```

This creates an obfuscated Excel macro file with a default payload.

### Example 2: Advanced Usage - Generate Obfuscated VBS with Custom Payload

```python
macro_pack -g 2 -o payload.vbs --payload "CreateObject(\"WScript.Shell\").Run \"calc.exe\""
```

This embeds a calculator launcher in an obfuscated VBScript.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment
- [[Malicious File]] User Execution: Malicious File
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Python processes spawning Office applications or script interpreters
- Detection method 2: Signature-based detection of obfuscated VBA strings in Office files
- Detection method 3: Behavioral analysis of macro-enabled documents from untrusted sources
- Detection method 4: EDR alerts on file creation of .xlsm/.vbs with suspicious content

## Related Procedures

- [[procedures/Generate-Obfuscated-Macro-Payload]]
- [[procedures/Deliver-Phishing-with-Macro]]

## Related Tools

- [[tools/metasploit]]
- [[tools/Empire]]

## References

- Official GitHub: https://github.com/emericnasi/macro_pack
- Documentation: Included in repo README
- Related: Office Macro Malware Analysis guides
