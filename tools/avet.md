---
id: 39fbcdfa-d783-45f0-82c1-a173a1a8a320
name: avet
type: tool
verified: true
created_at: '2019-08-28T21:17:41.901209+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - evasion
  - antivirus-bypass
  - payload-generation
  - obfuscation
url: 'https://github.com/govolution/avet'
commands:
  - '[[commands/avet-generate-payload]]'
  - '[[commands/avet-encode-strings]]'
  - '[[commands/avet-build-executable]]'
validated: true
---

# avet

**Status**: Unverified

## Overview

AVET (AntiVirus Evasion Tool) is a Python-based framework designed to generate executable payloads that evade detection by antivirus software on Windows systems. It supports various evasion techniques including string encryption, API hashing, sleep masking, and code obfuscation, making it useful for red team operations and penetration testing where payload delivery needs to bypass endpoint protection.

## Description

AVET targets Windows machines by creating customized executables from templates and payloads. Users can select from pre-built templates or create custom ones to implement evasion strategies like dynamic function resolution to avoid static signatures. The tool is particularly effective against signature-based AV but may require iteration for machine-learning-based detectors. It's commonly used in post-exploitation phases to deliver reverse shells or implants without triggering alerts.

## Features

- Feature 1: Template-based payload generation with modular evasion modules (e.g., XOR encoding, base64 obfuscation)
- Feature 2: API hashing to resolve Windows APIs at runtime, reducing import table analysis
- Feature 3: Support for embedding arbitrary payloads (e.g., Meterpreter, custom shells) into benign-looking executables
- Feature 4: Icon customization and size optimization for stealthy delivery
- Feature 5: Cross-platform building (Linux host to Windows target)

## Installation

### Requirements

- Python 3.6+
- PyInstaller for executable building
- Git for cloning the repository

### Install Commands

```bash
# Clone the repository
git clone https://github.com/govolution/avet.git
cd avet

# Install dependencies
pip install -r requirements.txt

# For Kali/Ubuntu
sudo apt update && sudo apt install python3-pip pyinstaller

# For Windows (using WSL or native Python)
pip install pyinstaller
```

## Basic Usage

```bash
python avet.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -t, --template | Specify evasion template |
| -p, --payload | Input payload file |
| -o, --output | Output directory/file |
| --encode-strings | Enable string obfuscation |
| -b, --build | Build standalone executable |
| -i, --icon | Add custom icon to exe |

## Examples

### Example 1: Basic Usage

Generate a simple evaded payload:

```bash
python avet.py -t templates/basic.py -p payloads/shell.exe -o ./output
```

### Example 2: Advanced Usage

Build an obfuscated executable with icon:

```bash
python avet.py --encode-strings template.py -b -i icons/app.ico -o advanced_payload.exe
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[Process Injection]] Process Injection
- [[Hijack Execution Flow]] Hijack Execution Flow

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for PyInstaller-generated executables with unusual entropy (high due to obfuscation)
- Detection method 2: Behavioral analysis for runtime API resolution patterns or encoded strings in memory
- Detection method 3: File creation events for .pyc files or temporary build artifacts in user directories
- Detection method 4: Network callbacks from newly executed binaries to C2 servers

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: Veil-Evasion]]
- [[Related Tool: TheFatRat]]

## References

- Official GitHub: https://github.com/govolution/avet
- AVET Documentation: Included in repo README
- Related Resource: https://www.blackhillsinfosec.com/avet-antivirus-evasion-tool/
