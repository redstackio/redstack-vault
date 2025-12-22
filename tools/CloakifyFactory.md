---
type: tool
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - obfuscation
  - evasion
  - data-exfiltration
  - dlp-bypass
url: 'https://github.com/megabeets/Cloakify'
validated: true
---

# CloakifyFactory

**Status**: Unverified

## Overview

CloakifyFactory is a Python-based tool for generating custom ciphers used in the Cloakify toolset. It enables the creation of obfuscation schemes that disguise sensitive data as innocuous text, such as tweets, recipes, or product descriptions, to evade data loss prevention (DLP) systems, multi-layer security (MLS) devices, antivirus (AV) detection, and data whitelisting controls. Commonly used in red team operations for data exfiltration and infiltration in plain sight, as well as social engineering scenarios to mislead analysts.

## Description

The Cloakify toolset, with CloakifyFactory at its core for cipher generation, transforms payloads or exfiltrated data into formats that appear harmless. For example, command-and-control traffic or stolen credentials can be encoded to look like everyday web content. This tool is particularly useful in environments with strict monitoring, allowing attackers to bypass filters by making data indistinguishable from normal traffic. It supports a variety of disguise templates and can be chained with the companion Cloakify encoder/decoder for full obfuscation workflows.

## Features

- Generate custom ciphers from predefined disguise templates (e.g., Twitter posts, IKEA instructions, Bible verses).
- List available disguise formats for selection.
- Support for creating reusable cipher files compatible with Cloakify encoder/decoder.
- Cross-platform compatibility via Python 3.
- No external dependencies beyond standard Python libraries.

## Installation

### Requirements

- Python 3.6 or higher.
- Git for cloning the repository.

### Install Commands

```bash
# Clone the repository
git clone https://github.com/megabeets/Cloakify.git
cd Cloakify/CloakifyFactory

# No formal installation needed; run directly with Python
python3 CloakifyFactory.py --help
```

On Windows, use `python` instead of `python3` if Python is in PATH. The tool is a standalone script and does not require pip installations.

## Basic Usage

```bash
python3 CloakifyFactory.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage. |
| `-C` | Create a new cipher file. |
| `-L` | List available disguise templates. |
| `-o <file>` | Output file for the generated cipher. |

## Examples

### Example 1: Basic Usage - List Disguises

```bash
python3 CloakifyFactory.py -L
```

This lists all available disguise formats, such as 'twitter', 'ikea', 'bible', etc.

### Example 2: Advanced Usage - Generate a Cipher

```bash
python3 CloakifyFactory.py -C -o my_cipher.txt
```

Follow the interactive prompts to select a disguise template and generate a cipher file for use with Cloakify.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[Archive Collected Data]] Archive Collected Data

### Tactics

- [[Exfiltration]] Exfiltration
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of CloakifyFactory.py or generated .txt cipher files in unusual locations.
- Python processes executing obfuscation scripts with high entropy output.
- Network traffic containing disguised payloads (e.g., text resembling social media posts but with anomalous patterns).
- Log analysis for Python script executions involving file I/O with cipher-like names.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Cloakify]] (Companion encoder/decoder for generated ciphers)
- [[Base64]] (Basic encoding alternative)

## References

- Official GitHub Repository: https://github.com/megabeets/Cloakify
- Cloakify Toolset Documentation: Included in repo README
- Related Blog Post: Search for "Cloakify data exfiltration" for usage examples
