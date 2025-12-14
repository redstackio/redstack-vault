---
url: 'https://imagemagick.org/'
tags:
  - image-processing
  - rce
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.334Z'
id: 7e632f69-5c48-48ab-83c9-76c3c8cbc243
validated: true
submitted: true
---
# ImageMagick

**Status**: Unverified

## Overview

ImageMagick is an open-source software suite for creating, editing, and processing bitmap images, commonly used in web applications for handling uploads like profile pictures. In this context, it's exploited for RCE via MVG parsing and vulnerable delegates.

## Description

ImageMagick supports various formats including vector graphics like MVG, and uses delegate files (delegates.xml) to handle external protocols such as HTTPS via curl. Vulnerable configurations allow command injection when parsing malicious inputs, enabling arbitrary execution on the server.

## Features

- Feature 1: Multi-format image conversion and manipulation
- Feature 2: Delegate system for external tools (e.g., curl for URLs)
- Feature 3: MVG support for vector graphics, parsable from ASCII

## Installation

### Requirements

- Linux/Unix system
- Development libraries (e.g., libpng, libjpeg)

### Install Commands

```bash
# On Ubuntu/Debian
apt update && apt install imagemagick
```

## Basic Usage

```bash
convert input.jpg output.png
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
convert x.gif thumbnail.jpg
```

### Example 2: Advanced Usage

```bash
convert -size 640x480 xc:white -draw "image over 0 0 0 0 https://example.com/image.png" output.png
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Unix Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor ImageMagick processes spawning curl or bash
- Log file accesses to delegates.xml
- Alert on unexpected outbound connections from convert utility

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://imagemagick.org/script/
- Related resources: CVE details for ImageMagick vulnerabilities
