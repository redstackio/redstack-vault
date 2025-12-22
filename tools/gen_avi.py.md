---
id: tool-gen-avi-001
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/000/192/115/203df62ed08576396f9d87acd420bf51ac6ab7f1/gen_avi.py
tags:
  - avi-generation
  - malware-craft
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.390Z'
validated: true
submitted: true
---
# gen_avi.py

**Status**: Unverified

## Overview

Custom Python script to generate AVI files with embedded HLS playlists containing file:// URIs in GAB2 subtitles for local file disclosure exploits.

## Description

Used in Automattic vulnerabilities; creates valid AVI that FFmpeg processes to read and concatenate local files as video segments. Python 3 compatible; outputs binary AVI.

## Features

- Feature 1: Embeds specified file:// URI in HLS playlist
- Feature 2: Generates complete GAB2 chunk structure
- Feature 3: Ensures AVI playability for evasion

## Installation

### Requirements

- Python 3

### Install Commands

```bash
# Download
wget https://hackerone.../gen_avi.py
```

## Basic Usage

```bash
python3 gen_avi.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| No flags; positional args | file:// URI and output file |

## Examples

### Example 1: Basic Usage

```bash
python3 gen_avi.py file:///etc/passwd output.avi
```

### Example 2: Advanced Usage

For hostname:

```bash
python3 gen_avi.py file:///etc/hostname host.avi
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1587.001]] Develop Capabilities: Malware

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Generated AVIs with anomalous GAB2 sizes
- Embedded #EXTM3U strings in media files

## Related Procedures

- [[procedures/Execute-Local-File-Disclosure-via-AVI]]

## Related Tools

- [[tools/Hex-Editor]]

## References

- HackerOne Report Attachment
