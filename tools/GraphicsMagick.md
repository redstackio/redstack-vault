---
id: b19e7432-42aa-4d8f-afbb-e828981f7126
name: GraphicsMagick
type: tool
verified: false
created_at: '2025-12-11T06:10:15.540Z'
updated_at: '2025-12-11T06:10:15.540Z'
platforms:
  - Web
  - Linux
tags:
  - image-processing
  - rce
url: null
description: >-
  Fork of ImageMagick for image processing, similarly vulnerable when using
  affected Ghostscript.
validated: true
submitted: true
---

# GraphicsMagick

**Status**: Unverified

## Overview

GraphicsMagick is an image processing system forked from ImageMagick, used for server-side image manipulation and vulnerable to similar exploits involving Ghostscript.

## Description

It provides robust image processing capabilities and is often deployed in web applications, making it a target for file-based RCE attacks.

## Features

- Feature 1: Efficient image conversion.
- Feature 2: Support for PostScript via delegates.
- Feature 3: Security configurations to restrict coders.

## Installation

### Requirements

- Linux system
- Build tools

### Install Commands

```bash
sudo apt install graphicsmagick
```

## Basic Usage

```bash
gm --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-help` | Show help message |
| `-verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
gm convert input.ps output.png
```

### Example 2: Advanced Usage

```bash
gm convert -verbose input.ps output.png
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Log analysis for delegate calls.
- Detection method 2: Configuration audits for secure policies.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/ImageMagick]]
- [[tools/Ghostscript]]

## References

- Official documentation: http://www.graphicsmagick.org
