---
id: e022464a-76f3-47b6-acf7-77a771f56caf
name: Meta-Twin
type: tool
verified: true
created_at: '2019-08-28T21:17:24.022373+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - evasion
  - metadata
  - signature-cloning
url: 'https://example.com/meta-twin'
validated: true
---

# Meta-Twin

**Status**: Unverified

## Overview

Meta-Twin is a specialized tool designed for file resource cloning in security testing. It extracts metadata, including digital signatures, from one file and injects it into another, enabling the creation of files that mimic legitimate ones to evade detection mechanisms.

## Description

Meta-Twin operates by parsing file structures (e.g., PE for Windows executables) to isolate metadata components such as timestamps, certificates, and Authenticode signatures. This is particularly useful in red team operations for obfuscating malicious payloads by applying signatures from trusted sources, potentially bypassing signature-based antivirus detection. The tool supports both extraction and injection workflows, making it a key asset for defense evasion techniques.

## Features

- Feature 1: Metadata extraction from various file formats (PE, ELF, etc.)
- Feature 2: Digital signature cloning and injection without altering core file functionality
- Feature 3: Support for verification of injected signatures to ensure validity
- Feature 4: Batch processing for multiple files
- Feature 5: Output in JSON or binary formats for flexibility

## Installation

### Requirements

- Python 3.6+ (if script-based) or compiled binary
- Libraries: cryptography, pefile (for PE handling)
- Administrative privileges for signature operations on Windows

### Install Commands

```bash
# Clone from repository (assuming GitHub source)
git clone https://github.com/example/meta-twin.git
cd meta-twin

# Install dependencies (Python version)
pip install -r requirements.txt

# Or download pre-built binary for Windows/Linux
wget https://example.com/meta-twin-binary.zip
unzip meta-twin-binary.zip
chmod +x meta-twin
```

For Kali/Ubuntu:
```bash
sudo apt update
sudo apt install python3-pip git
# Then follow clone steps above
```

## Basic Usage

```bash
meta-twin --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output for debugging |
| --format json/binary | Specify output format for metadata |

## Examples

### Example 1: Basic Usage

Extract and inject metadata:
```bash
meta-twin extract --source legit.exe --output meta.json
meta-twin inject --target malicious.exe --metadata meta.json
```

### Example 2: Advanced Usage

Full clone operation:
```bash
meta-twin clone --source signed_driver.sys --target payload.sys --output ./cloned/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[Subvert Trust Controls]] Subvert Trust Controls

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual file modifications involving signature tampering (e.g., via Sysmon Event ID 11 on Windows)
- Detection method 2: Analyze file metadata inconsistencies, such as mismatched timestamps or signatures from unrelated sources
- Detection method 3: Process monitoring for meta-twin executable or Python scripts accessing PE/ELF headers

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Resource-Hacker]]
- [[tools/SignTool]]

## References

- Official documentation: https://example.com/meta-twin/docs
- Related resources: MITRE ATT&CK on Defense Evasion
