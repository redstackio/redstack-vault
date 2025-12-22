---
id: 2594c73a-d7c5-430f-8d46-23c1c3cf1d70
type: tool
verified: true
created_at: '2019-08-28T21:17:38.835814Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - pdf-analysis
  - malware-analysis
  - obfuscation
  - javascript-analysis
url: 'https://github.com/jesparza/peepdf'
validated: true
---

# peepdf

**Status**: Unverified

## Overview

peepdf is a Python-based tool designed for comprehensive PDF file analysis to determine if a file is potentially harmful. It serves security researchers by consolidating multiple analysis tasks into one tool, enabling the inspection of PDF structures for malicious content such as embedded JavaScript, shellcode, or obfuscated elements. Commonly used in malware analysis, red teaming for crafting malicious PDFs, and defensive forensics.

## Description

peepdf provides detailed exploration of PDF internals, including object trees, streams, filters (e.g., FlateDecode, ASCIIHex), encodings, and support for various PDF versions, object streams, and encrypted files. With optional dependencies like PyV8 for JavaScript analysis and Pylibemu for shellcode emulation, it offers advanced capabilities. Beyond analysis, it supports creating new PDFs, modifying existing ones, and obfuscating content to evade detection—making it versatile for both offensive and defensive security operations.

## Features

- Feature 1: Static and interactive PDF parsing with object and stream decoding
- Feature 2: Support for filters, encodings, encryption, and multiple PDF versions
- Feature 3: JavaScript analysis (via PyV8) and shellcode emulation (via Pylibemu)
- Feature 4: PDF creation, modification, and obfuscation capabilities
- Feature 5: Report generation for suspicious elements like embedded executables or anomalies

## Installation

### Requirements

- Python 2.7 (or 3.x with compatibility adjustments)
- Optional: PyV8 for JavaScript analysis
- Optional: Pylibemu for shellcode emulation

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python2.7

# For Ubuntu/Kali
git clone https://github.com/jesparza/peepdf.git
cd peepdf

# Run directly (no install needed)
python peepdf.py --help

# Optional: Install PyV8 (Ubuntu/Debian)
sudo apt install python-v8

# Optional: Install Pylibemu (may require building from source)
git clone https://github.com/buffer/pylibemu.git
cd pylibemu && python setup.py install
```

For Windows: Use Git Bash or WSL, ensure Python 2.7 is in PATH.
For macOS: `brew install python@2` then clone and run.

## Basic Usage

```bash
python peepdf.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -f, --file | Perform static analysis on a PDF file |
| -i, --interactive | Launch interactive mode for exploration |
| -o, --output | Specify output file for reports or new PDFs |
| -j, --js | Enable JavaScript analysis (requires PyV8) |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Static analysis of a PDF:

```bash
python peepdf.py -f sample.pdf
```

### Example 2: Advanced Usage

Interactive mode with JS analysis:

```bash
python peepdf.py -i -j malicious.pdf
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Documents (for PDF obfuscation and analysis)
- [[JavaScript]] JavaScript (for embedded JS detection and creation)
- [[Malicious File]] User Execution: Malicious File (analyzing PDFs that trigger exploits)

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Process monitoring for `peepdf.py` executions or Python scripts accessing PDF files
- Detection method 2: File system changes: New or modified PDFs in temp directories
- Detection method 3: Network: If analyzing network-delivered PDFs, log downloads followed by Python analysis
- Detection method 4: Optional deps like PyV8 or Pylibemu installations as prerequisites

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/pdfid]]
- [[qpdf]]
- [[Origami]]

## References

- Official GitHub: https://github.com/jesparza/peepdf
- Documentation: Included in repo README
- Related resources: MITRE ATT&CK for PDF techniques
