---
id: d12ef344-ad24-44d5-801f-b1acc232ed88
type: tool
verified: true
created_at: '2019-08-28T21:17:35.966010+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - pdf-analysis
  - forensics
  - malware-analysis
url: 'https://blog.didierstevens.com/files/software/pdf-parser_V0.7.12.zip'
commands:
  - '[[commands/pdf-parser-basic-parse]]'
  - '[[commands/pdf-parser-search-objects]]'
  - '[[commands/pdf-parser-extract-stream]]'
validated: true
---

# pdf-parser

**Status**: Unverified

## Overview

pdf-parser is a specialized Python tool for dissecting and analyzing PDF files at the structural level. It extracts objects, streams, cross-reference tables, and other low-level elements without rendering the document, making it ideal for security researchers to identify embedded malware, exploits, JavaScript, or hidden data in PDFs during offensive security operations or forensic investigations.

## Description

The tool parses PDF syntax to reveal its internal composition, supporting tasks like detecting obfuscated content, extracting embedded files, or searching for indicators of compromise. Commonly used in red teaming to craft or analyze malicious PDFs, and in blue teaming for threat hunting. It handles various PDF versions and corruption gracefully but focuses on raw structure rather than visual output.

## Features

- Feature 1: Object extraction and display of PDF internals (objects, trailers, xrefs)
- Feature 2: Keyword searching within objects for suspicious patterns like /JS or /GoToR
- Feature 3: Stream following and decoding for compressed or filtered content
- Feature 4: Support for malformed PDFs to aid in exploit development or analysis

## Installation

### Requirements

- Python 2.7 or 3.x (Python 3 recommended)
- No additional dependencies beyond standard library

### Install Commands

```bash
# Download from official source
wget https://blog.didierstevens.com/files/software/pdf-parser_V0.7.12.zip
unzip pdf-parser_V0.7.12.zip
cd pdf-parser_V0.7.12

# Or clone the suite (includes pdf-parser.py)
git clone https://github.com/DidierStevens/DidierStevensSuite.git
cd DidierStevensSuite
```

On Kali Linux, it may be available via apt, but manual download is preferred for latest version:

```bash
apt update && apt install -y python3
# Then download as above
```

## Basic Usage

```python
python pdf-parser.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -e | Display errors only |
| -o <keyword> | Search for objects containing keyword |
| -f <objnr> | Follow object number and extract stream |
| -s | Display streams |

## Examples

### Example 1: Basic Usage

```python
python pdf-parser.py document.pdf
```

### Example 2: Advanced Usage

```python
python pdf-parser.py -o /JS -s document.pdf
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[NTFS File Attributes]] Hidden Files and Directories (for analyzing embedded payloads in PDFs)
- [[Obfuscated Files or Information]] Obfuscated Files or Information (decoding obfuscated PDF streams)

### Tactics

- [[Collection]] Collection (gathering data from PDF artifacts)
- [[Impact]] Impact (analyzing for destructive payloads)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Process monitoring for python.exe/pdf-parser.py executions
- Detection method 2: File access logs showing PDF parsing on sensitive documents
- Detection method 3: Network downloads from Didier Stevens' domain

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[pefile]] (for PE analysis)
- [[tools/pdfid]] (companion PDF analysis tool)

## References

- Official documentation: https://blog.didierstevens.com/programs/pdf-tools/
- GitHub mirror: https://github.com/DidierStevens/DidierStevensSuite
- Related resources: SANS PDF Malware Reading Room
