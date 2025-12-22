---
type: tool
verified: true
created_at: '2020-02-21T01:32:32.881020+00:00'
updated_at: '2023-05-30T19:59:03.516267+00:00'
platforms:
  - Linux
tags:
  - data exposure
  - Enumeration
url: 'https://www.five-ten-sg.com/libpst/'
description: >-
  Utility for converting Microsoft Outlook PST files to standard formats like
  mbox for analysis and extraction of email content.
validated: true
---

# readpst

**Status**: ✓ Verified

## Overview

readpst is a command-line utility from the libpst suite designed to convert Microsoft Outlook Personal Storage Table (PST) files into readable formats such as mbox, allowing security analysts, forensic investigators, or red team operators to extract email content, attachments, and metadata without requiring Microsoft Outlook. It is particularly useful in post-exploitation scenarios for analyzing exfiltrated PST files on Linux systems to uncover credentials, communications, or sensitive data.

## Description

PST files are proprietary binary formats used by Outlook to store emails, contacts, calendars, and attachments. readpst parses these files and outputs them in open formats, enabling bulk processing and integration with other tools like email clients or grep for searching. Common use cases include data exfiltration analysis, incident response, and penetration testing where PST files are obtained from compromised Windows endpoints. It supports recursive processing of folder structures and can handle large PST archives, though performance may vary with file size.

## Features

- Conversion of PST to mbox format for easy import into email clients like Thunderbird.
- Extraction of individual emails as text files for targeted analysis.
- Saving attachments to a dedicated directory for separate examination.
- Support for folder hierarchy preservation in output.
- Command-line only, lightweight, and no GUI dependencies.

## Installation

### Requirements

- Linux distribution with apt package manager (e.g., Ubuntu, Kali).
- Basic build tools if compiling from source (gcc, make).

### Install Commands

On Debian/Ubuntu/Kali:

```bash
sudo apt update
sudo apt install libpst-utils
```

readpst is included in the libpst-utils package. Verify installation with `readpst --version`.

For other platforms:
- macOS: `brew install libpst`
- Windows: Use WSL or compile from source via https://www.five-ten-sg.com/libpst/

## Basic Usage

```bash
readpst -o output_dir input.pst
```

This extracts the PST contents to the specified output directory.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and usage. |
| `-V, --version` | Show version information. |
| `-o <dir>` | Specify output directory for extracted files. |
| `-m` | Generate an mbox file with all emails. |
| `-r` | Recursively process subfolders. |

## Examples

### Example 1: Basic Usage

Extract contents from a PST file to the current directory:

```bash
readpst -m example.pst
```

This creates an mbox file and text representations of emails.

### Example 2: Advanced Usage

Extract with attachments and custom output directory:

```bash
readpst -tea -o /tmp/pst_output example.pst
```

This outputs emails as text files, saves attachments, and creates an mbox in the specified directory.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Email Collection]] Email Collection
- [[Data from Local System]] Data from Local System

### Tactics

- [[Collection]] Collection
- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of libpst-utils package on non-standard systems (e.g., via `dpkg -l | grep libpst`).
- File system artifacts: Output directories with mbox files, numbered .txt email files, or attachments folders near PST sources.
- Process monitoring: `readpst` executions in logs, especially in forensic or analysis contexts.
- Network logs if PST files were exfiltrated prior to processing.

## Related Procedures

- [[procedures/Extract-Emails-and-Attachments-from-PST-Files]]

## Related Tools

- [[tools/libpst-utils]]
- [[tools/mutt]] (for viewing extracted mbox files)

## References

- Official documentation: https://www.five-ten-sg.com/libpst/
- Man page: `man readpst`
- GitHub mirror: https://github.com/libpsts/libpst
