---
url: 'https://exiftool.org/'
tags:
  - metadata
  - image-processing
type: tool
platforms:
  - Linux
  - Web
description: >-
  A tool for reading, writing, and editing metadata in image files, vulnerable
  to RCE via DjVu parsing in this context.
id: 98905e0d-a975-42a4-bb61-7fe2121c9b98
created_at: '2025-12-11T06:10:22.419Z'
updated_at: '2025-12-11T06:10:22.419Z'
verified: false
validated: true
submitted: true
---
# ExifTool

**Status**: Unverified

## Overview

ExifTool is used to remove non-whitelisted metadata from images but processes files based on content, enabling RCE through crafted DjVu files with injected Perl code.

## Description

In GitLab, it's integrated for metadata stripping, but insecure eval in its DjVu module allows command injection via annotations.

## Features

- Metadata reading/writing
- Supports various file formats including DjVu
- Command-line interface for batch processing

## Installation

### Requirements

- Perl installed
- Linux environment

### Install Commands

```bash
sudo apt install libimage-exiftool-perl
```

## Basic Usage

```bash
exiftool --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
exiftool image.jpg
```

### Example 2: Advanced Usage

```bash
exiftool -overwrite_original -all= image.jpg
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ExifTool process executions
- Anomalous file creations post-upload

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/GitLab-Workhorse]]

## References

- https://exiftool.org/
