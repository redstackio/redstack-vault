---
id: 129c0d3d-455e-4861-b166-9faf9dfa4f99
name: dont-kill-my-cat
type: tool
verified: true
created_at: '2019-08-28T21:17:41.142586+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - evasion
  - shellcode
  - polyglot
  - obfuscation
url: 'https://github.com/MicahBrock/dont-kill-my-cat'
commands:
  - '[[commands/dont-kill-my-cat-generate-polyglot]]'
validated: true
---

# dont-kill-my-cat

**Status**: Unverified

## Overview

Don't Kill My Cat is a Python-based tool for generating polyglot image files that embed obfuscated shellcode. The output is a fully valid image file (such as PNG or JPEG) that can also function as executable shellcode, enabling stealthy delivery of payloads in offensive security operations, particularly for bypassing signature-based detection in file uploads or transfers.

## Description

The tool takes raw shellcode as input and embeds it into an image format using steganographic-like techniques, ensuring the file passes validation as both an image and malicious code. It's commonly used in red teaming for evading antivirus detection during initial access or lateral movement phases. Supports common shellcode formats for Windows and Linux architectures.

## Features

- Feature 1: Generates polyglot PNG, JPEG, and BMP files with embedded shellcode
- Feature 2: Obfuscates shellcode to reduce detection rates
- Feature 3: Validates both image integrity and shellcode executability post-generation
- Feature 4: Supports custom image templates for blending payloads

## Installation

### Requirements

- Python 3.6+
- Pillow library for image manipulation
- Basic shellcode generation tools (e.g., msfvenom for creating input shellcode)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/MicahBrock/dont-kill-my-cat.git
cd dont-kill-my-cat

# Install dependencies
pip install -r requirements.txt

# For development, install in editable mode
pip install -e .
```

On Kali Linux, ensure Python and git are available via `apt update && apt install python3-pip git`.

## Basic Usage

```bash
python dont_kill_my_cat.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-v, --verbose` | Enable verbose output for debugging |
| `--format PNG` | Specify output image format (default: PNG) |

## Examples

### Example 1: Basic Usage

Generate a polyglot PNG from a shellcode file:

```bash
python dont_kill_my_cat.py reverse_shell.bin output.png
```

This creates `output.png`, which can be viewed in an image editor and executed as shellcode.

### Example 2: Advanced Usage

With verbose output and specific format:

```bash
python dont_kill_my_cat.py --verbose --format JPEG windows_payload.bin stealth.jpg
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Binary Padding]] Binary Padding (for obfuscation in images)
- [[NTFS File Attributes]] Hidden Files and Directories (via polyglot evasion)

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: File entropy analysis on images showing unusually high randomness (indicative of embedded binary data)
- Detection method 2: YARA rules scanning for polyglot signatures or shellcode patterns in image files
- Detection method 3: Behavioral monitoring for image files being executed as binaries

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/msfvenom]]
- [[tools/Steghide]]

## References

- Official GitHub Repository: https://github.com/MicahBrock/dont-kill-my-cat
- Related resources: Polyglot file techniques in evasion research
