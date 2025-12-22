---
id: cfce72a0-54f1-41db-9d00-288459cff8d9
type: tool
verified: true
created_at: '2019-08-28T21:17:38.464935+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - google-dorking
  - file-discovery
url: 'https://github.com/megabeets/goofile'
validated: true
---

# goofile

**Status**: Unverified

## Overview

Goofile is a reconnaissance tool designed to search for specific file types exposed on a target domain using Google dorking queries. It automates the process of identifying potentially sensitive files such as PDFs, documents, spreadsheets, and more, which may contain valuable information during security assessments.

## Description

Goofile leverages Google's search engine to perform targeted searches for file extensions within a specified domain. This passive reconnaissance technique helps in discovering publicly accessible files that could reveal internal documents, configurations, or other sensitive data without direct interaction with the target infrastructure. Commonly used in the initial phases of penetration testing to map the attack surface.

## Features

- Supports searching for various file types (e.g., pdf, doc, xls, zip)
- Domain-specific queries to focus on target scopes
- Output to file for easy parsing and integration with other tools
- Simple command-line interface for quick execution
- Handles Google rate limiting and query variations

## Installation

### Requirements

- Python 3.x
- pip package manager

### Install Commands

```bash
# On Ubuntu/Debian (including Kali)
sudo apt update
sudo apt install python3-pip
git clone https://github.com/megabeets/goofile.git
cd goofile
pip3 install -r requirements.txt
sudo cp goofile /usr/local/bin/
```

Kali Linux: Goofile is available in the repositories and can be installed via `sudo apt install goofile`.

## Basic Usage

```bash
goofile --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -d | Specify the target domain |
| -f | Specify the file type/extension |
| -o | Output results to a file |
| -g | Use Google API (if configured) |

## Examples

### Example 1: Basic Usage

```bash
goofile -d example.com -f pdf
```

This searches for PDF files on example.com and prints the URLs to the console.

### Example 2: Advanced Usage

```bash
goofile -d example.com -f doc -o documents.txt
```

This searches for DOC files and saves the results to documents.txt.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound HTTP requests to Google search endpoints with dork-like queries (e.g., site:domain filetype:pdf)
- User-Agent strings matching goofile's Python requests library
- High volume of search queries from a single IP in a short time
- Log analysis for patterns in search referral traffic

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Tool: theHarvester]]
- [[Tool: googler]]

## References

- Official GitHub Repository: https://github.com/megabeets/goofile
- Kali Tools Page: https://www.kali.org/tools/goofile/
