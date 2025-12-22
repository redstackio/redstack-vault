---
id: 6c6c4b39-43d5-4f46-ba59-0db0cd6501fd
name: make-pdf-embedded
type: tool
verified: true
created_at: '2019-08-28T21:17:20.762028+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - pdf-manipulation
  - evasion
  - steganography
  - red-team
url: 'https://github.com/example/make-pdf-embedded'
validated: true
---

# make-pdf-embedded

**Status**: Unverified

## Overview

make-pdf-embedded is a Python-based utility for embedding arbitrary files into PDF documents. It is commonly used in offensive security testing to hide payloads within seemingly benign PDFs, aiding in evasion of antivirus detection and facilitating social engineering attacks like phishing campaigns.

## Description

The tool modifies PDF structures to insert binary data (e.g., executables, scripts, or other files) as embedded objects or attachments. This allows red teams to deliver malicious content disguised as legitimate documents. It supports basic obfuscation options to make extraction more difficult. Primarily used in post-exploitation or initial access phases where document-based vectors are effective.

## Features

- Feature 1: Embed any file type into PDF streams or attachments
- Feature 2: Optional obfuscation to hide embedded data from simple scanners
- Feature 3: Support for batch processing multiple PDFs
- Feature 4: Extraction verification mode to test embedded content integrity

## Installation

### Requirements

- Python 3.6+
- pip and git
- Libraries: PyPDF2 or pdfminer for PDF handling

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/example/make-pdf-embedded.git
cd make-pdf-embedded

# Install dependencies
pip install -r requirements.txt

# For Kali/Ubuntu
sudo apt update && sudo apt install python3-pip git
pip3 install PyPDF2
```

## Basic Usage

```bash
python make_pdf_embedded.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-o, --obfuscate` | Apply basic obfuscation to embedded data |
| `-v, --verbose` | Enable verbose output for debugging |
| `-e, --extract` | Mode to extract and verify embedded files |

## Examples

### Example 1: Basic Usage

Embed a file into a PDF:

```bash
python make_pdf_embedded.py report.pdf payload.exe output.pdf
```

### Example 2: Advanced Usage

Embed with obfuscation:

```bash
python make_pdf_embedded.py -o report.pdf script.js obfuscated_output.pdf
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[T1566.001]] Phishing: Spearphishing Attachment

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual PDF file modifications using tools like pdfid or qpdf
- Detection method 2: Scan for embedded objects with antivirus or EDR solutions (e.g., YARA rules for PDF anomalies)
- Detection method 3: Network logs showing PDF downloads followed by execution of embedded payloads

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PyPDF2]]
- [[tools/binwalk]]
- [[tools/pdf-parser]]

## References

- Official documentation: https://github.com/example/make-pdf-embedded
- Related resources: MITRE ATT&CK on Obfuscated Files (T1027)

*Last updated: 2023-10-01T00:00:00+00:00*
