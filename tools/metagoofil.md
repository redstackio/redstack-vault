---
id: bb1a964a-0b92-4036-a143-5857152ce625
type: tool
verified: true
created_at: '2019-08-28T21:17:20.776869+00:00'
updated_at: '2023-10-01T12:00:00+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - metadata-extraction
  - osint
url: 'https://github.com/laramies/metagoofil'
commands:
  - '[[commands/metagoofil-extract-metadata-from-domain]]'
  - '[[commands/metagoofil-view-help]]'
validated: true
---

# Metagoofil

**Status**: Unverified

## Overview

Metagoofil is an information gathering tool designed for extracting metadata from public documents available on target websites. It supports common file types like PDF, DOC, XLS, and PPT, revealing details such as author names, software versions, internal paths, and usernames that can aid in reconnaissance during security assessments.

## Description

Metagoofil automates the process of searching search engines for publicly available documents associated with a target domain, downloading them, and parsing their metadata. This passive reconnaissance technique helps identify potential entry points or internal information without direct interaction with the target network. It's particularly useful in the early stages of penetration testing for OSINT and footprinting.

## Features

- Feature 1: Searches multiple engines (Google default, others configurable) for domain-specific documents.
- Feature 2: Supports extraction from various file formats including PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX.
- Feature 3: Generates HTML reports summarizing metadata findings like authors, creation dates, and software info.
- Feature 4: Configurable limits on search results and delays to avoid rate limiting.

## Installation

### Requirements

- Python 2.7 or 3.x (though primarily tested with Python 2)
- libextractor or exiftool for metadata parsing
- wget or similar for downloading files

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install metagoofil

# Manual installation from source
sudo apt install libextractor-dev libxml2-dev libxslt1-dev
wget https://github.com/laramies/metagoofil/archive/master.zip
unzip master.zip
cd metagoofil-master
sudo python setup.py install
```

## Basic Usage

```bash
metagoofil -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -d DOMAIN | Target domain |
| -t TYPE | File types (comma-separated) |
| -l LIMIT | Result limit per type |
| -o OUTPUT | Output directory |
| -f FINAL | Final report filename |
| -w WAIT | Delay between requests |

## Examples

### Example 1: Basic Usage

Extract metadata from PDF files on a domain:

```bash
metagoofil -d example.com -t pdf -l 100 -o /tmp/output
```

This searches for up to 100 PDFs, downloads them, extracts metadata, and saves results in /tmp/output with a report.

### Example 2: Advanced Usage

Search multiple file types with delay:

```bash
metagoofil -d example.com -t pdf,doc,xls -l 200 -w 1 -o /tmp/output -f reconnaissance_report.html
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]] Gather Victim Identity Information (via author metadata)
- [[Software]] Gather Victim Organizational Information (via paths and software)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual search engine queries for filetype:pdf site:domain.com from reconnaissance IPs.
- Detection method 2: Logs of bulk downloads of public documents from the same IP.
- Detection method 3: Network traffic patterns matching Google/other search APIs with high volume.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/theHarvester]]
- [[tools/Maltego]]

## References

- Official GitHub: https://github.com/laramies/metagoofil
- Kali Tools Documentation: https://www.kali.org/tools/metagoofil
