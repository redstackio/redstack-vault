---
id: tool-libreoffice
url: 'https://www.libreoffice.org/'
tags:
  - spreadsheet
  - testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.277Z'
validated: true
submitted: true
---
# LibreOffice

**Status**: Unverified

## Overview

LibreOffice is an open-source office suite used here as spreadsheet software to test and execute CSV injection payloads, particularly for verifying formula execution with single-quote formatting.

## Description

LibreOffice Calc handles CSV imports and evaluates formulas, making it ideal for demonstrating client-side vulnerabilities in exported files. It supports various payload formats and is cross-platform for testing on different environments.

## Features

- Feature 1: CSV import with automatic formula calculation
- Feature 2: Support for single-quote prefixed formulas to bypass certain parsers
- Feature 3: Cross-platform compatibility for Linux, Windows, macOS

## Installation

### Requirements

- Compatible OS (Linux, Windows, macOS)
- Internet for download

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install libreoffice

# On Windows/macOS: Download from official site
```

## Basic Usage

```bash
libreoffice --calc malicious.csv
```

### Common Options

| Option | Description |
|--------|-------------|
| --calc | Open in Calc (spreadsheet) mode |
| --headless | Run without GUI for automation |

## Examples

### Example 1: Basic Usage

```bash
libreoffice malicious.csv
```

### Example 2: Advanced Usage

```bash
libreoffice --headless --convert-to csv:"Calc CSV (CSV) (*.csv)" input.csv
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for LibreOffice processes handling untrusted CSVs
- Log formula executions in Calc
- Alert on unexpected application launches post-CSV open

## Related Procedures

- [[procedures/CSV-Injection-in-Student-Data-Export-via-Name-Field]]
- [[procedures/Bypassing-Double-Quote-Escaping-in-CSV-Export]]

## Related Tools

- [[tools/Microsoft-Excel]]

## References

- Official documentation: https://www.libreoffice.org/get-help/documentation/
- CSV handling guide: https://help.libreoffice.org/latest/en-US/text/scalc/guide/csv_import.html
