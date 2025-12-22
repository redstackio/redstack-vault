---
id: c506ef11-6f25-43d7-9ce1-7adac0780f01
name: pdfid
type: tool
verified: true
created_at: '2019-08-28T21:17:32.768913+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - pdf-analysis
  - malware-detection
  - document-inspection
url: 'https://didierstevens.com/files/software/pdfid_v0_4_11.zip'
validated: true
---

# pdfid

**Status**: Unverified

## Overview

pdfid is a specialized tool for scanning PDF documents to detect potentially malicious or exploitable features by counting specific keywords and structures. Commonly used in offensive security for triaging PDFs that may contain JavaScript, embedded executables, or auto-execution actions during phishing or malware analysis operations.

## Description

pdfid is not a full PDF parser but a lightweight scanner that identifies keywords like /JS, /OpenAction, /EmbeddedFile, and others indicative of advanced PDF features that could be abused for exploitation. It handles obfuscated names and is designed for simplicity to avoid parsing vulnerabilities. Use it as a first-pass filter before deeper analysis with tools like pdf-parser. In red teaming, it's valuable for assessing document-based attack vectors, such as crafting or inspecting weaponized PDFs for social engineering campaigns.

## Features

- Keyword counting for PDF structures (/obj, /stream, /JS, /AA, etc.)
- Detection of obfuscated elements
- Recursive directory scanning
- Stream extraction for further inspection
- Automatic integration with pdf-parser for detailed analysis
- Handles encrypted and compressed PDFs at a basic level

## Installation

### Requirements

- Python 2.7 or 3.x (tested on Python 3)
- No additional dependencies beyond standard library

### Install Commands

```bash
# Download the latest version
wget https://didierstevens.com/files/software/pdfid_v0_4_11.zip
unzip pdfid_v0_4_11.zip
cd pdfid_v0_4_11

# On Kali Linux (often pre-installed or available via apt)
apt update && apt install pdfid

# On Ubuntu
wget https://didierstevens.com/files/software/pdfid_v0_4_11.zip
unzip pdfid_v0_4_11.zip
chmod +x pdfid.py

# On Windows: Download ZIP, extract, and run with python pdfid.py
```

For GitHub mirror: git clone https://github.com/didierstevens/DidierStevensSuite.git && cd DidierStevensSuite && python pdfid.py --help

## Basic Usage

```bash
python pdfid.py example.pdf
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -v | Verbose output for detailed scanning |
| -r | Recursive scan of directories |
| -e | Extract streams from the PDF |
| -a | Automatic analysis (integrates with pdf-parser.py) |
| -f <file> | Specify input file |

## Examples

### Example 1: Basic Usage

```bash
python pdfid.py /path/to/document.pdf
```

Scans a single PDF and reports keyword counts.

### Example 2: Advanced Usage

```bash
python pdfid.py -r /path/to/pdf_directory/ -v
```

Recursively scans a directory with verbose output, flagging PDFs with /JS > 0.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery (for scanning documents)
- [[Forge Web Credentials]] Forge Web Credentials (in context of analyzing credential-phishing PDFs)

### Tactics

- [[Discovery]] Discovery
- [[Initial Access]] Initial Access (phishing via documents)

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for python.exe running pdfid.py
- File access logs showing scans of PDF directories
- Network downloads of Didier Stevens Suite ZIP files
- Command-line arguments containing 'pdfid.py' in process lists

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/pdf-parser]]
- [[peid]] (for PE file analysis)
- [[exiftool]] (for metadata extraction)

## References

- Official site: https://blog.didierstevens.com/programs/pdf-tools/
- GitHub mirror: https://github.com/didierstevens/DidierStevensSuite
- Usage guide: https://didierstevens.com/files/software/pdfid_usage.txt
