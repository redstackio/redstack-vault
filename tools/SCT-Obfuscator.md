---
id: 05fd5182-e035-4f08-aad7-f0531e3522e8
name: SCT Obfuscator
type: tool
verified: true
created_at: '2019-08-28T21:17:32.595515+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - obfuscation
  - cobalt-strike
  - evasion
  - payload
url: 'https://github.com/outflanknl/SCT-Obfuscator'
validated: true
---

# SCT-Obfuscator

**Status**: Unverified

## Overview

SCT-Obfuscator is a specialized tool for obfuscating Cobalt Strike SCT (Scriptlet) payloads. It is primarily used in red team operations to modify beacon payloads, making them harder for antivirus software, EDR systems, and signature-based detection to identify. The tool applies transformations to the scriptlet code without altering its functionality, enabling stealthier payload delivery via methods like regsvr32.exe execution.

## Description

Cobalt Strike's SCT payloads are XML-based scriptlets that can be executed by Windows via the regsvr32 command. However, these payloads often contain detectable strings and patterns. SCT-Obfuscator automates the process of encoding strings, randomizing variable names, inserting junk code, and restructuring control flow to create variants that bypass common defenses. It is particularly useful in post-exploitation scenarios where payload execution needs to evade behavioral analysis.

## Features

- Feature 1: String encoding (Base64, hex, etc.) to hide payload artifacts
- Feature 2: Variable and function name randomization for polymorphism
- Feature 3: Control flow obfuscation to complicate static analysis
- Feature 4: Support for multiple obfuscation levels (light, medium, high)
- Feature 5: Batch processing for multiple SCT files

## Installation

### Requirements

- Python 3.6+
- Git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/outflanknl/SCT-Obfuscator.git
cd SCT-Obfuscator

# Install dependencies
pip install -r requirements.txt
```

On Kali Linux or Ubuntu, ensure Python is installed: `sudo apt update && sudo apt install python3-pip git`.

## Basic Usage

```bash
python sctobfuscator.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output for debugging |
| --level | Set obfuscation level (low, medium, high) |
| --encode-strings | Apply string encoding transformations |

## Examples

### Example 1: Basic Usage

```bash
python sctobfuscator.py original.sct -o obfuscated.sct
```

This applies default obfuscation to `original.sct` and saves the result to `obfuscated.sct`.

### Example 2: Advanced Usage

```bash
python sctobfuscator.py original.sct -o obfuscated.sct --level high --encode-strings --randomize-vars
```

This uses high-level obfuscation with string encoding and variable randomization.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[T1027.010]] Command Obfuscation

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of modified SCT files with unusual encoding patterns in scriptlet XML
- Detection method 2: Regsvr32.exe spawning processes with obfuscated payloads (monitor via Sysmon Event ID 1)
- Detection method 3: Python processes executing sctobfuscator.py in temporary directories
- Detection method 4: Network callbacks from Cobalt Strike beacons post-obfuscation

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Cobalt-Strike]]
- [[tools/Invoke-Obfuscation]]

## References

- Official GitHub: https://github.com/outflanknl/SCT-Obfuscator
- Cobalt Strike Documentation: https://www.cobaltstrike.com/help-metasploit
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1027/
