---
id: tool-exiftool
url: 'https://exiftool.org/'
tags:
  - metadata
  - image-manipulation
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.379Z'
validated: true
submitted: true
---
# exiftool

**Status**: Unverified

## Overview

ExifTool is a command-line application for reading, writing, and manipulating metadata in image, audio, and video files, commonly used in security testing to embed payloads in non-executable formats.

## Description

It supports over 20,000 tags across numerous file types, allowing precise metadata injection like PHP code in EXIF for file upload exploits. Ideal for creating stealthy webshells in images.

## Features

- Feature 1: Read/write EXIF, IPTC, XMP metadata
- Feature 2: Batch processing of multiple files
- Feature 3: Conditional tag editing and validation

## Installation

### Requirements

- Perl (usually pre-installed on Linux/macOS)

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt install libimage-exiftool-perl

# On macOS with Homebrew
brew install exiftool
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
| `-overwrite_original` | Overwrite original file without backup |

## Examples

### Example 1: Basic Usage

```bash
exiftool -DocumentName 'test' image.jpg
```

### Example 2: Advanced Usage

```bash
exiftool -phpinfo -b image.png > metadata.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]
- [[Remote File Copy]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for exiftool executions
- File integrity checks on images for anomalous metadata
- Log anomalous metadata writes in forensics

## Related Procedures


## Related Tools

- [[tools/metagoofil]]

## References

- Official documentation: https://exiftool.org/exiftool_pod.html
