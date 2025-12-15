---
id: tool-uuid-2
url: 'http://www.graphicsmagick.org/'
tags:
  - image-processing
  - rce-enabler
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.780Z'
validated: true
submitted: true
---
# GraphicsMagick

**Status**: Unverified

## Overview

GraphicsMagick is an alternative to ImageMagick for server-side image processing, capable of invoking Ghostscript for PostScript files, which can lead to RCE vulnerabilities when handling unvalidated uploads like disguised EPS files.

## Description

Forked from ImageMagick, it offers similar functionality for web app image conversion. In security contexts, outdated versions chained with vulnerable Ghostscript enable exploitation of file upload flaws, as seen in Basecamp's profile image processing.

## Features

- Feature 1: Fork of ImageMagick with performance optimizations
- Feature 2: Handles PostScript via external calls to Ghostscript
- Feature 3: Configurable modules; disable PS support to mitigate risks

## Installation

### Requirements

- Linux/Unix environment
- Build dependencies (e.g., freetype, jpeg)

### Install Commands

```bash
# On Ubuntu/Debian
apt update && apt install graphicsmagick

# From source
wget http://sourceforge.net/projects/graphicsmagick/files/graphicsmagick/1.3.40/GraphicsMagick-1.3.40.tar.gz
# Configure without Ghostscript if securing: ./configure --without-gs
```

## Basic Usage

```bash
gm convert input.gif output.png
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h` | Show help |
| `-debug all` | Enable debug logging for subprocess calls |

## Examples

### Example 1: Basic Usage

```bash
gm convert rce.gif thumbnail.jpg  # May invoke gs on PS content
```

### Example 2: Advanced Usage

```bash
gm convert -resize 200x200 rce.gif output.jpg
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring: gm invoking gs
- Audit uploads processed by GraphicsMagick with PS headers
- Check for unpatched versions vulnerable to chained exploits

## Related Procedures

- [[procedures/Upload-Malicious-PostScript-as-Profile-Image]]

## Related Tools

- [[tools/ImageMagick]]
- [[tools/Ghostscript]]

## References

- Official documentation: http://www.graphicsmagick.org/security.html
- Related CVEs: Chained with Ghostscript vulns
