---
url: 'https://www.libreoffice.org/'
tags:
  - office
  - processing
  - vulnerable
type: tool
platforms:
  - Linux
  - Cloud (AWS)
description: >-
  Open-source office suite used for document processing, vulnerable to LFI in
  file conversion via CVE-2019-17400 when integrated with unoconv.
id: cd9b9db1-be33-41e3-966c-5caa888ee9ae
created_at: '2025-12-14T03:46:14.536Z'
updated_at: '2025-12-14T03:46:14.536Z'
verified: false
validated: true
submitted: true
---
# LibreOffice

**Status**: Unverified

## Overview

LibreOffice is an open-source office productivity suite commonly used for creating and processing documents, spreadsheets, and presentations. In security contexts, it is exploited in file preview pipelines, such as Slack's thumbnail generation, where vulnerabilities allow LFI during conversion with tools like unoconv.

## Description

LibreOffice handles Office formats (e.g., .docx, .xlsx) and integrates with libraries like unoconv for automated conversions. CVE-2019-17400 enables crafted files to access local files, making it a vector for credential theft in cloud environments. It is typically deployed server-side for batch processing in web apps.

## Features

- Feature 1: Supports OLE and macro execution in documents
- Feature 2: Command-line interface for headless conversions
- Feature 3: Integration with unoconv for format transformations

## Installation

### Requirements

- Linux-based system (common in AWS containers)
- Dependencies: Java runtime for some features

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update
sudo apt install libreoffice
```

## Basic Usage

```bash
libreoffice --headless --convert-to pdf input.docx --outdir /output
```

### Common Options

| Option | Description |
|--------|-------------|
| `--headless` | Run without GUI for server use |
| `--convert-to` | Specify output format |
| `--outdir` | Output directory |

## Examples

### Example 1: Basic Usage

```bash
libreoffice --headless --convert-to png input.docx --outdir thumbnails
```

### Example 2: Advanced Usage

```bash
libreoffice --headless --convert-to thumbnail input.xlsx --outdir /tmp
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1203.001]]
- [[File and Directory Discovery]]

### Tactics

- [[Execution]]
- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor processes for libreoffice --headless in containers
- Scan for CVE-2019-17400 exploit patterns in input files
- Log file access during conversions

## Related Procedures


## Related Tools

- [[tools/unoconv]]

## References

- Official documentation: https://www.libreoffice.org/
- CVE-2019-17400 details: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17400
