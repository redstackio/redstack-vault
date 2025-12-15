---
url: 'https://exiftool.org/'
tags:
  - exif
  - metadata
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.386Z'
id: 53c84062-aac2-4449-a964-9c2831e163bf
validated: true
submitted: true
---
# exiftool

**Status**: Unverified

## Overview

ExifTool is a command-line application for reading, writing, and manipulating metadata in image files, commonly used in security testing to verify or extract EXIF data like GPS coordinates.

## Description

ExifTool supports a wide range of file formats, including JPEG, and can selectively read tags (e.g., GPS) or remove them. In offensive security, it's used to prepare test images or analyze leaked metadata from vulnerable uploads.

## Features

- Feature 1: Read specific tags like GPS without full dump
- Feature 2: Edit or delete metadata for evasion testing
- Feature 3: Batch processing for multiple images

## Installation

### Requirements

- Perl interpreter (included in most systems)

### Install Commands

```bash
# On Linux/macOS
sudo apt install libimage-exiftool-perl  # Debian/Ubuntu
# Or download from official site
wget https://exiftool.org/ExifTool-12.70.tar.gz
tar -xzf ExifTool-12.70.tar.gz
cd ExifTool-12.70
perl Makefile.PL
make test
make install
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
| `-GPS*` | Filter to GPS tags |

## Examples

### Example 1: Basic Usage

```bash
exiftool image.jpg
```

### Example 2: Advanced Usage

```bash
exiftool -GPS:all image.jpg
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]]
- [[Data from Information Repositories]]

### Tactics

- [[Discovery]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process name 'exiftool' in task lists
- File access logs showing metadata reads on images
- Network downloads of exiftool binaries

## Related Procedures

- [[procedures/Prepare-Images-with-EXIF-Data]]
- [[procedures/Extract-EXIF-Metadata-from-Image]]

## Related Tools

- [[tools/exif-regex-info]]

## References

- Official documentation: https://exiftool.org/exiftool_pod.html
